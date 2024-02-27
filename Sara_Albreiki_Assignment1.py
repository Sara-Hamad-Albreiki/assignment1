#A Person class is used to handle information related to an individual such as his or her name, gender, and phone number
class Person:
    def __init__(self, person_phone_num, person_gender):
        #Initialize the person's phone number and gender
        self.person_phone_num = person_phone_num
        self.person_gender = person_gender
        
    #Call the person and retrieve their phone number
    def get_phone_num(self):
        return self.person_phone_num

    def set_phone_num(self):
        self.person_phone_num= person_phone_num
        
    #Call the person and retrieve their gender
    def get_person_gender(self):
        return self.person_gender
        
    # Display the person's gender along with the phone number
    def display_person_gender(self):
        print(f"Passenger Phone Number: {self.person_phone_num}, Passenger Gender: {self.person_gender}")

#Create a class Passenger that inherits Person and contains additional information about passengers
    class Passenger(Person):
    def __init__(self, person_phone_num, person_gender, passenger_id, passenger_name, passenger_email):
        super().__init__(person_phone_num, person_gender)
        # passenger_name(str): name of the passenger
        # passenger_id(int): the ID for the passenger
        # passenger_email(str): email address of teh passenger
        self.passenger_name = passenger_name
        self.passenger_id = passenger_id
        self.passenger_email = passenger_email


    #Use the get function to retrieve the passenger's name
    def get_passenger_name(self):
        return self.passenger_name
        
    #Use the get function to retrieve the passenger's ID
    def get_passenger_id(self):
        return self.passenger_id

    #Use the get function to retrieve the passenger's email
    def get_passenger_email(self):
        return self.passenger_email
        
    #Use the set function to allow the passenger to set or update the passenger's email
    def set_passenger_email(self, new_email):
        self.passenger_email = new_email

    #Display passenger's details including ID, name, email, phone number, and gender
    def display_passenger(self):
        print(f'Passenger ID: {self.passenger_id}, Passenger Name: {self.passenger_name}, '
              f'Passenger Email: {self.passenger_email}, Passenger Phone Number: {self.person_phone_num}, '
              f'Passenger Gender: {self.person_gender}')

# Define the BoardingPass class to hold boarding pass details
class BoardingPass:
    def __init__(self, boarding_time, departure_time, departure_city, seat_num, departure_gate):
        #Initialize boarding pass details
        self.boarding_time = boarding_time
        self.departure_time = departure_time
        self.departure_city = departure_city
        self.seat_num = seat_num
        self.departure_gate = departure_gate

    #Use the get function to retrieve boarding time
    def get_boarding_time(self):
        return self.boarding_time
        
    #Use the get function to Retrieve the departure time
    def get_departure_time(self):
        return self.departure_time
        
    #Use the get function to retrieve the departure city
    def get_departure_city(self):
        return self.departure_city
        
    #Use the get function to retrieve the seat number
    def get_seat_num(self):
        return self.seat_num
        
    #Use the get function to retrieve the departure gate
    def get_departure_gate(self):
        return self.departure_gate
        
    #Generate string expression of the boarding pass
    def __str__(self):
        return (f'Departure Time: {self.departure_time}, Departure City: {self.departure_city}, '
                f'Seat Number: {self.seat_num}, Departure Gate: {self.departure_gate}, '
                f'Boarding Time: {self.boarding_time}')

    #Print the boarding pass details
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

    #Use the get function to retrieve ticket number
    def get_ticket_num(self):
        return self.ticket_num

    #Use the get function to retrieve flight number
    def get_flight_num(self):
        return self.flight_num
        
    #Use the get function to retrieve the arrival city
    def get_arrival_city(self):
        return self.arrival_city
        
    #Use the get function to retrieve the arrival time
    def get_arrival_time(self):
        return self.arrival_time

    #Use the get function to retrieve the flight terminal
    def get_flight_terminal(self):
        return self.flight_terminal

    #Check the flight status if all the above 
    def check_flight_status(self):
        #This function would involve querying external systems for flight information, 
        #checking if the flight time is on time, delayed, or canceled, and updating flight status accordingly.
        pass

    #Generate string expression of the flight details
    def __str__(self):
        return (f"Ticket Number: {self.ticket_num}, Flight Number: {self.flight_num}, "
                f"Arrival City: {self.arrival_city}, Arrival Time: {self.arrival_time}, "
                f"Flight Terminal: {self.flight_terminal}")

#Display boarding pass details by creating instances of the classes:
person1 = Person(
    person_phone_num=51234567,
    person_gender="Male"
)

passenger1 = Passenger(
    person_phone_num=51234567,  # Provide the person's phone number
    person_gender="Male",       # Provide the person's gender
    passenger_id=123,
    passenger_name="James Smith",
    passenger_email="james@example.com"
)
boarding_pass1 = BoardingPass(
    seat_num="09A",
    departure_gate=3,
    boarding_time="11:20",
    departure_time="11:40",
    departure_city="Chicago ORD"
)
flight1 = Flight(
    ticket_num="5A6BCD78",
    flight_num="NA4321",
    arrival_city="New York",
    arrival_time="13:30",
    flight_terminal=2
)
# Display the person's phone number and gender
person1.display_person_gender()

# Display passenger's details
passenger1.display_passenger()

# Print boarding pass details
boarding_pass1.print_boarding_pass()

#Retrieve and print the flight's ticket number, flight number, arrival city, time, and flight terminal
print("Ticket Number: ", flight1.get_ticket_num())
print("Flight Number:",flight1.get_flight_num() )
print("Flight Arrival City:", flight1.get_arrival_city())
print("Flight Arrival Time:", flight1.get_arrival_time())
print("Flight Terminal:", flight1.get_flight_terminal())
