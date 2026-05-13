"""
name = input("What's you name? ") # name is a variable and input is a function

# removes whitespace from str
name = name.strip() # name is the variable, then I use the variable, a dot and a function (built in Python). Technically this function is a method

# capitalize user's name
name = name.capitalize()

# capitalize the first letter of each word
name = name.title()

# putting all the methods in one line
name = name.strip().title()

# even better, having one line of code to solve this problem
name = input("What's you name? ").strip().title()

# Split user's name into first and lastname
first, last = name.split()


# removes all spaces in between and get only first name
parts = name.split()
first = parts[0]

print(f"hello {first}, how are you?") # estoy añadiendo la variable al string. Dos opciones para agregar variables. El signo + o la coma.
"""

"""---------
# Time to use our own functions
def hello():
    print("Hello")

name = input("What's your name? ")
hello()
print(name)

# Including a parameter in my function
def hello(to):
    print("Hello,", to)

name = input("What's your name? ")
hello(name) # I just don't need to use the "print" built in function 

# Now the parameter has a default value
def hello(to="world"):
    print("Hello,", to)

hello() # It says hello, world before the user's input
name = input("What's your name? ")
hello(name)
"""
# Standard way to structure your code
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("Hello,", to)

main()
