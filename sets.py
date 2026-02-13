# Unordered, unindexed, and do not allow duplicate values.
# my_set = {item1, item2, item3, ...}

fruits = {"apple", "banana", "cherry"}
print(fruits)

fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # duplicates are ignored



# check if item exists
print("banana" in fruits)

fruits.add("orange")  # add single item
print(fruits)



fruits.update(["kiwi", "mango"])  # updpate multiple items
print(fruits)


fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")  # removes item (error if not found)
print(fruits)


fruits.discard("kiwiii")  # removes item safely (no error if not found)
print(fruits)

# set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))  # combine both sets with no duplicates



print(set1.union(set2))          # combine both sets (no duplicates)
print(set1.intersection(set2))   # returns common elements
print(set1.difference(set2))     # elements in set1 but not in set2


# length
print(len(set1))

# copying sets
new_set = set1.copy()
print(new_set)

# clearing sets
set1.clear()
print(set1)

#mini challenge

# 1. create 2 sets:
# invited_friends{} 4 people
# rsvped= {} 3 people

invited_friends = {"Alex", "Ben", "Carla", "Diana"}
rsvped = {"Alex", "Ben", "Carla"}


# 2. print:

# everyone who was invited (union)
print(invited_friends.union(rsvped))

# everyone who said they're coming (rsvped)
print(rsvped)

# who hasn’t replied (difference)
print(invited_friends.difference(rsvped))


# 3. Add two new names to invited_friends
invited_friends.add("Ethan")
invited_friends.add("Faith")
print(invited_friends)


# 4. one of the people canceled - remove them from rsvped
rsvped.remove("Ben")
print(rsvped)


# 5. Print how many total confirmed guests are attending
print(len(rsvped))


# 1. create 2 sets:

# 1. create 2 sets:

invited_friends = {"Alex", "Ben", "Carla", "Diana"}
rsvped = {"Alex", "Ben", "Carla"}


# 2. print:

# everyone who was invited 
print(invited_friends.union(rsvped))  # combine both sets

# everyone who said they're coming
print(rsvped)

# who hasn’t replied 
print(invited_friends.difference(rsvped))  # invited but not replied


# 3. Add two new names to invited_friends
invited_friends.add("Ethan")
invited_friends.add("Faith")
print(invited_friends)


# 4. one of the people canceled - remove them from rsvped
rsvped.remove("Ben")
print(rsvped)


# 5. Print how many total confirmed guests are attending
print(len(rsvped))
