from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

class SentimentAnalyzer:
    def __init__(self, model: str = 'distilbert-base-uncased-finetuned-sst-2-english'):
        
        self.tokenizer = DistilBertTokenizer.from_pretrained(model)
        self.model = DistilBertForSequenceClassification.from_pretrained(model)

    def get_textblob_sentiment(self, text: str):
        blob = TextBlob(text)
        if blob.sentiment.polarity > 0:
            return 'positive'
        elif blob.sentiment.polarity < 0:
            return 'negative'
        else:
            return 'neutral'
        
    def get_vader_sentiment(self, text: str):
        sia = SentimentIntensityAnalyzer()

        score = sia.polarity_scores(text)
        if score['compound'] > 0.05:
            return 'positive'
        elif score['compound'] < -0.05:
            return 'negative'
        else:
            return 'neutral'
        
    def get_distilbert_sentiment(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            logits = self.model(**inputs).logits
        predicted_class_id = logits.argmax().item()
        return self.model.config.id2label[predicted_class_id]