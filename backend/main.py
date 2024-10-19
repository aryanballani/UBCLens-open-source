import pandas as pd

# Step 1: Load the dataset (assuming it's in CSV format)
# Adjust the path to where your CSV file is located or replace it with your actual dataframe
df_cpsc_213_final = pd.read_csv('CPSC_213_Data.csv')

# Step 2: Clean and prepare the data
# Convert columns to datetime if they are not already in the correct format
df_cpsc_213_final['topic_created_at'] = pd.to_datetime(df_cpsc_213_final['topic_created_at'], errors='coerce')
df_cpsc_213_final['topic_posted_at'] = pd.to_datetime(df_cpsc_213_final['topic_posted_at'], errors='coerce')
df_cpsc_213_final['post_timestamp'] = pd.to_datetime(df_cpsc_213_final['post_timestamp'], errors='coerce')

# Step 3: Group by 'topic_title' and count the number of replies (posts) in each topic
top_topics = df_cpsc_213_final.groupby('topic_title').size().reset_index(name='num_replies')

# Step 4: Sort the topics by the number of replies in descending order and select the top 15
top_15_topics = top_topics.sort_values(by='num_replies', ascending=False).head(15)

# Step 5: Display the results
print("Top 15 most discussed topics based on the number of replies:")
print(top_15_topics)

# Optional: If you want to visualize the results
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.barh(top_15_topics['topic_title'], top_15_topics['num_replies'], color='skyblue')
plt.xlabel("Number of Replies")
plt.ylabel("Topics")
plt.title("Top 15 Most Discussed Topics in CPSC 213")
plt.gca().invert_yaxis()  # To display the most discussed topic at the top
plt.show()
