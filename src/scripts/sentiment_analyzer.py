from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

class SentimentAnalyzer:
    """SentimentAnalyzer class for analyzing sentiment using TextBlob, VADER, and DistilBERT."""
    def __init__(self, model: str = 'distilbert-base-uncased-finetuned-sst-2-english'):
        """Initialize the SentimentAnalyzer with DistilBERT model.
        Parameters:
            model (str): The name of the DistilBERT model to use for sentiment analysis."""
        self.tokenizer = DistilBertTokenizer.from_pretrained(model)
        self.model = DistilBertForSequenceClassification.from_pretrained(model)

    def get_textblob_sentiment(self, text: str):
        """Analyze sentiment using TextBlob.
        Parameters:
            text (str): The input text for sentiment analysis.
        Returns:
            str: Sentiment label ('positive', 'negative', or 'neutral').
        """
        blob = TextBlob(text)
        if blob.sentiment.polarity > 0:
            return 'positive'
        elif blob.sentiment.polarity < 0:
            return 'negative'
        else:
            return 'neutral'
        
    def get_vader_sentiment(self, text: str):
        """Analyze sentiment using VADER.
        Parameters:
            text (str): The input text for sentiment analysis.
        Returns:
            str: Sentiment label ('positive', 'negative', or 'neutral').
        """
        sia = SentimentIntensityAnalyzer()

        score = sia.polarity_scores(text)
        if score['compound'] > 0.05:
            return 'positive'
        elif score['compound'] < -0.05:
            return 'negative'
        else:
            return 'neutral'
        
    def get_distilbert_sentiment(self, text: str):
        """Analyze sentiment using DistilBERT.
        Parameters:
            text (str): The input text for sentiment analysis.
        Returns:
            str: Sentiment label based on DistilBERT classification.
        """
        # Tokenize the input text
        inputs = self.tokenizer(text, return_tensors="pt")

        with torch.no_grad():
            logits = self.model(**inputs).logits
        # Get the predicted class ID
        # DistilBERT outputs logits for two classes: 0 (negative) and 1 (positive)
        # We take the argmax to get the predicted class
        predicted_class_id = logits.argmax().item()
        return self.model.config.id2label[predicted_class_id]