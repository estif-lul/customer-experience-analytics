from sklearn.feature_extraction.text import TfidfVectorizer

class ThematicAnalyzer:
    """ThematicAnalyzer class for analyzing themes in text data using TF-IDF."""
    def __init__(self):
        # Define thematic categories
        self.themes = {
            "Performance Issues": ["slow", "transaction", "crash", "network"],
            "Authentication Problems": ["login", "access", "error"],
            "User Interface": ["UI", "design", "navigation", "old"],
            "Application Bug": ["bug", "issue", "problem", "fails", "update"],
        }

    def get_keywords(self, text_list, top_n: int =100, ngram_range=(1, 2)):
        """Extract top keywords from a list of text using TF-IDF.
        Parameters:
            text_list (list): List of text documents to analyze.
            top_n (int): Number of top keywords to return.
            ngram_range (tuple): Range of n-grams to consider (default is unigrams and bigrams).
        Returns:
            list: List of top keywords extracted from the text documents.
        """
        # Vectorize the dataset
        vectorizer = TfidfVectorizer(ngram_range=ngram_range, max_features=top_n)
        X = vectorizer.fit_transform(text_list)

        # Get top keywords
        keywords = vectorizer.get_feature_names_out()
        return keywords
    
    def assign_theme(self, text):
        """Assign a theme to the given text based on predefined themes.
        Parameters:
            text (str): The input text to analyze.
        Returns:
            list: List of themes assigned to the text. If no themes match, returns ["Other"].
        """
        assigned_themes = [theme for theme, words in self.themes.items() if any(word in text for word in words)]
        return assigned_themes if assigned_themes else ["Other"]
        