w = (float(input("Enter your weight in kg")))
h = (float(input("Enter your height in cm")))

BMI=w/(h/100)**2

if(BMI<18.4):
    print("underweight")#eat more food!!!
elif(BMI<24.9):
    print("healthy")#doing good but i recommend to eat a little more;)
elif(BMI<29.9):
    print("overweight")# your just not getting my point when i said eat more i didnt mean eat all of mcdonals chicken nuggets eat less!!!
elif(BMI<39.9):
    print("obese")# i literally said dont eat what part of eat less did you not understand
else:
    print("seriously obesed")# no no no no pls dont make him come here i am even seeing another doctor because of him just tell him "RIP brother"
