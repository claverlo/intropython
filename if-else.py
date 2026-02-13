'''TThe if block runs only if the condition evalueates to true.
If the condition is False, the else block runs instead.
You can also add elif (else if) blocks to check multiple conditions in sequence.
if condition:
    - Code block runs if condition is True
elif another_condition:
    - Code block runs if the first condition is False and this condition is True
else: 
    - Code block runs if none of the above conditions are True

'''


x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


x = -10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")



# short hand If statements
# you can do it all in one line



if x > 5: print("x is greater than 5")


# short hand if else
print("Even") if x % 2 == 0 else print("Odd")


# nested if Statements

if x > 0:
    if x < 20:    # both of this myust be true in order to work
        print("x is a positive number less than 20")


# combining conditions

age = 18

if age >= 18 and age <= 21:
    print("You are between 18 and 21 years old")


# Mini challenge
# Mini challenge

# 1. Ask the user to enter a number from 0-100 and store it in a variable called "score".
# 2. If the score is 90 or above, print "Grade: A".
# 3. If the score is between 80-89, print "Grade: B".
# 4. If the score is between 70-79, print "Grade: C".
# 5. Otherwise, print "Grade: F".

# 6. Create a variable "passed" – set it to True if score >= 70, otherwise False.
# BONUS: If passed is True, print "Congratulations!", otherwise print "Try again!"


score = int(input("Enter a number from 0-100: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

passed = True if score >= 70 else False

if passed:
    print("Congratulations!")
else:
    print("Try again!")
