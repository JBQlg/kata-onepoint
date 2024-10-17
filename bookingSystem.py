from booking_system.flight_handler import Flight_handler
from booking_system.plane_handler import Plane_handler
from booking_system.reservation_handler import Reservation_handler  
import argparse
import json 

class BookingSystem: 
    """This class is the main class of the booking system. 
    It will handle the main menu and the different handlers.
    Each handler will handle the different actions of the system.
    This class make the interactions with the user and make the link between the different handlers.
    """
    DATA_FILE = "booking_data.json"
    def __init__(self):
        # create the different handlers
        self.flight_handler = Flight_handler()
        self.plane_handler = Plane_handler()
        self.reservation_handler = Reservation_handler()
        self.load_data()
    
    def display_menu(self):
        # display the main menu and return the choice of the user
        print("\n Menu Principal :")
        print("1. Faire une réservation")
        print("2. Afficher les vols")
        print("3. Modifier une réservation")
        print("4. Afficher les détails d'une réservation")
        print("5. Quitter")
        print("-------------------------")
        print("Fonctionnalités supplémentaires :\n")
        print("6. Créer un avion")
        print("7. Créer un vol")
        print("8. Affichage des avions enregistrés")
        print("9. Supprimer un avion")
        print("10. Supprimer un vol")
        choix = input("Veuillez entrer votre choix : ")
        #check if the choice is valid
        while choix not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            print("Choix invalide")
            choix = input("Veuillez entrer votre choix : ")
        return choix
    
    def modification_menu(self):
        # display the modification menu and return the choice of the user
        print("\n Que voulez-vous modifier ?")
        print("1. Modifier le passager")
        print("2. Modifier le siège")
        print("3. Annuler la réservation")
        print("4. Retour")
        choix = input("Veuillez entrer votre choix : ")
        #check if the choice is valid
        while choix not in ["1", "2", "3", "4"]:
            print("Choix invalide")
            choix = input("Veuillez entrer votre choix : ")
        return choix
    
    def main_menu_handler(self):
        # dispatch the user choice to the right handler or the correcti function
        while True:
            choix = self.display_menu()
            if choix == "1":
                # create a reservation
                self.flight_handler.flights = self.reservation_handler.create_reservation(self.flight_handler.flights, self.plane_handler.planes)
            elif choix == "2":
                print(self.flight_handler)
            elif choix == "3":
                self.flight_handler.flights = self.reservation_handler.modify_reservation(self.modification_menu(), self.flight_handler.flights, self.plane_handler.planes)
            elif choix == "4":
                self.reservation_handler.print_reservation_details(self.flight_handler.flights)
            elif choix == "5":
                self.save_data()
                break
            elif choix == "6":
                self.plane_handler.create_plane(input("Modèle de l'avion : "), int(input("Nombre de rangées : ")), int(input("Nombre de colonnes : ")))
            elif choix == "7":
                print("Voici la liste des avions disponibles : ")
                print(self.plane_handler)
                plane = self.plane_handler.get_plane(input("ID de l'avion : "))
                self.flight_handler.create_flight(plane_id=plane.id, departure=input("Départ : "), destination=input("Destination : "), schedule=input("Horaire : "), date=input("Date : "), reservations=[])
            elif choix == "8":
                print(self.plane_handler)
            elif choix == "9":
                self.plane_handler.delete_plane(input("ID de l'avion à supprimer : "))
            elif choix == "10":
                self.flight_handler.delete_flight(input("ID du vol à supprimer : "))
            else:
                print("Choix invalide")

    #  Simulation item method 
    def items_simulation(self):
        """This function create some items to simulate the system
        """
        # create some planes
        self.plane_handler.create_plane("Airbus A320", 10, 6)   
        self.plane_handler.create_plane("Boeing 747", 5, 4)
        self.plane_handler.create_plane("Airbus A380", 6, 5)
        self.plane_handler.create_plane("Boeing 787", 7, 6)
    
        #create some flights with those planes
        self.flight_handler.create_flight(plane_id=self.plane_handler.planes[0].id, departure="Paris", destination="New York", schedule="12:00", date="2021-07-01", reservations=[])
        self.flight_handler.create_flight(plane_id=self.plane_handler.planes[1].id, departure="Paris", destination="London", schedule="12:00", date="2021-07-02", reservations=[])
        self.flight_handler.create_flight(plane_id=self.plane_handler.planes[1].id, departure="Paris", destination="Madeira", schedule="8:00", date="2021-07-02", reservations=[])
        self.flight_handler.create_flight(plane_id=self.plane_handler.planes[2].id, departure="Paris", destination="Tokyo", schedule="15:00", date="2021-07-03", reservations=[])
        self.flight_handler.create_flight(plane_id=self.plane_handler.planes[3].id, departure="Paris", destination="Los Angeles", schedule="10:00", date="2021-07-04", reservations=[])
        
        # create some reservations
        # passenger1 = self.reservation_handler.build_passenger("123456789", "John", "Doe", 34)
        # passenger2 = self.reservation_handler.build_passenger("987654321", "Jane", "Doe", 32)
        # flight = self.reservation_handler.assign_seat(flight=self.flight_handler.flights[0], passenger=passenger1, seat="C5", list_planes=self.plane_handler.planes)    
        # flight = self.reservation_handler.assign_seat(flight=self.flight_handler.flights[0], passenger=passenger2, seat="D5", list_planes=self.plane_handler.planes)    
            
    # JSON serialization methods 
    def save_data(self):
        """Save all the data into a JSON file."""
        # create data dictionary
        data = {
            "planes": [plane.to_dict() for plane in self.plane_handler.planes],
            "flights": [flight.to_dict() for flight in self.flight_handler.flights],
        }
        with open(self.DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print("Données sauvegardées avec succès.")
            
    def load_data(self):
        """Load system data from the JSON file."""
        try:
            with open(self.DATA_FILE, 'r') as f:
                data = json.load(f)
            
            # Charger les avions
            self.plane_handler = Plane_handler.from_dict(data["planes"])
            
            # Charger les vols
            self.flight_handler = Flight_handler.from_dict(data["flights"])
            
            print("Données chargées avec succès.")
        except FileNotFoundError:
            print("Fichier de données non trouvé.")
        except json.JSONDecodeError as e:
             print(f"Erreur de décodage JSON: {e}")

    # Direct command line handler
    def run(self, args):
        """This method handle the direct command line system and make corresponding call with the right handler."""
        command_executed = False  # token to check if a cmd is executed successfully
        if args.command == "reserve":
            # we keep this contextual menu, because  we need to knwow available seats in flihgts
            self.flight_handler.flights = self.reservation_handler.create_reservation(self.flight_handler.flights, self.plane_handler.planes)
            command_executed = True
            
        elif args.command == "list-flights":
            print(self.flight_handler)
            command_executed = True
            
        elif args.command == "list-planes":
            print(self.plane_handler)
            command_executed = True
            
            # modify reservation, as create reservation we keep this contextual menu
        elif args.command == "modify-reservation":
            self.flight_handler.flights = self.reservation_handler.modify_reservation(args.subcommand, self.flight_handler.flights, self.plane_handler.planes)
            command_executed = True
            
        elif args.command == "details":
            self.reservation_handler.print_reservation_details(self.flight_handler.flights, args.reservation_id)
            command_executed = True
            
        elif args.command == "add-plane":
            self.plane_handler.create_plane(args.model, args.rows, args.columns)
            print(f"Avion ajouté : Modèle {args.model}, {args.rows} rangées, {args.columns} colonnes.")
            command_executed = True
            
        elif args.command == "delete-plane":
            self.plane_handler.delete_plane(args.plane_id)
            print(f"Avion avec ID {args.plane_id} supprimé.")
            command_executed = True
            
        elif args.command == "add-flight":
            # check if the plane exists
            plane = self.plane_handler.get_plane(args.plane_id) 
            if plane:
                self.flight_handler.create_flight(plane_id=plane.id, departure=args.departure, destination=args.destination, schedule=args.schedule, date=args.date, reservations=[])
                print(f"Vol ajouté de {args.departure} à {args.destination} à {args.schedule} le {args.date}")
                command_executed = True
            else:
                print(f"L'avion avec ID {args.plane_id} n'a pas été trouvé.")
                
        elif args.command == "delete-flight":
            self.flight_handler.delete_flight(args.flight_id)
            print(f"Vol avec ID {args.flight_id} supprimé.")
            command_executed = True
            
        elif args.command == "help":
            self.show_help()
            command_executed = True
        else:
            self.main_menu_handler()

        # if a command is executed, save the data
        if command_executed:
            self.save_data()
    
    def show_help(self):
        """Display the list of available commands and their usage."""
        print("\nListe des commandes disponibles :")
        print("  reserve             : Créer une nouvelle réservation.")
        print("  list-flights        : Lister tous les vols disponibles.")
        print("  list-planes         : Lister tous les avions disponibles.")
        print("  modify-reservation  : Modifier une réservation existante. Utiliser avec un sous-argument [1, 2, 3] pour spécifier ce que vous voulez modifier.")
        print("                        - 1 = passager")
        print("                        - 2 = siège")
        print("                        - 3 = annuler la réservation")
        print("  details             : Voir les détails d'une réservation.")
        print("  add-plane           : Ajouter un nouvel avion. Utiliser avec les arguments suivants : modèle, rangées, colonnes.")
        print("  delete-plane        : Supprimer un avion. Utiliser avec l'argument suivant : plane_id.")
        print("  add-flight          : Ajouter un nouveau vol. Utiliser avec les arguments suivants : plane_id, départ, destination, horaire, date.")
        print("  delete-flight       : Supprimer un vol. Utiliser avec l'argument suivant : flight_id.")
        print("  help                : Afficher cette aide.")



# main method to run the system
def main():
    
    # handle direct command line system
    parser = argparse.ArgumentParser(description="Booking System Command Line Interface")
    subparsers = parser.add_subparsers(dest="command")
    # add subcommands to make user choices
    subparsers.add_parser("reserve", help="Create a new reservation")
    subparsers.add_parser("list-flights", help="List all available flights")
    modify_parser = subparsers.add_parser("modify-reservation", help="Modify an existing reservation")
    modify_parser.add_argument("subcommand", choices=["1", "2", "3"], help="What to modify: 1 = passenger, 2 = seat, 3 = cancel reservation")
    details_parser = subparsers.add_parser("details", help="View reservation details")
    details_parser.add_argument("reservation_id", type=str, help="The ID of the reservation to view")
    # subparsers.add_parser("quit", help="Save data and quit the system")
    #new plane
    add_plane_parser = subparsers.add_parser("add-plane", help="Add a new plane")
    add_plane_parser.add_argument("model", type=str, help="The model of the plane")
    add_plane_parser.add_argument("rows", type=int, help="The number of rows in the plane")
    add_plane_parser.add_argument("columns", type=int, help="The number of columns in the plane")
    # delete plane
    delete_plane_parser = subparsers.add_parser("delete-plane", help="Delete a plane")
    delete_plane_parser.add_argument("plane_id", type=str, help="The ID of the plane to delete")
    #new flight
    add_flight_parser = subparsers.add_parser("add-flight", help="Add a new flight")
    add_flight_parser.add_argument("plane_id", type=str, help="The ID of the plane for this flight")
    add_flight_parser.add_argument("departure", type=str, help="The departure city")
    add_flight_parser.add_argument("destination", type=str, help="The destination city")
    add_flight_parser.add_argument("schedule", type=str, help="The time of departure")
    add_flight_parser.add_argument("date", type=str, help="The date of the flight (format YYYY-MM-DD)")
    # delete flight
    delete_flight_parser = subparsers.add_parser("delete-flight", help="Delete a flight")
    delete_flight_parser.add_argument("flight_id", type=str, help="The ID of the flight to delete")
    # list planes
    subparsers.add_parser("list-planes", help="List all available planes")
    # help 
    subparsers.add_parser("help", help="Show help documentation")
    args = parser.parse_args()

    # Create the system and run it based on the arguments
    system = BookingSystem()
    system.run(args)

    
if __name__ == "__main__":
    main()
    # booking = BookingSystem()
    
    # # simulation des items pour tester le système
    # print("Simulation des items : " )
    # #booking.items_simulation()

    # # lancement du menu principal
    # booking.main_menu_handler()
    
    print("Au revoir !")
    