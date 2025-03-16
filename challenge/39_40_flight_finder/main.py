from credential_manager import Credentials
from data_manager import DataManager

data = Credentials()
credentials = data.get_credentials()
data_manager = DataManager(credentials)
data_manager.fill_airport_city_codes()
data_manager.get_sheet_data()
data_manager.start_querying_flights(base_location="FRA",days_ahead=4)