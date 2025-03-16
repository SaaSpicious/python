class FlightData:

    def __init__(self,price,date,airline):
        self.price = price
        self.date = date
        self.airline = airline

    def stringify_cheap_flight(self):
        return_string = f"There's a flight by {self.airline} on {self.date} for {self.price} Euros."
        return return_string
