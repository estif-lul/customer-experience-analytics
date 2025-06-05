from google_play_scraper import app, Sort, reviews
import csv

result, _ = reviews(
    'com.nianticlabs.pokemongo',
)
print(result[0].keys())

class GooglePlayScrapper:
    def __init__(self, package_name: str, bank_name: str ,lang: str = 'en', country: str = 'us'):
        self.package_name = package_name
        self.bank_name = bank_name
        self.lang = lang
        self.country = country

    def get_app_info(self):
        result = app(
            self.package_name,
            lang=self.lang,
            country=self.country
        )
        return app(self.package_name, lang=self.lang, country=self.country)
    
    def get_reviews(self, sort='NEWEST', count=5000):
        results, _ = reviews(
            self.package_name,
            lang=self.lang,
            country=self.country,
            sort=Sort[sort],
            count=count,
            filter_score_with=None
        )
        return results
    def save_reviews_to_csv(self, reviews, filename):
        
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
                    'user_name': entry['userName'] if 'userName' in entry else 'Anonymous'
                })