from rooms import Hotels, Rooms
from user_management import User, Customer, Admin
from booking import Booking, BookedHotel
from payment import Order, Payment
booking = Booking()
hotel = Hotels()

def search_hotel(hotel, query):
    results = hotel.search_hotels(query)
    for hotel_name in results:
        print(f"{hotel_name.name} - ${hotel_name.price}")
    return results

def main():

    users = {}
    current_user = None

    admin = Admin(1,"admin","password","admin@example.com")
    users[admin.username] = admin
    admin.add_hotels(Rooms(1,"Maharaja","Single room","Bangalore",1000,5), hotel)
    admin.add_hotels(Rooms(2,"Kings Palace","Double room","Pune",1500, 4), hotel)

    def register():
        user_id = len(users) + 1
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        email = input("Enter email: ")
        customer = Customer(user_id,username,password, email)
        users[username] = customer
        print("Registration Successfull.")

    def login():
        nonlocal current_user
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in users and users[username].password == password:
            current_user = users[username]
            print(f"Welcome, {current_user.username}!")
        else:
            print("Invalid username or password")

    def browse_hotels():
        query = input("Enter hotel name to search: ")
        results = search_hotel(hotel, query)
        if not results:
            print("No hotels found!")

    def booking_hotel():
        hotel_id = int(input("Enter hotel id: "))
        quantity = int(input("Enter number of rooms to book: "))
        if hotel_id in hotel.hotels:
            hotel_name = hotel.hotels[hotel_id]
            current_user.booking.add_to_booking(hotel_name,quantity)
            print(f"{quantity} rooms booked in {hotel_name.name}.")
        else:
            print("Hotel not found.")

    def view_booking():
        hotel_rooms = current_user.booking.view_booking()
        if not hotel_rooms:
            print("You have no bookings.")
        for hotel_room in hotel_rooms:
            print(f"Hotel: {hotel_room.hotel_name.name}, Number of rooms: {hotel_room.no_of_rooms}, Price: ${hotel_room.hotel_name.price*hotel_room.no_of_rooms}.")

    def place_order():
        if not current_user.booking.hotel_rooms:
            print("You have no bookings.")
            return
        order = Order(len(current_user.booking.hotel_rooms)+1,current_user,current_user.booking.view_booking())
        payment = Payment()
        total_amount = sum(hotel_room.hotel_name.price*hotel_room.no_of_rooms for hotel_room in order.no_of_rooms)
        if payment.process_payment(total_amount):
            print(f"Order {order.order_id} was placed successfully.")
            current_user.booking = Booking()

    while True:
        print("\n1. Register\n2. Login\n3. Browse Hotels\n4. Add to bookings\n5. View Bookings\n6. Place bookings\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            if current_user:
                browse_hotels()
            else:
                print("You need to log in first.")

        elif choice == '4':
            if current_user and isinstance(current_user, Customer):
                booking_hotel()
            else:
                print("You need to log in as a customer first.")
        elif choice == '5':
            if current_user and isinstance(current_user, Customer):
                view_booking()
            else:
                print("You need to log in as a customer first.")
        elif choice == '6':
            if current_user and isinstance(current_user, Customer):
                place_order()
            else:
                print("You need to log in as a customer first.")
        elif choice == '7':
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

