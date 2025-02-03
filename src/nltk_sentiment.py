import pandas as pd
import nltk
# Download the VADER lexicon (only needs to be done once) - Take it outside execution if we see error
# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer from NLTK.
analyzer = SentimentIntensityAnalyzer()

def get_sentiment_details(text):
    """
    Returns a dictionary of sentiment scores for the given text.
    The dictionary contains:
      - Sentence: the original text
      - Positive: positive score from VADER
      - Negative: negative score from VADER
      - Neutral: neutral score from VADER
      - Overall: compound score from VADER
    """
    if not isinstance(text, str):
        text = str(text)
    scores = analyzer.polarity_scores(text)
    return {
        'Sentence': text,
        'Positive': scores['pos'],
        'Negative': scores['neg'],
        'Neutral': scores['neu'],
        'Overall': scores['compound']
    }

def get_sentiment_label(compound_score):
    """
    Returns the sentiment label ('Positive', 'Negative', or 'Neutral') based on the compound score.
      - Positive: compound >= 0.05
      - Negative: compound <= -0.05
      - Neutral: otherwise
    """
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def main():
    # Define the path to your CSV file.
    csv_file_path = "../Data/processed/noon_filtered_comments_with_sentiment.csv"
    
    # Load the CSV file into a Pandas DataFrame.
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return
    
    # Verify that the expected column exists.
    if 'comment_text' not in df.columns:
        print("The CSV file does not contain a 'comment_text' column.")
        return

    # Apply sentiment analysis on each comment.
    sentiment_details_list = []
    sentiment_labels = []
    for comment in df['comment_text']:
        details = get_sentiment_details(comment)
        sentiment_details_list.append(details)
        sentiment_labels.append(get_sentiment_label(details['Overall']))
    
    # Add detailed sentiment scores and label as new columns in the DataFrame.
    df['Positive'] = [detail['Positive'] for detail in sentiment_details_list]
    df['Negative'] = [detail['Negative'] for detail in sentiment_details_list]
    df['Neutral'] = [detail['Neutral'] for detail in sentiment_details_list]
    df['Overall'] = [detail['Overall'] for detail in sentiment_details_list]
    df['Sentiment_Nltk'] = sentiment_labels
    
    # Display the first few rows to verify the results.
    print(df[['comment_text', 'Sentiment_Nltk', 'Positive', 'Negative', 'Neutral', 'Overall']].head())
    
    # Sort the comments to get the top strongly positive and negative ones.
    sorted_positive = sorted(sentiment_details_list, key=lambda x: x['Overall'], reverse=True)
    sorted_negative = sorted(sentiment_details_list, key=lambda x: x['Overall'])
    
    tweet_qty = min(10, len(sentiment_details_list) // 2)
    
    print("\nThe top {} strongly positive comments are:".format(tweet_qty))
    for i in range(tweet_qty):
        pos_comment = sorted_positive[i]
        if pos_comment['Overall'] != 0:
            print("\n{}\nPositive score: {:.3f}, Negative score: {:.3f}, Neutral score: {:.3f}, Overall: {:.3f}"
                  .format(pos_comment['Sentence'], pos_comment['Positive'], pos_comment['Negative'], pos_comment['Neutral'], pos_comment['Overall']))
        else:
            print("\n{}\nNeutral comment with not much emotion".format(pos_comment['Sentence']))
    
    print("\nThe top {} strongly negative comments are:".format(tweet_qty))
    for i in range(tweet_qty):
        neg_comment = sorted_negative[i]
        if neg_comment['Overall'] != 0:
            print("\n{}\nPositive score: {:.3f}, Negative score: {:.3f}, Neutral score: {:.3f}, Overall: {:.3f}"
                  .format(neg_comment['Sentence'], neg_comment['Positive'], neg_comment['Negative'], neg_comment['Neutral'], neg_comment['Overall']))
        else:
            print("\n{}\nNeutral comment with not much emotion".format(neg_comment['Sentence']))
    
    # Optionally, save the DataFrame with the sentiment analysis to a new CSV file.
    output_file = "../Data/processed/noon_filtered_comments_with_sentiment_nltk.csv"
    try:
        df.to_csv(output_file, index=False)
        print(f"\nSentiment analysis complete. Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving the output CSV file: {e}")

if __name__ == "__main__":
    main()