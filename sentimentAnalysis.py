import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax
import torch

# Load pre-trained BERT model and tokenizer
model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# Sentiment Analysis Function
def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        # Compute probabilities with softmax
        probs = softmax(logits, dim=-1)
        predicted_class = torch.argmax(probs).item()
        sentiment_labels = ["very negative", "negative", "neutral", "positive", "very positive"]
        return sentiment_labels[predicted_class], probs

def read_data(filename):
    data = pd.read_table(filename, sep=",")
    return data.iloc[:, 11]

def writeback(filename, counts, size):
    percentages =(counts / size * 100).to_dict()

    df = pd.DataFrame(list(percentages.items()), columns=['Sentiment', 'Percentage'])

    # Save the DataFrame to a CSV file
    df.to_csv('backend/data/' + filename + '.csv', index=False)


# Example usage
if __name__ == "__main__":
    # # CPSC 213
    # sentimentPredictions213 = []
    # messages = read_data("backend/data/CPSC_213_Data_5.csv")
    # tempMessages = messages[:2000]
    # for message in tempMessages:
    #     sentiment, probabilities = analyze_sentiment(message)
    #     sentimentPredictions213.append(sentiment)
    #     # print(f"Message: {message}")
    #     # print(f"Sentiment: {sentiment}")

    # # Count sentiment predictions
    # size213 = len(sentimentPredictions213)
    # series213 = pd.Series(sentimentPredictions213)
    # counts213 = series213.value_counts()
    # print(counts213)
    # writeback("CPSC_213_Percentages", counts213, size213)
    # print("CPSC 213 Sentiment Predictions Done")

    # STAT 200
    sentimentPredictions200 = []
    messages = read_data("backend/data/STAT_200_Discussion_Data.csv")
    for message in messages:
        sentiment, probabilities = analyze_sentiment(message)
        sentimentPredictions200.append(sentiment)
        # print(f"Message: {message}")
        # print(f"Sentiment: {sentiment}")

    # Count sentiment predictions
    size200 = len(sentimentPredictions200)
    series200 = pd.Series(sentimentPredictions200)
    counts200 = series200.value_counts()
    print(counts200)
    writeback("STAT_200_Percentages", counts200, size200)
    print("STAT 200 Sentiment Predictions Done")

    # # CPSC 221
    # sentimentPredictions221 = []
    # messages = read_data("backend/CPSC_213_Data_4.csv")
    # tempMessages = messages[328:342]
    # for message in tempMessages:
    #     sentiment, probabilities = analyze_sentiment(message)
    #     sentimentPredictions221.append(sentiment)
    #     # print(f"Message: {message}")
    #     # print(f"Sentiment: {sentiment}")

    # # Count sentiment predictions
    # size221 = len(sentimentPredictions221)
    # series221 = pd.Series(sentimentPredictions221)
    # counts221 = series221.value_counts()
    # print("CPSC 221 Sentiment Predictions Done")

