from rooms import Rooms, Hotels
from booking import Booking
hotel = Hotels()

class User:

    def __init__(self, user_id, username, password, email):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email

class Admin(User):

    def __init__(self, user_id, username, password, email):
        super().__init__(user_id,username,password, email)

    def add_hotels(self, hotel_name, hotel):
        hotel.add_hotels(hotel_name)

    def update_hotels(self, hotel_id, updated_hotels, hotel):
        hotel.update_hotels(hotel_id, updated_hotels)

    def delete_hotels(self, hotel_id, hotel):
        hotel.delete_hotels(hotel_id)


class Customer(User):

    def __init__(self, user_id, username, password, email):
        super().__init__(user_id, username, password, email)
        self.booking = Booking()