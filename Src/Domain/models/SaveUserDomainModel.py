import datetime


class SaveUserDomainModel:
    name: str
    email: str
    password: str
    access_level: int
    address: str
    postal_code: int
    phone_number: int
    creation_time: datetime

    def __init__(self, name: str, email: str, password: str, access_level: int,
                 address: str, postal_code: int, phone_number: int, creation_time: datetime):

        self.name = name
        self.email = email
        self.password = password
        self.access_level = access_level
        self.address = address
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.creation_time = creation_time

    def to_dict(self):
        return {
                "name": self.name,
                "email": self.email,
                "password": self.password,
                "access_level": self.access_level,
                "address": self.address,
                "postal_code": self.postal_code,
                "phone_number": self.phone_number,
                }


