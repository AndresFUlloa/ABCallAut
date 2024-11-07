

class UserDTO:

    def __init__(self):
        self.name: str = ""
        self.last_name: str = ""
        self.email: str = ""
        self.password: str = ""
        self.id_number: str = ""
        self.cellphone: str = ""
        self.password: str = ""
        self.id_type: str = ""
        self.role: str = ""


    def __str__(self):
        return f'Name: {self.name}, Last Name: {self.last_name}, Email: {self.email}, ID Number: {self.id_number}, ' \
               f'Id Type: {self.id_type}, Role: {self.role}'


