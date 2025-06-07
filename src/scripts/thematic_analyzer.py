from sklearn.feature_extraction.text import TfidfVectorizer

class ThematicAnalyzer:
    def __init__(self):
        # Define thematic categories
        self.themes = {
            "Performance Issues": ["slow", "transaction", "crash", "network"],
            "Authentication Problems": ["login", "access", "error"],
            "User Interface": ["UI", "design", "navigation", "old"],
            "Application Bug": ["bug", "issue", "problem", "fails", "update"],
        }

    def get_keywords(self, text_list, top_n: int =100, ngram_range=(1, 2)):
        # Vectorize the dataset
        vectorizer = TfidfVectorizer(ngram_range=ngram_range, max_features=top_n)
        X = vectorizer.fit_transform(text_list)

        # Get top keywords
        keywords = vectorizer.get_feature_names_out()
        return keywords
    
    def assign_theme(self, text):
        assigned_themes = [theme for theme, words in self.themes.items() if any(word in text for word in words)]
        return assigned_themes if assigned_themes else ["Other"]
        