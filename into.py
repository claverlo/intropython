# ctl + s to save file
# up on arrow key in terminal for previous line



print("Hello World from Python") # No semi colon needed
print(2) # printing number
print(5 + 3)# print result

"""
This is a multi-line comment (docsting)
Triple quotes let you write longer explinations.
"""
# --- VARIABLES AND CONATENATION ---

name = "Leo"
age = 41
print(name,age) #Prints variable
print("My name is " + name + " and I am " + str(age) + " years old.")

# -- F-String (modern concatenation)
middle_name = "Marinas"
last_name = "Claveria"

#// Naming conventions: snake_case, camelCase

print(f"hello")
print(f"My name is {name} {middle_name} {last_name} and i am {age} years old.")
# tab key fills out variable

# Multi-line f-string
print(f"""
My name is {name} {middle_name} {last_name}
and i am {age}
years old.
""")

# MINICHALLENGE 1

my_name = "Leomar"
my_last_name = "Claveria"
my_age = 41
my_favorite_technology = "Python"

print(f"My name is {my_name} {my_last_name}, I am {my_age} years old, and my favorite technology is {my_favorite_technology}")


# ---TYPE FUNCTION---
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
print(type(True))   # <class 'bool'>
# highlight and ctrl + / creates comment


# -- Casting (Changing Data Types) ---
print(20 + int("20"))   # 40
print(20 + age)         # 43
print(20 + 2.98)        #22.98

# --- INPUT FUNCTION ---
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")



user_age = int(input("Enter your age: "))
print(age + user_age)
# print(f"you are {user_age} years old")

# --- Mini Challenge 2 ---

"""
Pizza Calculator
- Ask how many slices of pizza and how many people.
- Use math operators to calculate slices per person.
- Show the result with an f-string.
"""

slices = int(input("How many slices of pizza? "))
people = int(input("How many people? "))

slices_per_person = slices / people

print(f"Each person gets {slices_per_person} slices of pizza")
