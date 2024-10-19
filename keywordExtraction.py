import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import string
import nltk

# Download stopwords from nltk (only run this once if not already installed)
# nltk.download('stopwords')

# read in dataset messages
def read_data(filename):
    data = pd.read_table(filename, sep=",")
    return data.iloc[:, 11]

# writeback keywords
def writeback(filename, keywords):
    # Save the DataFrame to a CSV file
    keywords.to_csv('backend/data/' + filename + '.csv', index=False)

# Define the pipeline steps
def build_pipeline(messages):
    # Initialize the vectorizer with options for preprocessing
    vectorizer = CountVectorizer(
        stop_words=stopwords.words('english'),  # Remove stopwords
        lowercase=True,  # Convert to lowercase
        token_pattern=r'\b\w+\b',  # Include only words (removes punctuation)
        max_features=1000  # Limit the number of features to speed up processing
    )

    # Fit and transform the data (text messages)
    X_tfidf = vectorizer.fit_transform(messages)

    # Sum TF-IDF scores across all messages
    count = X_tfidf.toarray().sum(axis=0)

    # Create a DataFrame with words and their TF-IDF scores
    tfidf_frequencies = pd.DataFrame({
        'word': vectorizer.get_feature_names_out(),
        'count': count
    })

    # Sort by TF-IDF score
    top_keywords = tfidf_frequencies.sort_values(by='count', ascending=False)

    return top_keywords

# Run the pipeline

# STAT 200
messages200 = read_data("backend/data/STAT_200_Discussion_Data.csv")
top_keywords200 = build_pipeline(messages200)
writeback("STAT_200_Keywords", top_keywords200)

# CPSC 213
messages213 = read_data("backend/data/CPSC_213_Data_5.csv")
top_keywords213 = build_pipeline(messages213)
writeback("CPSC_213_Keywords", top_keywords213)
