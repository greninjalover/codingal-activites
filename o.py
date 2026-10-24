class Account:
    def __init__(self, name, pin):
        self.name = name
        self.__pin = pin

    def get_pin(self):
        return "PIN is private"

    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN changed successfully")
        else:
            print("PIN must be 4 numbers")

    def __str__(self):
        return "Account Name: " + self.name + "\nPIN: ****"


my_account = Account("Alex", "1234")

print(my_account)

print("Trying to access private PIN:")
print(my_account.get_pin())

print("Changing PIN:")
my_account.set_pin("5678")

print("Updated account:")
print(my_account)