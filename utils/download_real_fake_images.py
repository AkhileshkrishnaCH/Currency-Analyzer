import os
from icrawler.builtin import BingImageCrawler


currencies = ["INR", "USD", "EUR", "GBP", "JPY", "CNY"]

real_queries = {
    "INR": "Indian rupee banknote",
    "USD": "US dollar banknote",
    "EUR": "Euro banknote",
    "GBP": "British pound banknote",
    "JPY": "Japanese yen banknote",
    "CNY": "Chinese yuan banknote",
}

fake_queries = {
    "INR": "fake Indian rupee banknote",
    "USD": "fake US dollar banknote",
    "EUR": "fake Euro banknote",
    "GBP": "fake British pound banknote",
    "JPY": "fake Japanese yen banknote",
    "CNY": "fake Chinese yuan banknote",
}


dataset_path = "dataset"


for currency in currencies:

    real_path = os.path.join(dataset_path, currency, "real")
    fake_path = os.path.join(dataset_path, currency, "fake")

    os.makedirs(real_path, exist_ok=True)
    os.makedirs(fake_path, exist_ok=True)

    print(f"\nDownloading REAL {currency} images")

    crawler = BingImageCrawler(storage={"root_dir": real_path})
    crawler.crawl(keyword=real_queries[currency], max_num=80)

    print(f"Downloading FAKE {currency} images")

    crawler = BingImageCrawler(storage={"root_dir": fake_path})
    crawler.crawl(keyword=fake_queries[currency], max_num=80)


print("\nDownload complete")
