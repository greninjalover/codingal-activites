class iostring():
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1= input("Enter The String:")
    def print_string(self):
        print("The String Is:", self.str1.upper())

s1=iostring()
s1.get_string()
s1.print_string()