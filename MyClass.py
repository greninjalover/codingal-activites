class MyClass:
    __privatevar=27
    def __privmethod(self):
        print("I'm inside class MyClass")

    def hello(self):
        print("Private Variable:",MyClass.__privatevar)


foo = MyClass()
foo.hello()
#foo.__privmethod()
foo.__privatevar=30
foo.hello()