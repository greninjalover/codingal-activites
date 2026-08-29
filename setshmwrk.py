from array import array

print("SCHOOL SNACK COUNTER")
print()

box1 = {"Apple", "Chips", "Juice", "Muesli Bar"}
box2 = {"Chips", "Juice", "Cookie", "Banana"}

print("Snack Box 1:", box1)
print("Snack Box 2:", box2)
print()

box1.add("Popcorn")

print("Box 1 after adding Popcorn:")
print(box1)
print()

shared_snacks = box1.intersection(box2)

print("Snacks in both boxes:")
print(shared_snacks)
print()

snack_counts = array("i", [10, 15, 8, 12])

print("Snack counts:")
print(snack_counts)
print()

snack_counts.insert(2, 20)
snack_counts.append(25)

print("After adding new snack counts:")
print(snack_counts)
print()

print("Number of 15s:", snack_counts.count(15))

snack_counts.reverse()

print("Reversed snack counts:")
print(snack_counts)