
class Seat:
    def __init__(self, row, col,category = "ECONONY", is_booked = False):
        self.row = row
        self.col = col
        self.category = category
        self.is_booked = is_booked
        
    def __str__(self):
        return f"{self.row}{self.col} ({self.category}) - {'BOOKED' if self.is_booked else 'AVAILABLE'}"