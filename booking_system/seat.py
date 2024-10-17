import booking_system.utils as ut
class Seat:
    def __init__(self, row, col,category = "ECONONY", is_booked = False):
        self.row = row
        self.col = col
        self.category = category
        self.is_booked = is_booked
        
    def __str__(self):
        return f"Seat : {ut.reverse_coordinates_converter(self.col,self.row)} ({self.category}) - {'BOOKED' if self.is_booked else 'AVAILABLE'}"

    def to_dict(self):
        """Convert Seat object to a dictionary for JSON serialization."""
        return {
            "row": self.row,
            "col": self.col,
            "category": self.category,
            "is_booked": self.is_booked
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Seat object from a dictionary (JSON deserialization)."""
        return cls(
            row=data["row"],
            col=data["col"],
            category=data.get("category", "ECONOMY"),
            is_booked=data["is_booked"]
        )
