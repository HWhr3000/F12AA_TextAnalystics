import pandas as pd
from datetime import datetime

# Read both CSV files
df1 = pd.read_csv('noon_filtered_comments_20250128_221435.csv')
df2 = pd.read_csv('noon_filtered_comments_extended_20250128_231246.csv')

# Combine the dataframes and remove duplicates based on comment_id
combined_df = pd.concat([df1, df2], ignore_index=True)
combined_df = combined_df.drop_duplicates(subset='comment_id', keep='first')

# Sort by created_utc
combined_df['created_utc'] = pd.to_datetime(combined_df['created_utc'])
combined_df = combined_df.sort_values('created_utc', ascending=False)

# Save the combined file with current timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f'noon_filtered_comments_combined_{timestamp}.csv'
combined_df.to_csv(output_file, index=False)

print(f"Original number of comments in first file: {len(df1)}")
print(f"Original number of comments in second file: {len(df2)}")
print(f"Total number of unique comments after combining: {len(combined_df)}")
print(f"Combined file saved as: {output_file}")
