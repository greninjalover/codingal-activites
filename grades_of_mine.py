digitech= int(input())
science= int(input())
maths= int(input())
reading= int(input())
coding= int(input())

tot=digitech+science+maths+reading+coding

avg=tot/5

if(avg>=91 and avg<=100):
    print("grade A")

elif(avg>=81 and avg<=90):
    print("grade B")
    
elif(avg>=71 and avg<=80):
    print("grade C")

elif(avg>=61 and avg<=70):
    print("grade D")

elif(avg>=51 and avg<=60):
    print("grade E")

elif(avg>=41 and avg<=50):
    print("grade F")

else:
    print("You FAILED")