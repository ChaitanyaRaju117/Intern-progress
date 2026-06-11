# Day 2 - Control Flow and Loops Practice

print("--- Grade Calculator ---")
marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Marks: {marks} → Grade: {grade}")


print("\n--- For Loop ---")
fruits = ["apple", "banana", "mango", "orange"]
for fruit in fruits:
    print(f"  Fruit: {fruit}")


print("\n--- Even numbers from 1 to 20 ---")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()


print("\n--- Break example ---")
print("Stop at first multiple of 7:")
for i in range(1, 50):
    if i % 7 == 0:
        print(f"  Found first multiple of 7: {i}")
        break


print("\n--- Continue example ---")
print("Skip multiples of 3 from 1 to 15:")
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()


print("\n--- While Loop Countdown ---")
count = 5
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  Go!")


print("\n--- Functions with Default Args ---")

def greet(name, greeting="Hello"):
    """Greets a person with a custom or default greeting."""
    print(f"  {greeting}, {name}!")

greet("Chaitu")
greet("Chaitu", "Good morning")
greet("Manager", "Good evening")


# --- variable scope ---
print("\n--- Variable Scope ---")
x = 10  

def show_scope():
    x = 20  # local variable - does not affect global x
    print(f"  Inside function: x = {x}")

show_scope()
print(f"  Outside function: x = {x}")


print("\n--- Docstring Example ---")

def add_numbers(a, b):
    
    return a + b

result = add_numbers(10, 20)
print(f"  10 + 20 = {result}")
print(f"  Function docs: {add_numbers.__doc__}")