# challenge Order Status
from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5


class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.status = OrderStatus.PENDING 

    def update_status(self, new_status):
        if isinstance(new_status, OrderStatus):
            self.status = new_status
            print (f"Order: {self.order_id} updated to: {self.status}")
        else: 
            print("Invalid status.\n")
    
    def display(self):
        print(f"OrderID: {self.order_id}, CustomerName: {self.customer_name}, OrderStatus: {self.status}")

if __name__ == "__main__":
    o=Order(101, 'James Cavanaugh')

    o.display()
    o.update_status(OrderStatus.PROCESSING)
    o.display()