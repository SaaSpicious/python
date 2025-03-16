from datetime import datetime,timedelta
from flight_data import FlightData
from requests.auth import HTTPBasicAuth
import requests
import time


class DataManager:
    def __init__(self,credentials):
        self.credentials = credentials
        self.sheety_api_url = f"https://api.sheety.co/{credentials["SHEETY_USERNAME"]}/flightDealTracker/prices"
        self.sheety_api_header = {
            "Authorization": f"Bearer {credentials["SHEETY_BEARER_TOKEN"]}"
        }
        self.sheety_authorization = HTTPBasicAuth(self.credentials["SHEETY_BASIC_USER"],self.credentials["SHEETY_BASIC_PASSWORD"])
        self.amadeus_api_base_url = "https://test.api.amadeus.com/v1"
        self.amadeus_api_experimental_base_url = "https://test.api.amadeus.com/v2"

    def get_sheet_data(self):
        response = requests.get(url=self.sheety_api_url,auth=self.sheety_authorization)
        return response.json()

    def fill_airport_city_codes(self):
        airport_data = self.get_sheet_data()
        for airport in airport_data['prices']:
            if airport["iataCode"] == "":
                airport_codes = self.find_iata_code(airport["city"])
                iata_code = ""
                for code in airport_codes["data"]:
                    iata_code = code["iataCode"]
                if iata_code == "":
                    print(f"No airport found for {airport["city"]}, please refine the city name!")
                else:
                    print(f"The airport Code for {airport["city"]} is {iata_code}")
                    self.write_iata_code_to_sheet(iata_code,airport)
            else:
                print(f"Airport code found for {airport["city"]}.")

    def find_iata_code(self,city):
        bearer_token = self.get_amadeus_token()
        api_url = f"{self.amadeus_api_base_url}/reference-data/locations"
        api_header = {
            "Authorization": f"Bearer {bearer_token}"
        }

        query_params = {
            "subType": "AIRPORT",
            "keyword": city,
        }

        response = requests.get(url=api_url, headers=api_header, params=query_params)
        return response.json()

    def get_amadeus_token(self):
        amadeus_api_header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        amadeus_auth_body = {
            "grant_type": "client_credentials",
            "client_id": self.credentials["AMADEUS_API_KEY"],
            "client_secret": self.credentials["AMADEUS_API_SECRET"]
        }

        auth_response = requests.post(url=f"{self.amadeus_api_base_url}/security/oauth2/token", headers=amadeus_api_header, data=amadeus_auth_body)
        return auth_response.json()["access_token"]

    def write_iata_code_to_sheet(self,iata_code,airport):
        new_data = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.sheety_api_url}/{airport["id"]}", json=new_data, auth=self.sheety_authorization)
        print(response.status_code)

    def write_cheapest_flight_to_sheet(self,flight_response,airport):
        new_data = {
            "price": {
                "cheapFlight": flight_response
            }
        }
        response = requests.put(url=f"{self.sheety_api_url}/{airport["id"]}", json=new_data, auth=self.sheety_authorization)

    def start_querying_flights(self,base_location,days_ahead):
        airport_data = self.get_sheet_data()
        for airport in airport_data['prices']:
            if airport["iataCode"] == "":
                pass
            else:
                query_airport = airport["iataCode"]
                cheapest_flight = self.search_for_flight(base_location=base_location,iata_code=query_airport,days_ahead=days_ahead)
                if cheapest_flight and cheapest_flight.price <= float(airport["lowestPrice"]):
                    print(f"Found a cheaper flight for {airport["city"]}!")
                    return_string = cheapest_flight.stringify_cheap_flight()
                    self.write_cheapest_flight_to_sheet(return_string,airport)
                else:
                    print(f"No cheap flight found for {airport["city"]}!")
            time.sleep(3)


    def search_for_flight(self,base_location,iata_code,days_ahead):
        bearer_token = self.get_amadeus_token()
        api_url = f"{self.amadeus_api_experimental_base_url}/shopping/flight-offers"
        api_header = {
            "Authorization": f"Bearer {bearer_token}"
        }

        date = datetime.now()
        target_date = date + timedelta(days=days_ahead)

        cheapest_flights = []
        while date <= target_date:
            query_date = date.strftime("%Y-%m-%d")

            query_params = {
                "originLocationCode": base_location,
                "destinationLocationCode": iata_code,
                "departureDate": query_date,
                "adults": "1"
            }

            response = requests.get(url=api_url, headers=api_header, params=query_params)
            cheapest_flight = self.get_cheapest_flight(response.json()["data"], query_date)
            if cheapest_flight:
                cheapest_flights.append(cheapest_flight)
            date = date + timedelta(days=1)
            time.sleep(2)

        cheapest_price = 0
        cheapest_flight = None
        for flight in cheapest_flights:
            if flight and (flight.price < cheapest_price or cheapest_price == 0):
                cheapest_flight = flight
                cheapest_price = flight.price
        return cheapest_flight

    def get_cheapest_flight(self,result_json,date):
        flightList = []
        cheapest_price = 0
        cheapest_flight = None
        for flight in result_json:
            flight_object = FlightData(price=float(flight["price"]["total"]),date=date,airline=flight["validatingAirlineCodes"])
            if flight_object.price < cheapest_price or cheapest_price == 0:
                cheapest_flight = flight_object
                cheapest_price = flight_object.price
        return cheapest_flight











