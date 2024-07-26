class Rooms:

    def __init__(self,hotel_id, name, type_of_room, city, price, availability):
        self.hotel_id = hotel_id
        self.name = name
        self.type_of_room = type_of_room
        self.city = city
        self.price = price
        self.availability = availability

class Hotels:

    def __init__(self):
        self.hotels = {}

    def add_hotels(self, hotel_name):
        self.hotels[hotel_name.hotel_id] = hotel_name

    def update_hotels(self, hotel_id, updated_hotels):
        if hotel_id in self.hotels:
            self.hotels[hotel_id] = updated_hotels

    def delete_hotels(self, hotel_id):
        if hotel_id in self.hotels:
            del self.hotels[hotel_id]

    def search_hotels(self,name):
        return [hotel_name for hotel_name in self.hotels.values() if name.lower() in hotel_name.name.lower()]


