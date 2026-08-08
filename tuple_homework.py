habits = ("Studying", True, 7, 20.5)
print(habits)
 
weeklyhabits = (1, 1, 0, 0, 0, 1, 1)
print(weeklyhabits)
 
print("Amount of days tracked:", len(weeklyhabits))
 
print("Day 1 status:", weeklyhabits[0])
print("Day 2 status:", weeklyhabits[1])
print("Day 3 status:", weeklyhabits[2])
print("Day 4 status:", weeklyhabits[3])
print("Day 5 status:", weeklyhabits[4])
print("Day 6 status:", weeklyhabits[5])
print("Day 7 status:", weeklyhabits[6])
firstfewdays = weeklyhabits[0:3]
print("First three days:", firstfewdays)
 
weekenddays = weeklyhabits[5:7]
print("Weekend days:", weekenddays)
 
weekly_habits = weeklyhabits + (1,)
print("After adding one more day:", weeklyhabits)
 
completed = weeklyhabits.count(1)
missed = weeklyhabits.count(0)
 
print("Completed days:", completed)
print("Missed days:", missed)
 
finished = 0
notdone = 0
 
for i in range(0, len(weeklyhabits)):
    if weeklyhabits[i] == 1:
        finished += 1
    else:
        notdone += 1
 
if finished > notdone:
    print("Great Job!")
else:
    print("Try to do it more often!!")#or dont do it at all ;)

 print("")
print("===== Weekly Habits =====")
print("Habit Name:", habits[0])
print("Weekly Record:", weeklyhabits)
print("Completed:", finished)
print("Missed:", notdone)
# sorry i tried my best but couldnt get it to work