class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False

    def available_seats(self):
        return self.total_seats - self.booked_seats


class BusSystem:
    def __init__(self):
        self.buses = {}
        self.passengers = []

    def book_ticket(self, bus_number, name, phone):
        bus = self.buses.get(bus_number)
        if bus:
            if bus.book_seat():
                self.passengers.append(Passenger(name, phone, bus))
                print("Ticket booked. Fare: ৳500\n")
            else:
                print("Seat not available.\n")
        else:
            print("Bus not found.\n")

    def add_bus(self, number, route, total_seats):
        if number in self.buses:
            print("Bus already exist.\n")
        else:
            self.buses[number] = Bus(number, route, total_seats)
            print("New bus added.\n")

    def show_buses(self):
        if not self.buses:
            print("No bus available.\n")
            return
        for bus in self.buses.values():
            print(f"Bus Number : {bus.number}")
            print(f"Bus Route : {bus.route}")
            print(f"Available Seats : {bus.available_seats()}\n")


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


class Admin:
    def __init__(self):
        self.__username = "admin"
        self.__password = "1234"

    def login(self, username, password):
        if username != self.__username:
            print("Invalid Username.\n")
            return False
        elif password != self.__password:
            print("Invalid Password\n")
            return False
        else:
            print("Successfully Logged In.\n")
            return True


def input_validation():
    try:
        option = int(input("Enter Number: "))
        return option
    except ValueError:
        print("Invalid input type, Please enter a number.\n")
        return None


a = Admin()
zaer = BusSystem()

while True:
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit\n")

    option = input_validation()

    if option == 1:
        username = input("Enter Username: ")
        password = input("Enter password: ")
        if a.login(username, password):
            while True:
                print("1. Add Bus")
                print("2. View All Buses")
                print("3. Logout\n")

                admin_option = input_validation()

                if admin_option == 1:
                    bus_number = input("Enter Bus Number: ")
                    route = input("Enter Bus Route: ")
                    total_seats = input_validation()
                    if total_seats is not None and total_seats > 0:
                        zaer.add_bus(bus_number, route, total_seats)
                    else:
                        print("Seat number must be a number and it can't be 0 or less.\n")
                elif admin_option == 2:
                    zaer.show_buses()

                elif admin_option == 3:
                    break
                elif admin_option is not None:
                    print("Invalid option.\n")

    elif option == 2:
        bus_num = input("Enter Bus Number: ")
        passenger_name = input("Enter your name: ")
        passenger_phone = input("Enter your phone: ")
        zaer.book_ticket(bus_num, passenger_name, passenger_phone)

    elif option == 3:
        zaer.show_buses()

    elif option == 4:
        break

    elif option is not None:
        print("Invalid option.\n")
