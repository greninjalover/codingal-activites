def palind(r):
    e=len(r)-1
    s=0

    while(s<e):
        if(r[s]!=r[e]):
            return False

        s+=1
        e-=1
    return True

r=(3,4,56,4,3,5)

if(palind(r)):
    print("The Tuple is a very Majestic Palindrome")
else:
    print("The Tuple is not a very Majestic Palindrome")
        