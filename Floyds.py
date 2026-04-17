ROWS=int(input("Enter A Value For Rows"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
number=1

for i in range(1, ROWS+1):
    for j in range(1,i+1):
        print(number,end=' ')
        number= number+1
    print()
    
