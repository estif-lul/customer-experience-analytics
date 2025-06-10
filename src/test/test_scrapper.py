import sys
sys.path.insert(1, 'src/scripts')
from scrapper import GooglePlayScrapper

import os

def test_get_app_info():
    """Test the get_app_info method of GooglePlayScrapper."""
    scrapper = GooglePlayScrapper(package_name='com.combanketh.mobilebanking', bank_name='Commercial Bank of Ethiopia')
    app_info = scrapper.get_app_info()
    
    assert isinstance(app_info, dict), "Expected app_info to be a dictionary"
    assert 'title' in app_info, "App info should contain 'title'"
    assert 'score' in app_info, "App info should contain 'score'"
    assert 'description' in app_info, "App info should contain 'description'"

def test_get_reviews():
    """Test the get_reviews method of GooglePlayScrapper."""
    scrapper = GooglePlayScrapper(package_name='com.combanketh.mobilebanking', bank_name='Commercial Bank of Ethiopia')
    reviews = scrapper.get_reviews(sort='NEWEST', count=10)
    
    assert isinstance(reviews, list), "Expected reviews to be a list"
    assert len(reviews) <= 10, "Expected at most 10 reviews"
    
    for review in reviews:
        assert 'content' in review, "Each review should contain 'content' key"
        assert 'score' in review, "Each review should contain 'score' key"
        assert 'at' in review, "Each review should contain 'at' key"
        assert 'userName' in review, "Each review should contain 'userName' key"

def save_reviews_to_csv():
    """Test the save_reviews_to_csv method of GooglePlayScrapper."""
    scrapper = GooglePlayScrapper(package_name='com.example.app', bank_name='Example Bank')
    reviews = scrapper.get_reviews(sort='NEWEST', count=10)
    
    filename = 'test_reviews.csv'
    scrapper.save_reviews_to_csv(reviews, filename)
    
    # Check if the file was created
    assert os.path.exists(filename), f"File {filename} should be created"
    
    # Clean up the test file
    os.remove(filename)