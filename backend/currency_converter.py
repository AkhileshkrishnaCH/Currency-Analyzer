import requests


def convert_to_inr(currency):

    if currency == "INR":
        return 1

    try:

        url = f"https://open.er-api.com/v6/latest/{currency}"

        response = requests.get(url)
        data = response.json()

        rate = data["rates"]["INR"]

        return rate

    except:

        print("Exchange rate API error. Using fallback rate.")

        fallback_rates = {
            "USD": 83,
            "EUR": 90,
            "GBP": 105,
            "JPY": 0.55,
            "CNY": 11.5,
        }

        return fallback_rates.get(currency, 1)
