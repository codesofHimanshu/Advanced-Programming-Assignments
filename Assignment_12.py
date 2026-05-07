from abc import ABC, abstractmethod

# ---------------- PAYMENT ----------------
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class WalletPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")


# ---------------- NOTIFICATION ----------------
class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(NotificationService):
    def send(self, message):
        print(f"Email: {message}")

class SMSNotification(NotificationService):
    def send(self, message):
        print(f"SMS: {message}")

class PushNotification(NotificationService):
    def send(self, message):
        print(f"Push: {message}")


# ---------------- STORAGE ----------------
class Storage(ABC):
    @abstractmethod
    def save(self, order):
        pass

class DatabaseStorage(Storage):
    def save(self, order):
        print(f"Order {order.order_id} saved in Database")

class FileStorage(Storage):
    def save(self, order):
        print(f"Order {order.order_id} saved in File")


# ---------------- ORDER ----------------
class Order(ABC):
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    @abstractmethod
    def get_final_amount(self):
        pass

class RegularOrder(Order):
    def get_final_amount(self):
        return self.amount

class DiscountedOrder(Order):
    def get_final_amount(self):
        return self.amount * 0.9

class PriorityOrder(Order):
    def get_final_amount(self):
        return self.amount + 50


# ---------------- SERVICE ----------------
class OrderService:
    def __init__(self, payment, notifier, storage):
        self.payment = payment
        self.notifier = notifier
        self.storage = storage

    def place_order(self, order):
        final_amount = order.get_final_amount()
        print(f"\nProcessing Order {order.order_id}...")

        self.payment.pay(final_amount)
        self.storage.save(order)
        self.notifier.send(f"Order {order.order_id} successful!")

        print("Order Completed\n")


# ---------------- FACTORY FUNCTIONS ----------------
def get_payment(choice):
    if choice == "1":
        return CreditCardPayment()
    elif choice == "2":
        return UPIPayment()
    elif choice == "3":
        return WalletPayment()
    else:
        raise ValueError("Invalid payment option")

def get_notification(choice):
    if choice == "1":
        return EmailNotification()
    elif choice == "2":
        return SMSNotification()
    elif choice == "3":
        return PushNotification()
    else:
        raise ValueError("Invalid notification option")

def get_storage(choice):
    if choice == "1":
        return DatabaseStorage()
    elif choice == "2":
        return FileStorage()
    else:
        raise ValueError("Invalid storage option")

def get_order_type(choice, order_id, amount):
    if choice == "1":
        return RegularOrder(order_id, amount)
    elif choice == "2":
        return DiscountedOrder(order_id, amount)
    elif choice == "3":
        return PriorityOrder(order_id, amount)
    else:
        raise ValueError("Invalid order type")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    order_id = int(input("Enter Order ID: "))
    amount = float(input("Enter Amount: "))

    print("\nSelect Order Type:")
    print("1. Regular  2. Discounted  3. Priority")
    order_choice = input("Choice: ")

    print("\nSelect Payment:")
    print("1. Credit Card  2. UPI  3. Wallet")
    payment_choice = input("Choice: ")

    print("\nSelect Notification:")
    print("1. Email  2. SMS  3. Push")
    notif_choice = input("Choice: ")

    print("\nSelect Storage:")
    print("1. Database  2. File")
    storage_choice = input("Choice: ")

    # Create objects using factory
    order = get_order_type(order_choice, order_id, amount)
    payment = get_payment(payment_choice)
    notifier = get_notification(notif_choice)
    storage = get_storage(storage_choice)

    # Inject into service
    service = OrderService(payment, notifier, storage)

    # Place order
    service.place_order(order)