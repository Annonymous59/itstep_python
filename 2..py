name = input("Name: ")
print(f"Welcome {name}!")
age = int(input("Age: "))

if age < 18:
    print("You are child yet")
if age >= 18:
    print("You are adult")