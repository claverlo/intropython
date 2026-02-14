"""
A for loop in Python is a control structure that lets you repeat a block of code
for each item in a sequence

for variable in sequence:
    # Code block runs for each item in the sequence
"""

# basic example
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

print("---------------------------------")

for letter in "Leo":
    print(letter)

print("---------------------------------")
# range() generates a sequence of numbers

for x in range(5): # range of 5 in index
    print(x)

print("---------------------------------")

# start and end with range()
for x in range(2, 6):
    print(x)

print("---------------------------------")

for number in range(0, 10, 2):
    print(number)


    print("---------------------------------")

# else in for loops
for x in range(3):
    print(x)
else:  # this runs when loop is done
    print("Loop done!")


print("---------------------------------")

# BREAK and CONTINUE in for loops
for x in range(15):
    if x == 5:
        continue  # Skips 5 because continue goes to the next iteration
    if x == 8:
        break  # Stops loop completely
    print(x)



""""
mini challenge
"""

# # Ask the user for a number
# num = int(input("Enter a number: "))
# # Loop from 1 to 10
# for i in range(1, 11):
#     result = num * i
#     print(f"{num} x {i} = {result}")



"""
WHILE LOOPS
A while loop repeats a block of code as long as condition is True.
Be careful — if the condition never becomes False, you'll get an INFINITE loop!

while condition:
    # Code block runs as long as condition is True
"""""
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # Assignment operator which increases count each time (so the loop ends)

print("---------------------------------")

# Using break to stop the loop
number = 0

while True:  # infinite loop
    print(number)
    number += 1
    if number == 3:
        break  # stop the loop when number hits 3

print("---------------------------------")

# using continue to skip iteration
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue  # skips 3
    print(count)

print("---------------------------------")

# else with while loops
# The else block runs when the loop condition becomes False (not by breaking)

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished!")


#mini challenge

password = ""

while password != "secret123":
    password = input("Enter password: ")

    if password != "secret123":
        print("Wrong! Try again.")

print("Access granted!")