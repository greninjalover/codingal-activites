a = int(input("Enter first number (A): "))
b = int(input("Enter second number (B): "))
c = int(input("Enter third number (C): "))

print(f"\nBefore swap: A={a}, B={b}, C={c}")

holding_box = a
a = b
b = c
c = holding_box

print(f"After swap:  A={a}, B={b}, C={c}")

