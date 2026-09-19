studentgrade={"Alex":50, "Adam":20, "Dave":100, "Angeline":80, "Ava":95}
total=0
for student in studentgrade:
    total= total + studentgrade.get(student)
    print(total)
avg=total/5
print(avg)
maximum=max(studentgrade)
minimum=min(studentgrade)
print(maximum)
print(minimum)

search=input("Whose grades are you looking for?")

if search== "Alex":
    print(studentgrade[0])

if search== "Adam":
    print(studentgrade[1])

if search== "Dave":
    print(studentgrade[2])

if search== "Angeline":
    print(studentgrade[3])

if search== "Ava":
    print(studentgrade[4])

else:
    print("sorry we dont know who that is")