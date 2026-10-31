from abc import ABC, abstractmethod
class Abclass(ABC):
    def print(self, x):
        print("Passed Value", x)

    @abstractmethod
    def task(self):
        print("We are inside the Absclass Task")

class testclass(Abclass):
     def task(self):
            print("We are inside the testclass Task")

test_obj=testclass()
test_obj.task()
test_obj.print(153)