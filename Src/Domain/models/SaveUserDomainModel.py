import datetime


class SaveUserDomainModel:
    # Cart_id: int
    name: str
    email: str
    password: str
    access_level: int
    address: str
    postal_code: int
    phone_number: int

    def __init__(self, name: str, email: str, password: str, access_level: int,
                 address: str, postal_code: int, phone_number: int):

        # self.Cart_id = Cart_id
        self.name = name
        self.email = email
        self.password = password
        self.access_level = access_level
        self.address = address
        self.postal_code = postal_code
        self.phone_number = phone_number

    def to_dict(self):
        return {
                # "Cart_id": self.Cart_id,
                "name": self.name,
                "email": self.email,
                "password": self.password,
                "access_level": self.access_level,
                "address": self.address,
                "postal_code": self.postal_code,
                "phone_number": self.phone_number
                }


