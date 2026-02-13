"""
def function_name(parameters):
    # Code block (indented)
    # Preform actions using the parameters
    return value #optional
"""
# Simple function (no parameters)

# Simple function (no parameters)

def my_function(): # 
    print("This is my function")  # This line run when its called

my_function()  # calling Function

# Function with parameter
# Parameters allow us to pass information into a function

def print_full_name(first_name, last_name):
    print(f"The name is: {first_name} {last_name}")

print_full_name("Leo", "Flores")


def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"  # sends back the full name as text

# Store the returned value in a variable whcih in here is the full_name
full_name = get_full_name("Leo", "Flores")
print(full_name)


"""
A default parameter means the function will use that value
if no argument is provided when calling the function.
"""

def greet(name="Student"):
    print(f"Hello, {name}! Welcome to class.")

# Calling with no argument -> uses the default
greet()  # Output: "Student"

# calling with an argument -> overrides the default
greet("Leo")  # Output: "Leo"

