import requests
from collections import Counter

class BreweryData:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_breweries_by_state(self, state):
        """
        Fetch all breweries in a specific state.
        """
        try:
            response = requests.get(f"{self.base_url}/breweries?by_state={state}")
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to fetch data for {state}. Status code: {response.status_code}")
                return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def list_brewery_names(self, state):
        """
        List the names of all breweries in a specific state.
        """
        breweries = self.fetch_breweries_by_state(state)
        print(f"\nBreweries in {state}:")
        for brewery in breweries:
            print(f"- {brewery.get('name', 'N/A')}")

    def count_breweries_in_state(self, state):
        """
        Count the number of breweries in a specific state.
        """
        breweries = self.fetch_breweries_by_state(state)
        print(f"\nTotal number of breweries in {state}: {len(breweries)}")

    def count_brewery_types_in_cities(self, state):
        """
        Count the number of types of breweries in individual cities of the state.
        """
        breweries = self.fetch_breweries_by_state(state)
        city_brewery_types = {}
        for brewery in breweries:
            city = brewery.get('city', 'Unknown')
            brewery_type = brewery.get('brewery_type', 'Unknown')
            if city not in city_brewery_types:
                city_brewery_types[city] = Counter()
            city_brewery_types[city][brewery_type] += 1

        print(f"\nNumber of types of breweries in individual cities of {state}:")
        for city, brewery_types in city_brewery_types.items():
            print(f"- {city}: {dict(brewery_types)}")

    def count_breweries_with_websites(self, state):
        """
        Count how many breweries have websites in a specific state.
        """
        breweries = self.fetch_breweries_by_state(state)
        breweries_with_websites = [brewery for brewery in breweries if brewery.get('website_url')]
        print(f"\nNumber of breweries with websites in {state}: {len(breweries_with_websites)}")
        print("Breweries with websites:")
        for brewery in breweries_with_websites:
            print(f"- {brewery.get('name', 'N/A')}: {brewery.get('website_url')}")


# Main program
if __name__ == "__main__":
    base_url = "https://api.openbrewerydb.org"
    states = ["Alaska", "Maine", "New York"]
    brewery_data = BreweryData(base_url)

    for state in states:
        brewery_data.list_brewery_names(state)
        brewery_data.count_breweries_in_state(state)
        brewery_data.count_brewery_types_in_cities(state)
        brewery_data.count_breweries_with_websites(state)


#sample output