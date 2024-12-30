import requests

class CountryData:
    def __init__(self, url):
        """
        Constructor to initialize the API URL.
        """
        self.url = url
        self.data = None

    def fetch_data(self):
        """
        Fetch all the JSON data from the URL.
        """
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.data = response.json()
                print("Data fetched successfully!")
            else:
                print(f"Failed to fetch data. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_countries_info(self):
        """
        Display the name of countries, currencies, and currency symbols.
        """
        if self.data:
            for country in self.data:
                name = country.get("name", {}).get("common", "N/A")
                currencies = country.get("currencies", {})
                for currency_code, currency_details in currencies.items():
                    print(f"Country: {name}, Currency: {currency_details.get('name', 'N/A')}, Symbol: {currency_details.get('symbol', 'N/A')}")
        else:
            print("No data available. Please fetch the data first.")

    def display_countries_with_currency(self, currency_name):
        """
        Display all countries that use a specific currency.
        """
        if self.data:
            countries = []
            for country in self.data:
                currencies = country.get("currencies", {})
                if any(currency.get("name", "").lower() == currency_name.lower() for currency in currencies.values()):
                    countries.append(country.get("name", {}).get("common", "N/A"))
            print(f"Countries using {currency_name.upper()}: {', '.join(countries)}")
        else:
            print("No data available. Please fetch the data first.")

# Main program
if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    country_data = CountryData(url)

    # Fetching data
    country_data.fetch_data()

    # Displaying country names, currencies, and symbols
    print("\n--- Country Information ---")
    country_data.display_countries_info()

    # Displaying countries with DOLLAR as currency
    print("\n--- Countries with DOLLAR as Currency ---")
    country_data.display_countries_with_currency("Dollar")

    # Displaying countries with EURO as currency
    print("\n--- Countries with EURO as Currency ---")
    country_data.display_countries_with_currency("Euro")
