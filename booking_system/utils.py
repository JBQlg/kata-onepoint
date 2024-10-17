


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
    #check if the row and col are valid
    if row < 0 or col < 0:
        raise ValueError("The row and column numbers must be positive.")
    lettre = chr(col + ord('A'))  
    seat_number = str(row + 1)  
    return lettre + seat_number

def is_passport_number_valid(passport_number):
    """This function checks if the passport number is valid.
    """
    if len(passport_number) != 9:
        print("The passport number must have 9 characters")
        return False
    return True


from datetime import datetime

def validate_date(date_str):
    """Valide que la chaîne de caractères correspond bien au format d'une date.
    
    Args:
        date_str (str): La chaîne de caractères représentant une date.
    
    Raises:
        ValueError: Si la chaîne de caractères n'est pas au format attendu.
    """
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"La date '{date_str}' n'est pas au format attendu 'YYYY-MM-DD'.")
    if date_obj.date() <= datetime.today().date():
        raise ValueError(f"La date '{date_str}' doit être dans le futur.")

