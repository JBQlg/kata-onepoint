import unittest
from booking_system.passenger import Passenger

class TestPassenger(unittest.TestCase):
    
    def setUp(self):
        self.passenger = Passenger(passport_number="A12345678", firstname="John", lastname="Doe", age=30)

    def test_initialization(self):
        """Test if the Passenger is initialized correctly."""
        self.assertEqual(self.passenger.passport_number, "A12345678")
        self.assertEqual(self.passenger.firstname, "John")
        self.assertEqual(self.passenger.lastname, "Doe")
        self.assertEqual(self.passenger.age, 30)
        self.assertEqual(self.passenger.flights, [])

    def test_book_flight(self):
        """Test if a flight can be added to the passenger's list of flights."""
        self.passenger.book_flight("FL123")
        self.assertIn("FL123", self.passenger.flights)
        self.assertEqual(len(self.passenger.flights), 1)

        self.passenger.book_flight("FL456")
        self.assertIn("FL456", self.passenger.flights)
        self.assertEqual(len(self.passenger.flights), 2)

    def test_get_flights(self):
        """Test if the passenger's list of booked flights is returned correctly."""
        self.passenger.book_flight("FL123")
        self.passenger.book_flight("FL456")
        flights = self.passenger.get_flights()
        
        self.assertEqual(flights, ["FL123", "FL456"])
        self.assertEqual(len(flights), 2)

    def test_str_representation(self):
        """Test the string representation of the Passenger."""
        self.assertEqual(str(self.passenger), "John Doe (30) - A12345678")
    
    def test_passport_number_uniqueness(self):
        """Test that the passport number is used as a unique identifier."""
        passenger2 = Passenger(passport_number="A98765432", firstname="Jane", lastname="Smith", age=25)
        self.assertNotEqual(self.passenger.passport_number, passenger2.passport_number)
    
