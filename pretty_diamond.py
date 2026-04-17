RowS=int(input("Enter A Value To Make Rows"))

number=1 

for i in range(1,RowS+1):
    for j in range(1,i+1):
        print(number,end=(" "))
        number=number+1
    print()

