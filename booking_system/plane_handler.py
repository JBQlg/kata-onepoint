
from booking_system.plane import Plane

class Plane_handler: 
    def __init__(self):
        self.planes = []
    
    def create_plane(self, model, row_nb, col_nb):
        plane = Plane(model, row_nb, col_nb)
        self.planes.append(plane)
        print(f"Plane {plane.id} created with {plane.row_nb} rows and {plane.col_nb} columns")
        return plane
    
    def get_planes(self):
        return self.planes
    
    def get_plane(self, id_plane):
        for plane in self.planes : 
            if plane.id == id_plane:
                return plane
        print(f"Plane {id_plane} not found")
        return None
    