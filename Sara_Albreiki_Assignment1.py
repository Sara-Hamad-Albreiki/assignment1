class Person:
    def __init__(self, person_phone_num, person_gender):
        self.person_phone_num = person_phone_num
        self.person_gender = person_gender

    def get_phone_num(self):
        return self.person_phone_num

    def get_person_gender(self):
        return self.person_gender

    def display_person_gender(self):
        print(f"Passenger Phone Number: {self.person_phone_num}, Passenger Gender: {self.person_gender}")


class Passenger(Person):
    def __init__(self, person_phone_num, person_gender, passenger_id, passenger_name, passenger_email):
        super().__init__(person_phone_num, person_gender)
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

    def display_passenger(self):
        print(f'Passenger ID: {self.passenger_id}, Passenger Name: {self.passenger_name}, '
              f'Passenger Email: {self.passenger_email}, Passenger Phone Number: {self.person_phone_num}, '
              f'Passenger Gender: {self.person_gender}')


class BoardingPass:
    def __init__(self, boarding_time, departure_time, departure_city, seat_num, departure_gate):
        self.boarding_time = boarding_time
        self.departure_time = departure_time
        self.departure_city = departure_city
        self.seat_num = seat_num
        self.departure_gate = departure_gate

    def get_boarding_time(self):
        return self.boarding_time

    def get_departure_time(self):
        return self.departure_time

    def get_departure_city(self):
        return self.departure_city

    def get_seat_num(self):
        return self.seat_num

    def get_departure_gate(self):
        return self.departure_gate

    def __str__(self):
        return (f'Departure Time: {self.departure_time}, Departure City: {self.departure_city}, '
                f'Seat Number: {self.seat_num}, Departure Gate: {self.departure_gate}, '
                f'Boarding Time: {self.boarding_time}')

    def print_boarding_pass(self):
        print(self)


class Flight:
    def __init__(self, ticket_num, flight_num, arrival_city, arrival_time, flight_terminal):
        self.ticket_num = ticket_num
        self.flight_num = flight_num
        self.arrival_city = arrival_city
        self.arrival_time = arrival_time
        self.flight_terminal = flight_terminal

    def get_ticket_num(self):
        return self.ticket_num

    def display_ticket_num(self):
        return self.ticket_num

    def get_flight_num(self):
        return self.flight_num

    def display_flight_num(self):
        return self.flight_num

    def get_arrival_city(self):
        return self.arrival_city

    def get_arrival_time(self):
        return self.arrival_time

    def get_flight_terminal(self):
        return self.flight_terminal

    #Check the flight status if 
    def check_flight_status(self):
        pass

    def __str__(self):
        return (f"Ticket Number: {self.ticket_num}, Flight Number: {self.flight_num}, "
                f"Arrival City: {self.arrival_city}, Arrival Time: {self.arrival_time}, "
                f"Flight Terminal: {self.flight_terminal}")


person = Person(
    person_phone_num=51234567,
    person_gender="Male"
)

passenger = Passenger(
    person_phone_num=51234567,  # Provide the person's phone number
    person_gender="Male",       # Provide the person's gender
    passenger_id=123,
    passenger_name="James Smith",
    passenger_email="james@example.com"
)
boarding_pass = BoardingPass(
    seat_num="09A",
    departure_gate=3,
    boarding_time="11:20",
    departure_time="11:40",
    departure_city="Chicago ORD"
)
flight = Flight(
    ticket_num="5A6BCD78",
    flight_num="NA4321",
    arrival_city="New York",
    arrival_time="13:30",
    flight_terminal=2
)

person.display_person_gender()
passenger.display_passenger()
boarding_pass.print_boarding_pass()

print("Flight Arrival City:", flight.get_arrival_city())
print("Flight Arrival Time:", flight.get_arrival_time())
