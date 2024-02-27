# A Person class is used to handle information related to an individual such as his or her name, gender, and phone number
class Person:
    def __init__(self, person_phone_num, person_gender):
        # Initialize the person's phone number and gender
        self.person_phone_num = person_phone_num
        self.person_gender = person_gender

    # Call the person and retrieve their phone number and gender
    def get_person_phone_num(self):
        return self.person_phone_num

    def get_person_gender(self):
        return self.person_gender

    # Use the set function to allow the passenger to set or update the person's phone number and gender
    def set_person_phone_num(self, person_phone_num):
        self.person_phone_num = person_phone_num

    def set_person_gender(self, person_gender):
        self.person_gender = person_gender

    # Display the person's gender along with the phone number
    def display_person(self):
        return f"Person Phone Number: {self.person_phone_num}, Person Gender: {self.person_gender}"

# Create a class Passenger that inherits Person and contains additional information about passengers
class Passenger(Person):
    def __init__(self, person_phone_num, person_gender, passenger_id, passenger_name, passenger_email):
        super().__init__(person_phone_num, person_gender)
        # passenger_name(str): name of the passenger
        # passenger_id(int): the ID for the passenger
        # passenger_email(str): email address of teh passenger
        self.passenger_name = passenger_name
        self.passenger_id = passenger_id
        self.passenger_email = passenger_email

    # Use the set function to allow the passenger to set or update the passenger's name, ID, and email.
    def set_passenger_name(self, passenger_name):
        self.passenger_name = passenger_name

    def set_passenger_id(self, passenger_id):
        self.passenger_id = passenger_id

    def set_passenger_email(self, passenger_email):
        self.passenger_email = passenger_email

    #Use the get function to retrieve the passenger's name, ID, and email.
    def get_passenger_name(self):
        return self.passenger_name

    def get_passenger_id(self):
        return self.passenger_id

    def get_passenger_email(self):
        return self.passenger_email

    # Display passenger's details including ID, name, email, phone number, and gender
    def display_passenger(self):
        return super().display_person() + f', Passenger Name: {self.passenger_name}, Passenger ID: {self.passenger_id}, Passenger Email: {self.passenger_email}'

# Define the BoardingPass class to hold boarding pass details
class BoardingPass:
    def __init__(self, boarding_time, departure_time, departure_city, seat_num, departure_gate):
        # Initialize boarding pass details boarding time, departure time, departure city, seat num, and departure gate
        self.boarding_time = boarding_time
        self.departure_time = departure_time
        self.departure_city = departure_city
        self.seat_num = seat_num
        self.departure_gate = departure_gate

    # Use the set function to allow the passenger to set or update the boarding time, departure time, departure city, seat num, departure gate
    def set_boarding_time(self, boarding_time):
        self.boarding_time = boarding_time

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def set_departure_city(self, departure_city):
        self.departure_city = departure_city

    def set_seat_num(self, seat_num):
        self.seat_num = seat_num

    def set_departure_gate(self, departure_gate):
        self.departure_gate = departure_gate

    #Use the get function to retrieve boarding time, departure time, departure city, seat num, departure gate
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

    #Display the boarding pass details the boarding time, departure time, departure city, seat num, and departure gate
    def display_boarding_pass(self):
        return (f'Departure Time: {self.departure_time}, Departure City: {self.departure_city}, '
                f'Seat Number: {self.seat_num}, Departure Gate: {self.departure_gate}, '
                f'Boarding Time: {self.boarding_time}')

    #Print the Boarding pass details
    def print_boarding_pass(self):
        print(self)

# Define the Flight class to drive the flight details
class Flight:
    def __init__(self, ticket_num, flight_num, arrival_city, arrival_time, flight_terminal):
        # Initialize flight details: ticket number, flight number, arrival city, arrival time, flight terminal
        self.ticket_num = ticket_num
        self.flight_num = flight_num
        self.arrival_city = arrival_city
        self.arrival_time = arrival_time
        self.flight_terminal = flight_terminal

    # Use the set function to allow the passenger to set or update the ticket number, flight number, arrival city, arrival time, flight terminal
    def set_ticket_num(self, ticket_num):
        self.ticket_num = ticket_num

    def set_flight_num(self, flight_num):
        self.flight_num = flight_num

    def set_arrival_city(self, arrival_city):
        self.arrival_city = arrival_city

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def set_flight_terminal(self, flight_terminal):
        self.flight_terminal = flight_terminal

    # Use the get function to retrieve ticket number, flight number, arrival city, arrival time, and flight terminal
    def get_ticket_num(self):
        return self.ticket_num

    def get_flight_num(self):
        return self.flight_num

    def get_arrival_city(self):
        return self.arrival_city

    def get_arrival_time(self):
        return self.arrival_time

    def get_flight_terminal(self):
        return self.flight_terminal

    # Check the flight status if needed
    def check_flight_status(self):
        # This function would involve querying external systems for flight information,
        # checking if the flight time is on time, delayed, or canceled, and updating flight status accordingly.
        pass

    #Display the Flight details ticket number, flight number, arrival city, arrival time, flight terminal
    def display_flight(self):
        return (f"Ticket Number: {self.ticket_num}, Flight Number: {self.flight_num}, "
                f"Arrival City: {self.arrival_city}, Arrival Time: {self.arrival_time}, "
                f"Flight Terminal: {self.flight_terminal}")


#Display boarding pass details by creating instances of the classes:

passenger = Passenger(
    person_phone_num=51234567,
    person_gender="Male",
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
# Display passenger's details
print(passenger.display_passenger())

# Print boarding pass details
print(boarding_pass.display_boarding_pass())

#Retrieve and print the flight's ticket number, flight number, arrival city, time, and flight terminal
print("Ticket Number: ", flight.get_ticket_num())
print("Flight Number:", flight.get_flight_num())
print("Flight Arrival City:", flight.get_arrival_city())
print("Flight Arrival Time:", flight.get_arrival_time())
print("Flight Terminal:", flight.get_flight_terminal())

