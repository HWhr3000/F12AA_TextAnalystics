import praw
import csv

# Configure your Reddit API credentials
REDDIT_CLIENT_ID = "KiDbeHRv0qhfYfGYZutrYw"
REDDIT_CLIENT_SECRET = "gFZA_u24aRateC9q3CEkDo4EBCFJVw"
REDDIT_USER_AGENT = "my_reddit_bot_v1.0"

def fetch_reddit_comments(search_query, subreddit="all", limit=100):
    """
    Fetch comments for a given search query from a specified subreddit.
    
    Args:
    - search_query: The search string to look for.
    - subreddit: Subreddit to search within (default: "all").
    - limit: Number of posts to retrieve (default: 100).
    
    Returns:
    - comments_list: A list of dictionaries containing comment data.
    """
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT,
    )
    
    comments_list = []
    
    # Search posts in the subreddit
    for submission in reddit.subreddit(subreddit).search(search_query, limit=limit):
        submission.comments.replace_more(limit=None)  # Retrieve all comments
        for comment in submission.comments.list():
            comments_list.append({
                "post_title": submission.title,
                "post_url": submission.url,
                "comment_id": comment.id,
                "comment_body": comment.body,
                "comment_author": comment.author.name if comment.author else "deleted",
                "comment_score": comment.score,
                "comment_created_utc": comment.created_utc
            })
    
    return comments_list

def save_to_csv(data, filename="reddit_comments.csv"):
    """
    Save a list of dictionaries to a CSV file.
    
    Args:
    - data: List of dictionaries containing data to save.
    - filename: Name of the CSV file (default: "reddit_comments.csv").
    """
    if not data:
        print("No data to save.")
        return
    
    # Get fieldnames from the first dictionary
    fieldnames = data[0].keys()
    
    # Write data to CSV
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    # Example usage
    search_string = input("Enter the search string: ")
    subreddit_name = input("Enter the subreddit (or leave blank for all): ") or "all"
    post_limit = int(input("Enter the number of posts to search (default 100): ") or 100)
    
    print("Fetching comments from Reddit...")
    comments = fetch_reddit_comments(search_string, subreddit=subreddit_name, limit=post_limit)
    
    print(f"Fetched {len(comments)} comments.")
    save_to_csv(comments)