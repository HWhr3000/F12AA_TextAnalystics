import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer once for efficiency.
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    """
    Returns the sentiment of the provided text as 'Positive', 'Negative', or 'Neutral'.
    Uses VADER's compound score:
      - Positive if compound score >= 0.05
      - Negative if compound score <= -0.05
      - Neutral otherwise.
    """
    # Ensure text is a string
    if not isinstance(text, str):
        text = str(text)
        
    vs = analyzer.polarity_scores(text)
    compound = vs['compound']
    
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def main():
    # Define the path to your CSV file. Change the file name/path as necessary.
    csv_file_path = "../Data/processed/noon_filtered_comments_20250128_221435.csv"
    
    # Load the CSV file into a Pandas DataFrame.
    # Adjust the sep parameter if your CSV uses a different delimiter (e.g., sep='\t' for tab-delimited).
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return
    
    # Check if the expected column exists
    if 'comment_text' not in df.columns:
        print("The CSV file does not contain a 'comment_text' column.")
        return
    
    # Apply the sentiment analysis function to the comment_text column.
    df['Sentiment'] = df['comment_text'].apply(get_sentiment)
    
    # Print the first few rows to verify the results
    print(df[['comment_text', 'Sentiment']].head())
    
    # Optionally, save the DataFrame with the sentiment analysis to a new CSV file.
    output_file = "../Data/processed/noon_filtered_comments_with_sentiment.csv"
    try:
        df.to_csv(output_file, index=False)
        print(f"Sentiment analysis complete. Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving the output CSV file: {e}")

if __name__ == "__main__":
    main()