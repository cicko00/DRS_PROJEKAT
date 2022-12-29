class User():
    first_name = None
    last_name = None
    password = None
    address = None
    town = None
    country = None
    phoneNumber = None
    email = None

     #konsutrktor sa poljima
    def __init__(self, fist_name, last_name, password, address, town, country, phone_number, email):
        self.first_name = fist_name
        self.last_name = last_name
        self.address = address
        self.password = password
        self.town = town
        self.country = country
        self.phoneNumber = phone_number
        self.email = email
