from booking_system.reservation import Reservation
from booking_system.passenger import Passenger
from booking_system.seat import Seat
import booking_system.utils as  ut
class Reservation_handler:
    
    def __init__(self):
        pass
    
    def create_reservation(self, flights_list, planes_list):
        """ This method allows to create a reservation for a flight.
        It take in argument the current list of flights and the list of planes used.
        And it returns the flights list with the flight updated with the new reservation.

        Args:
            flights_list ([Flight]): list of flights
            planes_list ([Plane]): list of plane used

        Returns:
            flight_list: the concerned flight is updated with the new reservation
        """
        print("Create reservation")
        # get the flight
        print("List of flights : ")
        for flight in flights_list:
            print(flight)
        input_flight = input("Enter the flight id : ")
        # check flight exist    
        for f in flights_list:
            if f.id == input_flight:
                break
        else:
            print("This flight does not exist")
            return
        # get the passenger
        passenger = self.create_passenger()
        # get the seat
        # display the seats
        print("Display of available seats : ")
        f.display_plane_plan(planes_list)
        seat = self.fill_seat(f)      
        # confirm the reservation
        reservation = Reservation(f.id, passenger, seat)
        print(reservation)
        reservation.confirm()
        if reservation.statut == "CONFIRMED":
            f.reservations.append(reservation)
            passenger.book_flight
        return flights_list
        
    def create_passenger(self):
        """This method allows to create a passenger to add to a reservation.
        It returns the passenger created.
        """
        passport_number = self.fill_passport_number()
        firstname = input("Enter the firstname : ")
        lastname = input("Enter the lastname : ")
        age = input("Enter the age : ")
        # check if the age is a number
        if not age.isdigit():
            print("The age must be a number")
            return self.create_passenger()
        passenger = Passenger(passport_number, firstname, lastname, age)
        return passenger
    
    def fill_seat(self, flight):
        """This method allows to create a seat for a reservation according to the flight's seats availability.

        Args:
            flight (flight): selected flight where the seat will be booked

        Returns:
            seat: the seat created
        """
        seat = input("Enter the new seat number (B6): ")
        # check if the seat is in the right format
        if len(seat) != 2:
            print("The seat must be in the format A1")
            return self.fill_seat()
        # check if the seat is available 
        row, col =ut.coordinates_converter(seat)
        seat = Seat(col, row)
        if flight.is_seat_available(seat) == True : 
            print("The seat is available")
            return seat 
        else:
            print("The seat is not available")
            return self.fill_seat(flight)
    
    def fill_passport_number(self):
        passport_number = input("Enter the passport number : ")
        # check if the passenger passport number last 9 characters
        if len(passport_number) != 9:
            print("The passport number must have 9 characters")
            return self.fill_passport_number()
        return passport_number
    
    def get_reservations_by_passport(self,flights_list, passport_number):
        for flight in flights_list:
            for resa in flight.reservations:
                if resa.passenger.passport_number == passport_number:
                    return resa
        print(f"Reservation for {passport_number} not found")
        return None
    
    def get_reservation_by_id_resa(self, flights_list, id_reservation):
        for flight in flights_list:
            for resa in flight.reservations:
                if resa.id == id_reservation:
                    return resa
        print(f"Reservation {id_reservation} not found")
        return None    
    
    def modify_reservation(self, choice_modif, flights_list, planes_list):
        """This method allow to redirect to the wanted king of modification.
        """
        print("\n ------------------")
        print("Modify reservation")
        print("We need to find the reservation to modify")
        choice = input("Do you have the reservation id ? (y/n)")
        # check if the choice is valid
        while choice not in ["y", "n"]:
            print("Invalid choice")
            choice = input("Enter your choice : ")
        if choice == "y":
            id_reservation = input("Enter the reservation id : \n")
            resa=self.get_reservation_by_id_resa(flights_list, id_reservation)
        elif choice == "n":
            passport_number = input("Enter the passport number : ")
            # check if the passport number is in the reservation
            if ut.is_passport_number_valid(passport_number) == False:
                print("Invalid passport number")
                return
            resa = self.get_reservations_by_passport(flights_list, passport_number)
            if resa == None:
                print("Reservation not found")
                return None
            else:
                print(resa)
        
        match choice_modif:
            case "1": # modify the passenger
                self.modify_reservation_passenger(resa)
            case "2":
                for f in flights_list:
                    if f.id == resa.flight_id:
                        break
                self.modify_reservation_seat(flight=f, resa=resa, planes_list=planes_list)
            case "3":
                self.concel_reservation(resa)
            case "4":
                return
    
    def modify_reservation_passenger(self, resa):
        print("Modify the passenger")
        print(resa.passenger)
        choice = input("Do you want to modify the passenger ? (y/n) \n")
        # check if the choice is valid
        while choice not in ["y", "n"]:
            print("Invalid choice")
            choice = input("Do you want to modify the passenger ? (y/n) \n")
        if choice == "y":
            # get the new passenger
            passenger = self.create_passenger()
            resa.passenger = passenger
            print("Passenger modified")
            return
        else:
            print("Passenger not modified")
            return
    
    def modify_reservation_seat(self,flight, resa, planes_list):
        print(f"Modify the seat : {ut.reverse_coordinates_converter(resa.seat.col +1, resa.seat.row+1)}")        
        choice = input("Do you want to modify the seat ? (y/n) \n")
        # check if the choice is valid
        while choice not in ["y", "n"]:
            print("Invalid choice")
            choice = input("Do you want to modify the seat ? (y/n) \n")
            
        # display the seats
        print("Display of available seats : ")
        print(flight.display_plane_plan(planes_list))
        if choice == "y":
            # get the new seat
            seat = self.fill_seat(flight)
            # free the old seat
            resa.seat = seat
            print("Seat modified")
            return
        else:
            print("Seat not modified")
            return
    
    def concel_reservation(self, resa):
        choice = input("Are you sure you want to cancel the reservation ? (y/n) \n")
        # check if the choice is valid
        while choice not in ["y", "n"]:
            print("Invalid choice")
            choice = input("Are you sure you want to cancel the reservation ? (y/n)\n")
        if choice == "y":
            resa.cancel()
            return
        else :
            print("Reservation not cancelled")
    
    def print_reservation_details(self, flights):
        print("Print reservation details")
        id_reservation = input("Enter the reservation id : ")
        #check if the reservation exist
        for f in flights:
            for resa in f.reservations:
                if resa.id == id_reservation:
                    print("Reservation details : ")
                    print(resa)
                    return
        print(f"Reservation {id_reservation} not found")
        return None
    