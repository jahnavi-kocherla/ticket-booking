import random
from datetime import date

# Preloaded train data
all_trains = [
    {
        "train_no": 101,
        "train_name": "Chennai Express",
        "train_stations": ["Chennai","Arakkonam","Katpadi","Jolarpettai","Bangarapet","Bengaluru East","Bengaluru West"],
        "seats": {"sleeper":200, "3ac":100, "2ac":50, "1ac":20}
    },
    {
        "train_no": 102,
        "train_name": "Hyderabad Express",
        "train_stations": ["Hyderabad","Arakkonam","Mahabubnagar","Kurnool City","Dhonepudi","Vijayawada"],
        "seats": {"sleeper":200, "3ac":100, "2ac":50, "1ac":20}
    },
    {
        "train_no": 103,
        "train_name": "Guntur Express",
        "train_stations": ["Guntur","Vejandla","Sangam Jagarlamudi","Angalakuduru","Tenali","Vemuru","Repalle"],
        "seats": {"sleeper":200, "3ac":100, "2ac":50, "1ac":20}
    },
    {
        "train_no": 104,
        "train_name": "Delhi Express",
        "train_stations": ["Delhi","Agra","Jhansi","Nagpur","Bhopal","Vijayawada"],
        "seats": {"sleeper":200, "3ac":100, "2ac":50, "1ac":20}
    },
    {
        "train_no": 105,
        "train_name": "Karnataka Express",
        "train_stations": ["Delhi","Agra","Nagpur","Bhopal","Hyderabad","Vijayawada"],
        "seats": {"sleeper":200, "3ac":100, "2ac":50, "1ac":20}
    }
]

bookings = {}

# Function to generate booking ID
def generate_booking_id():
    return "BK" + str(random.randint(1000,9999))

# Function to list all trains
def list_trains():
    print("\nAvailable Trains:")
    for train in all_trains:
        print(f"Train No: {train['train_no']} | Name: {train['train_name']} | Stations: {', '.join(train['train_stations'])}")

# Function to check available seats
def check_seats(train_no):
    for train in all_trains:
        if train["train_no"] == train_no:
            print(f"\nAvailable seats for {train['train_name']}:")
            for cls, seats in train["seats"].items():
                print(f"{cls}: {seats}")
            return
    print("Train not found!")

# Function to book tickets
def create_booking(train_no, seat_type, no_of_seats, passenger_name):
    today = date.today()
    travel_date_str = input("Enter the travel date (YYYY-MM-DD): ")

    try:
        travel_date = date.fromisoformat(travel_date_str)
    except:
        return "Invalid date format"

    if travel_date < today or (travel_date - today).days > 7:
        return "Booking can only be done for today or within the next 7 days"

    for train in all_trains:
        if train["train_no"] == train_no:
            if train["seats"].get(seat_type, 0) >= no_of_seats:
                booking_id = generate_booking_id()
                train["seats"][seat_type] -= no_of_seats
                bookings[booking_id] = {
                    "train_no": train_no,
                    "train_name": train["train_name"],
                    "seat_class": seat_type,
                    "date": str(travel_date),
                    "passenger": passenger_name,
                    "no_of_seats": no_of_seats
                }
                return f"Ticket booked! Booking ID: {booking_id}"
            else:
                return f"Not enough seats available in {seat_type} class"

    return "Train not found"

# Function to cancel a ticket
def cancel_ticket(booking_id):
    if booking_id in bookings:
        booking = bookings.pop(booking_id)
        for train in all_trains:
            if train["train_no"] == booking["train_no"]:
                train["seats"][booking["seat_class"]] += booking["no_of_seats"]
        return f"Booking {booking_id} cancelled successfully!"
    else:
        return "Booking ID not found!"

# Function to list all bookings
def list_bookings():
    if not bookings:
        return "No bookings yet."
    result = "Current Bookings:\n"
    for bid, info in bookings.items():
        result += f"{bid} - {info['passenger']} | {info['train_name']} | {info['seat_class']} | {info['date']} | Seats: {info['no_of_seats']}\n"
    return result

# Menu-driven interface
def main_menu():
    while True:
        print("\n--- Railway Ticket Booking System ---")
        print("1. List Trains")
        print("2. Check Available Seats")
        print("3. Book Ticket")
        print("4. Cancel Ticket")
        print("5. View All Bookings")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_trains()
        elif choice == "2":
            train_no = int(input("Enter train number: "))
            check_seats(train_no)
        elif choice == "3":
            train_no = int(input("Enter train number: "))
            seat_type = input("Enter seat class (sleeper/3ac/2ac/1ac): ").lower()
            no_of_seats = int(input("Enter number of seats: "))
            passenger_name = input("Enter passenger name: ")
            print(create_booking(train_no, seat_type, no_of_seats, passenger_name))
        elif choice == "4":
            booking_id = input("Enter booking ID to cancel: ")
            print(cancel_ticket(booking_id))
        elif choice == "5":
            print(list_bookings())
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
main_menu()
