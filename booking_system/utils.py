


def coordinates_converter(coord):
    """This function converts the seat coordinates (C5) in the planes to standard coordinates. (rangee =3, numero = 5)"""
    lettre = coord[0]
    row = int(coord[1:]) -1
    col = ord(lettre.upper()) - ord('A')
    return col, row

def reverse_coordinates_converter(col, row):
    """This function converts the standard coordinates (col, row) back to seat coordinates (e.g., C5).
    
    Args:
        col (int): Column number (starting from 0).
        row (int): Row number (starting from 0).
    
    Returns:
        coord (str): The seat coordinates in format like 'C5'.
    """
    # col =col - 1
    # row = row - 1
    lettre = chr(col + ord('A'))  # Convert column number to letter
    seat_number = str(row + 1)  # Convert row number back to 1-indexed seat number
    return lettre + seat_number


def is_passport_number_valid(passport_number):
    """This function checks if the passport number is valid.
    """
    if len(passport_number) != 9:
        print("The passport number must have 9 characters")
        return False
    return True

def save_json(): 
    """This function allow to save the full system data in a json file.
    """
    pass

def load_json():
    """This function allow to load the full system data from a json file at the start of the program.
    """
    pass

