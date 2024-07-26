class Order:

    def __init__(self, order_id, customer, no_of_rooms):
        self.order_id = order_id
        self.customer = customer
        self.no_of_rooms = no_of_rooms

class Payment:

    def process_payment(self,amount):
        print(f"Processing payment of ${amount}.")
        return True