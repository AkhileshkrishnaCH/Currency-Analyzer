import os
from icrawler.builtin import BingImageCrawler


currencies = {
    "INR": "Indian rupee banknote",
    "USD": "US dollar banknote",
    "EUR": "Euro banknote",
    "GBP": "British pound banknote",
    "JPY": "Japanese yen banknote",
    "CNY": "Chinese yuan banknote",
}


dataset_path = "dataset"


for currency, keyword in currencies.items():

    save_folder = os.path.join(dataset_path, currency)

    os.makedirs(save_folder, exist_ok=True)

    crawler = BingImageCrawler(storage={"root_dir": save_folder})

    print(f"Downloading images for {currency}...")

    crawler.crawl(keyword=keyword, max_num=40)

print("Download complete.")
