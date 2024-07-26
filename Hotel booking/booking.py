class BookedHotel:

    def __init__(self, hotel_name, no_of_rooms):
        self.hotel_name = hotel_name
        self.no_of_rooms = no_of_rooms

class Booking:

    def __init__(self):
        self.hotel_rooms = []

    def add_to_booking(self, hotel_name, no_of_rooms):
        for item in self.hotel_rooms:
            if item.hotel_name.hotel_id == hotel_name.hotel_id:
                item.no_of_rooms += no_of_rooms
                return
        self.hotel_rooms.append(BookedHotel(hotel_name,no_of_rooms))

    def remove_from_booking(self, hotel_id):
        self.hotel_rooms = [item for item in self.hotel_rooms if item.hotel_name.hotel_id != hotel_id]

    def view_booking(self):
        return self.hotel_rooms
