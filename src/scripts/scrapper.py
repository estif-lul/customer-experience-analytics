from google_play_scraper import app, Sort, reviews
import csv


# This class is designed to scrape reviews from the Google Play Store for a specific banking app.
class GooglePlayScrapper:
    """GooglePlayScrapper is a class that scrapes reviews from the Google Play Store for a specified banking app.
    Parameters:
            package_name (str): The package name of the app to fetch information for.
            bank_name (str): The name of the bank associated with the app.
            lang (str): The language code for the app information (default is 'en').
            country (str): The country code for the app information (default is 'us').
    """
    
    def __init__(self, package_name: str, bank_name: str ,lang: str = 'en', country: str = 'us'):
        self.package_name = package_name
        self.bank_name = bank_name
        self.lang = lang
        self.country = country

    # This method retrieves the app information such as title, score, and description.
    # It uses the package name, language, and country to fetch the relevant data.
    # Returns a dictionary containing the app information.
    def get_app_info(self):
        """Fetches app information from the Google Play Store.
        
        Returns:
            dict: A dictionary containing app information such as title, score, and description.
        """

        try:
            result = app(
                self.package_name,
                lang=self.lang,
                country=self.country
            )
        except Exception as e:
            raise Exception(f"Error fetching app info for {self.bank_name}: {e}") from e
        return result
    
    # This method fetches reviews for the app.
    # It allows sorting by 'NEWEST' or other criteria and specifies the number of reviews to fetch.
    # Returns a list of reviews.
    # The reviews include details such as review text, rating, date, bank name, source, and user name.
    def get_reviews(self, sort: str = 'NEWEST', count: int = 5000):
        """Fetches reviews for the app from the Google Play Store.
        Parameters:
            sort (str): The sorting order for the reviews (default is 'NEWEST').
            count (int): The number of reviews to fetch (default is 5000).
        Returns:
            list: A list of reviews, each containing review text, rating, date, bank name, source, and user name.
        Raises:
            ValueError: If the sort parameter is not recognized.
            Exception: If there is an error fetching the reviews.
        """
        try:
            results, _ = reviews(
                self.package_name,
                lang=self.lang,
                country=self.country,
                sort=Sort[sort],
                count=count,
                filter_score_with=None
            )
            return results
        except ValueError as e:
            raise ValueError(f"Invalid sort parameter: {sort}. Use 'NEWEST', 'RATING', or 'MOST_RELEVANT'.") from e
        except Exception as e:
            raise Exception(f"Error fetching reviews for {self.bank_name}: {e}") from e
    
    # This method saves the fetched reviews to a CSV file.
    # It takes a dictionary of reviews and a filename as parameters.
    # Each review is written with fields such as review text, rating, date, bank name, source, and user name.
    def save_reviews_to_csv(self, reviews: dict, filename: str):
        """Saves the fetched reviews to a CSV file.
        Parameters:
            reviews (list): A list of reviews to save.
            filename (str): The name of the file to save the reviews to.
        Raises:
            Exception: If there is an error writing to the CSV file.
        """
        
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source', 'user_name'])
                writer.writeheader()
                for entry in reviews:
                    writer.writerow({
                        'review_text': entry['content'],
                        'rating': entry['score'],
                        'date': entry['at'].strftime('%Y-%m-%d'),
                        'bank_name': self.bank_name,
                        'source': 'Google Play',
                        'user_name': entry['userName']
                    })
        except Exception as e:
            raise Exception(f"Error saving reviews to {filename}: {e}") from e