import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

class Preprocessor:

    # Custom language detector factory function
    @Language.factory("language_detector") 
    def create_language_detector(nlp, name):
        return LanguageDetector() # Create the detector component

    def detect_language(self, text):
        nlp = spacy.load("en_core_web_lg")
        nlp.add_pipe('language_detector', last=True)
        doc = nlp(text)
        return doc._.language['language']
    
    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words('english'))
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
        return ' '.join(tokens)