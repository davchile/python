# name = input("What's you name? ") # name is a variable and input is a function

# removes whitespace from str
# name = name.strip() # name is the variable, then I use the variable, a dot and a function (built in Python). Technically this function is a method

"""
This is a comment
"""

# capitalize user's name
# name = name.capitalize()

# capitalize the first letter of each word
# name = name.title()

# putting all the methods in one line
# name = name.strip().title()

# even better, having one line of code to solve this problem
name = input("What's you name? ").strip().title()

# Split user's name into first and lastname
# first, last = name.split()

# removes all spaces in between and get only first name
parts = name.split()
first = parts[0]

print(f"hello {first}, how are you?") # estoy añadiendo la variable al string. Dos opciones para agregar variables. El signo + o la coma.