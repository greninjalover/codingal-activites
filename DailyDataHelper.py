
class DailyDataHelper:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def show_data(self):
        print("\nDaily Data Helper")
        print("Name:", self.name)
        print("Data values:", self.values)

    def find_total(self):
        total = sum(self.values)
        print("Total:", total)

    def find_average(self):
        average = sum(self.values) / len(self.values)
        print("Average:", round(average, 2))

    def show_numbered_data(self):
        print("\nNumbered Data")

        for index, value in enumerate(self.values):
            print(index, ":", value)

    def search_data(self, number):
        for index, value in enumerate(self.values):
            if value == number:
                print(number, "was found at index", index)
                return

        print(number, "was not found")

    def __del__(self):
        print("Daily Data Helper has ended.")


data = DailyDataHelper("My Data", [10, 20, 30, 40, 50])

data.show_data()
data.find_total()
data.find_average()
data.show_numbered_data()
data.search_data(30)

del data
