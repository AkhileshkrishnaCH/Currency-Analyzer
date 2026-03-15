import os
from icrawler.builtin import BingImageCrawler

dataset_path = "dataset"

denominations = {
    "INR": ["10", "20", "50", "100", "200", "500", "2000"],
    "USD": ["1", "5", "10", "20", "50", "100"],
    "EUR": ["5", "10", "20", "50", "100", "200", "500"],
    "GBP": ["5", "10", "20", "50"],
    "JPY": ["1000", "2000", "5000", "10000"],
    "CNY": ["1", "5", "10", "20", "50", "100"],
}

download_per_denom = 3

for currency, denom_list in denominations.items():

    for category in ["real", "fake"]:

        folder = os.path.join(dataset_path, currency, category)

        os.makedirs(folder, exist_ok=True)

        for denom in denom_list:

            if category == "real":
                query = f"{currency} {denom} banknote"
            else:
                query = f"fake {currency} {denom} banknote"

            print(f"Downloading {query}")

            crawler = BingImageCrawler(storage={"root_dir": folder})

            crawler.crawl(keyword=query, max_num=download_per_denom)

print("\nDenomination coverage download complete")
