
class Plane : 
    _id_counter = 1
    def __init__(self, model, row_nb, col_nb) :
        if model == "" or row_nb <= 0 or col_nb <= 0:
            raise ValueError("All fields must be filled correctly")
        self.id = "P"+str(Plane._id_counter)
        Plane._id_counter += 1
        self.model = model
        self.row_nb = row_nb
        self.col_nb = col_nb    
    
    def __str__(self):
        return f"Plane {self.id} : {self.model} ({self.row_nb} x {self.col_nb})"    
    
    def to_dict(self):
        """Convert the Plane object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "model": self.model,
            "row_nb": self.row_nb,
            "col_nb": self.col_nb
        }
    @classmethod
    def from_dict(cls, data):
        """Create a Plane object from a dictionary (JSON deserialization)."""
        return cls(
            model=data["model"],
            row_nb=data["row_nb"],
            col_nb=data["col_nb"],
        )
