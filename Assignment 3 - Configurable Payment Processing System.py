class PaymentStrategy:
    def pay(self, amount):
        print("Payment method not selected...")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using PayPal.")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Bitcoin.")

class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)

def main():

    print("\n=================================================")
    print("     CONFIGURABLE PAYMENT PROCESSING SYSTEM")
    print("=================================================")


    print("---------------------------------------")
    amount = float(input("Enter Payment Amount (₹): "))
    print("---------------------------------------")


    print("\n-------------------------------------------------")
    print("              PAYMENT METHODS")
    print("-------------------------------------------------")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. Bitcoin")
    print("-------------------------------------------------")


    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        processor = PaymentProcessor(CreditCardPayment())

    elif choice == 2:
        processor = PaymentProcessor(PayPalPayment())

    elif choice == 3:
        processor = PaymentProcessor(BitcoinPayment())

    else:
        print("Invalid choice!")
        return


    print("\n-------------------------------------------------")
    print("              PAYMENT STATUS")
    print("-------------------------------------------------")

    processor.process_payment(amount)

    print("\n=================================================")
    print("Thank You for using the system!")
    print("=================================================")

main()