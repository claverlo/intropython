#LISTS
# Lists are used to store Multiple items in a single variable.
# Think of it as a "container"
# print the list to the screen

my_list = [10, 20, 30, 40, 50] #snake case _ underscore
print(my_list)

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# Accessing list items by their INDEX number
# indexing starts at 0
fruit = ["apple", "banana", "cherry"]
print(fruit[0])
print( fruit[2])

# You can also use NEGATIVE indexes to count from the end
print(fruit[-1]) # -1 will print Cherry and -2 banana and -3 apple

# Modifying list items
fruit[1] = "mango" # this will repalce banana
print(fruit)

# Adding items
fruit.append("orange") # append is a funtion and it add 1 item (argrument) at the end so this will print out = ['apple', 'mango', 'cherry', 'orange']
print(fruit)


fruit.insert(1, "kiwi") # it put in the postion between #1 and 2. ['apple', 'kiwi', 'mango', 'cherry', 'orange']
print(fruit)

# Removing items
fruit.remove("cherry") #['apple', 'kiwi', 'mango', 'orange']
print(fruit)

fruit.pop() #['apple', 'kiwi', 'mango']
print(fruit)


# Looping through a list
for fruit in fruit:  # will list it each individual line (vertical)
    print(fruit)


# Check if ITEM exists
if "mango" in fruit:
    print("Yes, mango is in the list!") # will print = Yes, mango is in the list!

# LIST LENGTH
print(len(fruit)) # of items in the list( most oen created) it will print = 5
