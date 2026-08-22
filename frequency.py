test_dict={"Ramcharan":2 , "Is":2 , "The":2 , "Coolest":2 , "Guy":1}

print("the original dictionary", str(test_dict))

k=2

res=0

for key in test_dict:
    if test_dict[key]==k:
        res=res+1

print("frequency of k is", (res))      
