# store data in KEY:VALUE pairs
# think of them as a realife dictionary (word -> definition)
# They require curly brackets { }

student = {
    "name": "Leo",
    "age": 23,
    "major": "Computer Science"
}

print(student)

# Accessing Items
print(student["name"]) # will print = Leo
print(student.get("major")) # will print = major


# Adding new items
student["graduation_year"] = 2025 # will add graduation_year = 2025 
print (student)


# Changing Values
student["age"] = 30
print(student)

# Removing Items
student.pop("major") #w will remvoe the = major
print(student)


# Check if KEY exists
if "name" in student:
    print("Key 'name' exists in the dictionary!") # study this one how it works!!!!!!!!!!!!!!!!!!



# Nested Dictoinary
students = {
    "student1": {"name": "Leo", "age": 23},
    "student2": {"name": "alex", "age": 26} # will print = Leo
}

print(students["student1"]["name"])


#Mini challenge

report_card = {                  # created the report card
    "name": "leo",
    "subject": "Math",
    "grades": (90, 85, 88)
}


print(report_card["name"])
print(report_card["subject"])          # Print the student's name and subject


average = sum(report_card["grades"]) / len(report_card["grades"]) # average of the 3 grades


report_card["average"] = average   # the average of the score 


if average >= 90:
    print("Excellent!")
elif average >= 70:
# 70 <= average <= 89:  # average and print result
    print("Good Job!")
else:
    print("Needs improvement")


report_card.pop("subject") # i  Remove the "subject" key and print the updated dictionary
print(report_card)
