class computer:
    def __init__(self):
        self.__maxprice=900

    def sell(self):
        print("Selling Price = {}".format(self.__maxprice))

    def setmaxprice(self, price):
        self.__maxprice=price


c=computer()
c.sell()

c.__maxprice=1500
c.sell()

c.setmaxprice(1500)
c.sell()
