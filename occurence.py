s1=input("Enter A Sentence Or Word")
c1=input("Enter A Letter")

#these are variables
i=0
count=0

#loops
while(i<len(s1)):
    if(s1[i]==c1):
        count=count+1
    i=i+1
print("The Letter Occured ", count," Times")


