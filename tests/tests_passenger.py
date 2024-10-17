import unittest
from booking_system.passenger import Passenger

class TestPassenger(unittest.TestCase):
    
    def setUp(self):
        self.passenger = Passenger(passport_number="A12345678", firstname="John", lastname="Doe", age=30)

    def test_initialization(self):
        """Test passenger init normal case"""
        self.assertEqual(self.passenger.passport_number, "A12345678")
        self.assertEqual(self.passenger.firstname, "John")
        self.assertEqual(self.passenger.lastname, "Doe")
        self.assertEqual(self.passenger.age, 30)
        self.assertEqual(self.passenger.flights, [])

    def test_book_flight(self):
        """Test association flight to passenger"""
        self.passenger.book_flight("FL123")
        self.assertIn("FL123", self.passenger.flights)
        self.assertEqual(len(self.passenger.flights), 1)

        self.passenger.book_flight("FL456")
        self.assertIn("FL456", self.passenger.flights)
        self.assertEqual(len(self.passenger.flights), 2)

    def test_get_flights(self):
        """check passenger's booking list flight."""
        self.passenger.book_flight("FL123")
        self.passenger.book_flight("FL456")
        flights = self.passenger.get_flights()
        
        self.assertEqual(flights, ["FL123", "FL456"])
        self.assertEqual(len(flights), 2)
        
    def test_invalid_passport_number(self):
        """Test with invalid passport number."""
        with self.assertRaises(ValueError):
            Passenger(passport_number="", firstname="John", lastname="Doe", age=30)

    def test_invalid_age(self):
        """Test with an invalid age"""
        with self.assertRaises(ValueError):  # Assuming you raise ValueError for invalid age
            Passenger(passport_number="A12345678", firstname="John", lastname="Doe", age=-5)
    
    def test_duplicate_flight_booking(self):
        """Test booking the same flight multiple times."""
        self.passenger.book_flight("FL123")
        with self.assertRaises(ValueError):
            self.passenger.book_flight("FL123")
        self.assertEqual(self.passenger.flights.count("FL123"), 1)
    
    def test_str_representation(self):
        """Test the str method of the Passenger."""
        self.assertEqual(str(self.passenger), "John Doe (30) - A12345678")
