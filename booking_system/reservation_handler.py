from booking_system.reservation import Reservation
from booking_system.passenger import Passenger
from booking_system.seat import Seat
import booking_system.utils as  ut
class Reservation_handler:
    """This class allow ton manage all the reservations options. 
    It's including the creation, the modification and the cancellation of a reservation.
    And also the display of the reservation details.
    """
    
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
            return flights_list
        # get the passenger
        print("If the reservation is for several passengers please select the number of passengers  \n")
        nb_passengers = input("Else press 'enter' : ")
        # check if the number of passengers is a number or empty
        if nb_passengers.isdigit() == False and nb_passengers != "":
            raise("Invalid number of passengers, reservation not created")
        #get plane 
        if nb_passengers == "":
            nb_passengers = 1
        for p in planes_list:
            if p.id == f.plane_id:
                plane = p
                if int(nb_passengers) > plane.row_nb * plane.col_nb:
                    raise("The number of passengers is too high")
            
        passengers = []
        seat =[]
        for i in range(int(nb_passengers)):
            print(f"Passenger {i+1}")
            passengers.append(self.create_passenger())
            # get the seat
            # display the seats
            print("Display of available seats : ")
            f.display_plane_plan(planes_list)
            seat.append(self.fill_seat(f))

        # confirm the reservation
        reservation = Reservation(f.id, passengers, seat)
        print(reservation)
        reservation.confirm()
        if reservation.statut == "CONFIRMED":
            f.reservations.append(reservation)
            for p in passengers:
                p.book_flight(f.id)
        return flights_list
        
    def add_reservation(self, passenger, seat, flight):
        """This method allows to add a reservation to a flight.
        It returns the reservation created.
        """
        reservation = Reservation(flight.id, passenger, seat)
        reservation.confirm()
        flight.reservations.append(reservation)
        return flight
    
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
    
    def build_passenger(self, passport_number, firstname, lastname, age):
        """This method allows to create a passenger to add to a reservation.
        It returns the passenger created.
        """
        passenger = Passenger(passport_number, firstname, lastname, age)
        return passenger
    
    def assign_seat(self, flight, passenger, seat, list_planes):
        """This method allows to assign a seat to a reservation.
        It returns the seat created.
        """
        # check if the seat is in the right format
        if len(seat) != 2:
            raise ValueError("The seat must be in the format A1")
        col, row,  =ut.coordinates_converter(seat)
        seat = Seat(col, row)
        # check if the seat is available
        if flight.is_seat_available(seat) == True :
            #check if the seat is in the plane
            row, col = ut.coordinates_converter(seat)
            if row > list_planes[flight.plane_id].row_nb or col > list_planes[flight.plane_id].col_nb:
                raise ValueError("The seat is not in the plane")
        else:
            raise ValueError("The seat is not available")
    
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
                for passenger in resa.passengers:
                    if passenger.passport_number == passport_number:
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
        """This method allows modifying an existing reservation.
        The method first identifies the reservation either by the reservation ID or by 
        the passenger's passport number. Once the reservation is found, the method offers
        several options: modifying the passenger details, changing the seat, or canceling 
        the reservation. If there are multiple passengers, the user can choose which passenger 
        to modify.
        Args:
            choice_modif (str): The user's choice of modification (1: modify passenger, 2: modify seat, 3: cancel reservation).
            flights_list (list): A list of all flights available.
            planes_list (list): A list of all planes.
        Raises:
            ValueError: If the user input is invalid or if the reservation or passenger cannot be found.
        """
        print("\n ------------------")
        print("Modify reservation")
        
        choice = input("Do you have the reservation ID? (y/n): ").strip().lower()

        # Check input (only 'y' or 'n' is allowed)
        while choice not in ["y", "n"]:
            print("Invalid choice. Please enter 'y' or 'n'.")
            choice = input("Do you have the reservation ID? (y/n): ").strip().lower()

        # look for reservation by ID or by passport number
        if choice == "y":
            id_reservation = input("Enter the reservation ID: ").strip()
            resa = self.get_reservation_by_id_resa(flights_list, id_reservation)
            if not resa:
                raise ValueError(f"Reservation with ID {id_reservation} not found.")
        else:
            passport_number = input("Enter the passenger's passport number: ").strip()
            # check passport number format
            if not ut.is_passport_number_valid(passport_number):
                raise ValueError("Invalid passport number format.")
            
            resa = self.get_reservations_by_passport(flights_list, passport_number)
            if not resa:
                raise ValueError(f"No reservation found for passport number {passport_number}.")
            else:
                print(f"Reservation found: {resa}")

        # We have the reservation instance, now we can proceed with the modification
    
        # Select the passenger if there are multiple passengers in the reservation
        if len(resa.passengers) > 1:
            print("There are multiple passengers in this reservation.")
            id_p = input("Enter the passenger's passport number to modify: ").strip()
            
            # Find the selected passenger
            for p in resa.passengers:
                if p.passport_number == id_p:
                    selected_passenger = p
                    break
            else:
                # If no match, assume first passenger
                selected_passenger = resa.passengers[0]
                print(f"Passenger not found. Modifying the first passenger: {selected_passenger}")
        else:
            selected_passenger = resa.passengers[0]  # Only one passenger, select by default

        # Perform the modification based on the reservation and passenger
        match choice_modif:
            case "1":  #Modify passenger
                resa = self.modify_reservation_passenger(resa, selected_passenger.passport_number)
            case "2":  # Modify the seat for the reservation
                # Find the flight instance
                flight = next((f for f in flights_list if f.id == resa.flight_id), None)
                if not flight:
                    raise ValueError(f"Flight with ID {resa.flight_id} not found.")
                resa = self.modify_reservation_seat(flight=flight, resa=resa, planes_list=planes_list)
            case "3":  # Cancel the reservation
                resa = self.concel_reservation(resa)
            case "4":  # Exit without modifying
                print("Exiting without modifications.")
                return flights_list
            case _:  # Handle invalid input for modification choice
                raise ValueError("Invalid modification choice.")
        
        # Update the reservation in the flight's reservation list
        for flight in flights_list:
            if flight.id == resa.flight_id:
                for i, r in enumerate(flight.reservations):
                    if r.id == resa.id:
                        flight.reservations[i] = resa  # Update the modified reservation
                        break

        return flights_list  # Return the updated flight list
    
    def modify_reservation_passenger(self, resa, passport_number):
        """ This method allows to modify a passenger in a reservation.
        
        Args: flight (Flight): the flight where the reservation is made
        
        resa (Reservation): the reservation to modify
        
        passport_number (str): the unique passport number of the passenger to modify
        Returns: resa (Reservation): the updated reservation to push in the flight
        """
        print("Modify the passenger")
        
        # refind the passenger in the reservation to modify
        for i, passenger in enumerate(resa.passengers):
            if passenger.passport_number == passport_number:
                break
        if passenger == None:
            raise ValueError("Passenger not found")
        print(f"Passenger : {passenger}")
        
        choice = input("Are you sure to modify this passenger ? (y/n) \n")
        # check if the choice is valid
        while choice not in ["y", "n"]:
            print("Invalid choice")
            choice = input("Are you sure to modify this passenger ? (y/n) \n")
            
        if choice == "y":
            # get the new passenger
            new_passenger = self.create_passenger()
            # modify the passenger
            # passenger = new_passenger
            resa.passengers[i] = new_passenger
            print("Passenger modified")
            return resa
        else:
            print("Passenger not modified")
            return
    
    def modify_reservation_seat(self,flight, resa, planes_list):
        """This method allows to modify the seat of a reservation.

        Args:
            flight (Flight): flight concered by the reservation
            resa (Reservation): reservation to modify
            planes_list ([Plane]): plane_list to check the seat plan
        Return : resa (Reservation): the updated reservation 
        """
        print("Modify seats for passengers")
    
        for i, passenger in enumerate(resa.passengers):
            current_seat = resa.seats[i]
            print(f"Passenger: {passenger}, Current seat: {ut.reverse_coordinates_converter(current_seat.col, current_seat.row)}")
            
            choice = input(f"Do you want to modify the seat for {passenger.firstname} {passenger.lastname}? (y/n) ").strip().lower()
            
            # Validate input
            while choice not in ["y", "n"]:
                print("Invalid choice")
                choice = input(f"Do you want to modify the seat for {passenger.firstname} {passenger.lastname}? (y/n) ").strip().lower()
            
            if choice == "y":
                # Display available seats
                print("Display of available seats:")
                flight.display_plane_plan(planes_list)
                # Get new seat
                new_seat = self.fill_seat(flight)
                # Update the seat for this passenger
                resa.seats[i] = new_seat
                resa.confirm()
                print(f"Seat modified for {passenger.firstname} {passenger.lastname}")
            else:
                print(f"Seat not modified for {passenger.firstname} {passenger.lastname}")
        
        return resa 
    
    def concel_reservation(self, resa):
        """This method allows to cancel a seat or a complete reservation.

        Args:
            resa (Reservation): reservation to modify
            
        Returns:
            resa: the reservation is cancelled
        """
        # check if the choice is valid
        choice = input("Are you sure you want to cancel the reservation ? (y/n)\n")
        while choice not in ["y", "n"]:
            print("Invalid choice")
            choice = input("Are you sure you want to cancel the reservation ? (y/n)\n")
        if choice == "y":
            resa.cancel()
            print( "Reservation cancelled")
        else :
            print("Reservation not cancelled")
        return resa        
    
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
