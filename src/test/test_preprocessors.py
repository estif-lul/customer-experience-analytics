import sys
sys.path.insert(1, 'src/scripts')
from preprocessors import Preprocessor


def test_detect_language():
    """Test the language detection functionality."""
    preprocessor = Preprocessor()
    text = "This is a test sentence in English."
    detected_language = preprocessor.detect_language(text)
    assert detected_language == 'en', f"Expected 'en', got '{detected_language}'"