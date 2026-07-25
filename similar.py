def match(word):
    ctr=0
    lst=[]

    for i in word:
        if len(i)>1 and i[0]==i[-1]:
            ctr=ctr+1
            lst.append(i)
    print(lst)
    return ctr 
count=match(['abc','cbc','dbc','1221'])   
print(count)
    