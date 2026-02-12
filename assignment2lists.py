# LISTS PRACTICE

# Creating a new list
books = ["Math", "Science", "History", "English"]
print("Original list:", books)

# Accessing items by index
print("First book:", books[0])
print("Third book:", books[2])

# Replacing a value
books[1] = "Biology"
print("After replacing Science with Biology:", books)

# Removing item by value
books.remove("History")
print("After removing History:", books)

# Removing item by index
books.pop(1)
print("After removing item at index 1:", books)

# Printing the list and its length
print("Final list:", books)
print("Length of list:", len(books))
