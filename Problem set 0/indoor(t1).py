# First try
address = input("Write down your home address please: ").lower()
print(f"ok then, your order will be shipped to {address} in the next 4 hours.")

# Second try
def hello(to="Hello world, say something"):
    print(to)

hello()
something = input(" ").lower()
hello(something)