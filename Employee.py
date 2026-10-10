class Employee:
    def __init__(self):
        print("employee object created")
    def __del__(self):
        print("employee deleted")

def create_object():
    print("making object")
    obj=Employee()
    print("function ends")
    return obj
print("calling the create function object")
obj=create_object()
print("program end")