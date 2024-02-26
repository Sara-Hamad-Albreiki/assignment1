class Passenger:
    def __init__(self, passenger_id, passenger_name, passenger_email):
        self.passenger_name = passenger_name
        self.passenger_id = passenger_id
        self.passenger_email = passenger_email

    def get_passenger_name(self):
        return self.passenger_name

    def get_passenger_id(self):
        return self.passenger_id

    def get_passenger_email(self):
        return self.passenger_email

    def set_passenger_email(self, new_email):
        self.passenger_email = new_email


class Ticket(Passenger):
    def __init__(self, passenger_id, passenger_name, passenger_email, ticket_num, flight_num):
        super().__init__(passenger_id, passenger_name, passenger_email)
        self.ticket_num = ticket_num
        self.flight_num = flight_num

    def get_ticket_num(self):
        return self.ticket_num

    def display_ticket_num(self):
        return self.ticket_num

    def get_flight_num(self):
        return self.flight_num

    def display_flight_num(self):
        return self.flight_num

class BoardingPass(Ticket):
    def __init__(self, passenger_id, passenger_name, passenger_email, ticket_num, flight_num,
                 seat_num, departure_gate, departure_time, departure_city):
        super().__init__(passenger_id, passenger_name, passenger_email, ticket_num, flight_num)
        self.seat_num = seat_num
        self.departure_gate = departure_gate
        self.departure_time = departure_time
        self.departure_city = departure_city

    def __str__(self):
        return f"Boarding Pass for {self.passenger_name}:, Flight Number: {self.flight_num},Seat Number: {self.seat_num}, Departure Gate: {self.departure_gate}, Departure Time: {self.departure_time},Departure City: {self.departure_city}"

    def print_BoardingPass(self):
        print(self)


class Flight(BoardingPass):
    def __init__(self, passenger_id, passenger_name, passenger_email, ticket_num,
                 flight_num, seat_num, departure_gate, departure_time, departure_city, arrival_city, arrival_time):
        super().__init__(passenger_id, passenger_name, passenger_email, ticket_num,
                         flight_num, seat_num, departure_gate, departure_time, departure_city)
        self.arrival_city = arrival_city  # New York
        self.arrival_time = arrival_time  # 13:30

    def get_arrival_city(self):
        return self.arrival_city

    def get_departure_city(self):
        return self.departure_city

    def get_arrival_time(self):
        return self.arrival_time

    def check_flight_status(self):
        pass


    def __str__(self):
        return f"Arrival City: {self.arrival_city},Arrival Time: {self.arrival_time}"

    # Example:


boarding_pass = BoardingPass(
    passenger_id=123,
    passenger_name="James Smith",
    passenger_email="james@example.com",
    ticket_num="5A6BCD78",
    flight_num="NA4321",
    seat_num="09A",
    departure_gate="03",
    departure_time="11:40",
    departure_city="Chicago ORD"
)
flight_instance = Flight(
    passenger_id=123,
    passenger_name="James Smith",
    passenger_email="james@example.com",
    ticket_num="5A6BCD78",
    flight_num="NA4321",
    seat_num="09A",
    departure_gate="03",
    departure_time="11:40",
    departure_city="Chicago ORD",
    arrival_city="New York",
    arrival_time="13:30"
)
boarding_pass.print_BoardingPass()

print("Flight Arrival City:", flight_instance.get_arrival_city())
print("Flight Arrival Time:", flight_instance.get_arrival_time())

