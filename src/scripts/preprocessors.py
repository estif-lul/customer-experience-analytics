import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

class Preprocessor:
    """Preprocessor class for text preprocessing and language detection."""

    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('punkt_tab')
        nltk.download('vader_lexicon')

    # Custom language detector factory function
    @Language.factory("language_detector") 
    def create_language_detector(nlp, name):
        return LanguageDetector() # Create the detector component

    def detect_language(self, text):
        """Detect the language of the given text.
        Parameters:
            text (str): The input text for language detection.
        Returns:
            str: Detected language code (e.g., 'en' for English).
        """

        # Load the language model and add the language detector
        nlp = spacy.load("en_core_web_lg")
        # Add the language detector to the pipeline
        nlp.add_pipe('language_detector', last=True)
        doc = nlp(text)
        return doc._.language['language']
    
    def preprocess_text(self, text):
        """Preprocess the input text by tokenizing, lemmatizing, and removing stop words.
        Parameters:
            text (str): The input text to preprocess.
        Returns:
            str: Preprocessed text as a single string.
        """
        tokens = word_tokenize(text.lower()) # Tokenize and convert to lowercase
        lemmatizer = WordNetLemmatizer() # Initialize the lemmatizer
        stop_words = set(stopwords.words('english')) # Get English stop words
        # Lemmatize tokens, remove non-alphanumeric tokens and stop words
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
        return ' '.join(tokens)