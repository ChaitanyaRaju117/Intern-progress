# Day 1 — Python basics practice

# Variables and data types
name = "Chaitu"
age = 22
height = 5.9
is_intern = True

print(type(name), type(age), type(height), type(is_intern))

# Type coercion
print(str(age) + " years old")    
print(age + height)        

# f-strings
print(f"Hello, I'm {name}. I am {age} years old.")
print(f"Height: {height:.1f} ft")

# String methods
company = "  anthropic internship  "
print(company.strip().title())
print(company.strip().upper().replace("ANTHROPIC", "My"))

# String slicing
lang = "Python 3.12"
print(lang[:6])      
print(lang[-4:])     
print(lang[::2])     

# Arithmetic operators
a, b = 17, 5
print(a + b, a - b, a * b)
print(a / b)    
print(a // b)   
print(a % b)    
print(a ** b)   

