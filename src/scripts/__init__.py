
if __name__ == "__main__":
    from scrapper import GooglePlayScrapper

    banks_to_collect_reviews = [
        {
            "package_name": "com.combanketh.mobilebanking",
            "bank_name": "Commercial Bank of Ethiopia"},
        {
            "package_name": "com.boa.boaMobileBanking",
            "bank_name": "Bank of Abyssinia"},
        {
            "package_name": "com.dashen.dashensuperapp",
            "bank_name": "Dashen Bank"}]
    
    for bank in banks_to_collect_reviews:
        scrapper = GooglePlayScrapper(
            package_name=bank["package_name"],
            bank_name=bank["bank_name"]
        )
        
        print(f"Fetching reviews for {bank['bank_name']}...")
        
        try:
            app_info = scrapper.get_app_info()
            print(f"App Info: {app_info['title']} - \n {app_info['score']}")
            
            reviews = scrapper.get_reviews(sort='NEWEST', count=500)
            print(f"Fetched {len(reviews)} reviews.")
            
            filename = f"data/{bank['bank_name'].replace(' ', '_')}_reviews.csv"
            scrapper.save_reviews_to_csv(reviews, filename)
            print(f"Reviews saved to {filename}")
        except Exception as e:
            print(f"Error fetching reviews for {bank['bank_name']}: {e}")
