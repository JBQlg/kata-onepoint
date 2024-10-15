
class Plane : 
    _id_counter = 1
    def __init__(self, model, row_nb, col_nb) : 
        self.id = "P"+str(Plane._id_counter)
        Plane._id_counter += 1
        self.model = model
        self.row_nb = row_nb
        self.col_nb = col_nb    
    
    def __str__(self):
        return f"Plane {self.id} : {self.model} ({self.row_nb} x {self.col_nb})"    
    
    