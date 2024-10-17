
from booking_system.plane import Plane

class Plane_handler: 
    def __init__(self):
        self.planes = []
    
    def __str__(self):
        planes = ""
        for plane in self.planes:
            planes += f"Plane {plane.id} : {plane.model} ({plane.row_nb} x {plane.col_nb}) \n"
        return(planes)
    
    def create_plane(self, model, row_nb, col_nb):
        # checking inputs
        if not isinstance(model, str):
            raise ValueError("model must be a string")
        if not isinstance(row_nb, int) or not isinstance(col_nb, int):
            raise ValueError("row_nb and col_nb must be an integer")
        plane = Plane(model, row_nb, col_nb)
        self.planes.append(plane)
        print(f"Plane {plane.id} created with {plane.row_nb} rows and {plane.col_nb} columns")
        return plane
    
    def delete_plane(self, id_plane):
        for plane in self.planes : 
            if plane.id == id_plane:
                self.planes.remove(plane)
                print(f"Plane {id_plane} deleted")
                return
        raise ValueError("No plane with this id")
    
    def get_planes(self):
        return self.planes
    
    def get_plane(self, id_plane):
        for plane in self.planes : 
            if plane.id == id_plane:
                return plane
        print(f"Plane {id_plane} not found")
        return None
    
    def get_plane_from_id(self, id_plane):
        for plane in self.planes : 
            if plane.id == id_plane:
                return plane
        print(f"Plane {id_plane} not found")
        return None
    
    @classmethod
    def from_dict(cls, data):
        """Create a Plane_handler object from a dictionary (JSON deserialization)."""
        handler = cls()
        # Charger chaque avion depuis la liste dans le JSON
        handler.planes = [Plane.from_dict(plane_data) for plane_data in data]
        return handler
    