# A tuple is a bilt-in data structure that stores multiple
# items but they are imutable

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# access item
print(my_tuple[0])
print(my_tuple[2])

# single-item tuple
single = ("apple")
print(type(single))
print(single)

single = ("baking",) , #is need for tuple to work # Tuplel is liek constant, you cant cahgne it.
print(type(single))
print(single)


my_tuple = ("apple", "banana", "cherry", "water", "coke", "phone")
print(my_tuple)
print(my_tuple[0:4]) # it will print = ('apple', 'banana', 'cherry', 'water')   so basically = 0 < 4 


# nested tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)  #= (('a', 'b', 'c'), (1, 2, 3))
print(combine)

temp_list = list(my_tuple)# = 
print(temp_list)


temp_list.append("orange") 
my_tuple = tuple(temp_list)
print(my_tuple)


#  travel_bag / 5 items
travel_bag = ("shirt", "pants", "shoes", "toothbrush", "phone") #  travel_bag / 5 items

#  Print the second and fourth items
print(travel_bag[1])   # second item
print(travel_bag[3])   # fourth item


essential = ("passport", "wallet", "money") #new tuple  with 3  items
print(essential)
