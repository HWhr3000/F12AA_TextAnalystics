import praw
import pandas as pd
from datetime import datetime
import time
from typing import List, Dict
import re

class RedditScraper:
    def __init__(self, client_id: str, client_secret: str, user_agent: str):
        """Initialize Reddit API client."""
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        # Extended list of relevant subreddits
        self.subreddits = [
            'dubai', 'abudhabi', 'UAE', 'DubaiCentral', 
            'DubaiPetrolHeads', 'dubaiclassifieds', 'dubaigaming',
            'UAEexchange', 'sharjah', 'ajman', 'RAK', 'mydubai',
            'dubaifood', 'dubaipets', 'dubailife'
        ]
        
    def contains_noon_reference(self, text: str) -> bool:
        """Check if text contains reference to noon (case insensitive)."""
        keywords = [
            r'\bnoon\b', 'noon.com', 'noon food', 'noon delivery',
            'noon express', 'noon grocery', 'noon shopping',
            'noon marketplace', 'noon seller', 'noon daily'
        ]
        if not text:
            return False
        text = text.lower()
        return any(re.search(keyword.lower(), text) for keyword in keywords)
    
    def clean_text(self, text: str) -> str:
        """Clean text by removing extra whitespace and newlines."""
        if not text:
            return ""
        # Replace newlines with spaces
        text = text.replace('\n', ' ')
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    def process_comment(self, comment, post_id: str, post_title: str) -> Dict:
        """Process a comment and return its data."""
        return {
            'post_id': post_id,
            'post_title': post_title,
            'comment_id': comment.id,
            'author': str(comment.author),
            'comment_text': self.clean_text(comment.body),
            'score': comment.score,
            'created_utc': datetime.fromtimestamp(comment.created_utc),
            'is_submitter': comment.is_submitter,
            'contains_noon_mention': self.contains_noon_reference(comment.body),
            'subreddit': str(comment.subreddit)
        }
    
    def collect_comments(self, query: str, time_filter: str = 'all') -> List[Dict]:
        """Collect comments from posts matching the query."""
        all_comments = []
        
        for subreddit_name in self.subreddits:
            try:
                print(f"\nSearching in r/{subreddit_name} for: {query}")
                subreddit = self.reddit.subreddit(subreddit_name)
                # Increased limit to 100 posts per search
                posts = subreddit.search(query, time_filter=time_filter, limit=100)
                
                for post in posts:
                    # Process posts that either mention noon or have relevant comments
                    post_relevant = self.contains_noon_reference(post.title + ' ' + post.selftext)
                    
                    print(f"Processing post: {post.title[:50]}...")
                    
                    # Add the post itself as a "comment" with type='post'
                    post_data = {
                        'post_id': post.id,
                        'post_title': post.title,
                        'comment_id': post.id,
                        'author': str(post.author),
                        'comment_text': self.clean_text(post.selftext),
                        'score': post.score,
                        'created_utc': datetime.fromtimestamp(post.created_utc),
                        'is_submitter': True,
                        'contains_noon_mention': post_relevant,
                        'type': 'post',
                        'subreddit': str(post.subreddit)
                    }
                    
                    if post_relevant:
                        all_comments.append(post_data)
                    
                    # Process comments with higher limit
                    post.comments.replace_more(limit=5)  # Allow some MoreComments expansion
                    for comment in post.comments.list():
                        try:
                            comment_data = self.process_comment(comment, post.id, post.title)
                            comment_data['type'] = 'comment'
                            # Include comment if either the post or comment is relevant
                            if post_relevant or comment_data['contains_noon_mention']:
                                all_comments.append(comment_data)
                        except Exception as e:
                            print(f"Error processing comment: {str(e)}")
                            continue
                    
                    time.sleep(0.5)  # Respect rate limits
                    
            except Exception as e:
                print(f"Error processing subreddit {subreddit_name}: {str(e)}")
                continue
        
        return all_comments

def main():
    # Reddit API credentials
    CLIENT_ID = 'i2azsuZjoSWO6wzyRSZGrg'
    CLIENT_SECRET = 'KFHbkissjoq-K3IDx-daXyXpe8vYZQ'
    USER_AGENT = 'Noon Comment Scraper Extended v1.0'
    
    # Initialize scraper
    scraper = RedditScraper(CLIENT_ID, CLIENT_SECRET, USER_AGENT)
    
    # Extended search terms related to Noon
    search_terms = [
        'noon.com', 'noon UAE', 'noon delivery', 'noon shopping',
        'noon dubai', 'noon', 'noon food', 'noon express',
        'noon marketplace', 'noon seller', 'noon daily',
        'noon grocery', 'noon minutes', 'noon now',
        'noon sale', 'noon discount', 'noon review',
        'noon experience', 'noon courier', 'noon order'
    ]
    
    # Time periods to search
    time_periods = ['all']  # Can add 'year', 'month' if needed
    
    # Collect all comments
    all_comments = []
    for term in search_terms:
        for period in time_periods:
            comments = scraper.collect_comments(term, time_filter=period)
            all_comments.extend(comments)
            print(f"Collected {len(comments)} items for '{term}' in period '{period}'")
    
    # Convert to DataFrame
    df = pd.DataFrame(all_comments)
    
    # Remove duplicates based on comment_id
    df = df.drop_duplicates(subset='comment_id')
    
    # Create separate DataFrames
    posts_df = df[df['type'] == 'post'].copy()
    comments_df = df[df['type'] == 'comment'].copy()
    
    # Filter comments to only those mentioning noon
    noon_comments_df = comments_df[comments_df['contains_noon_mention']].copy()
    
    # Save to CSV files with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save all data
    df.to_csv(f'noon_all_data_extended_{timestamp}.csv', index=False)
    
    # Save filtered data
    noon_comments_df.to_csv(f'noon_filtered_comments_extended_{timestamp}.csv', index=False)
    posts_df.to_csv(f'noon_posts_extended_{timestamp}.csv', index=False)
    
    # Print summary
    print("\nScraping Complete!")
    print(f"Total posts collected: {len(posts_df)}")
    print(f"Total comments collected: {len(comments_df)}")
    print(f"Comments mentioning noon: {len(noon_comments_df)}")
    print("\nFiles created:")
    print(f"1. noon_all_data_extended_{timestamp}.csv (all posts and comments)")
    print(f"2. noon_filtered_comments_extended_{timestamp}.csv (only comments mentioning noon)")
    print(f"3. noon_posts_extended_{timestamp}.csv (only posts)")
    
    # Print subreddit distribution
    print("\nDistribution across subreddits:")
    print(noon_comments_df['subreddit'].value_counts())

if __name__ == "__main__":
    main()
