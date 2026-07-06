"""# countdown
i = 3
while i != 0:
    print("meow")
    i = i - 1

#count up
i = 1
while i <= 3:
    print("meow")
    i = i + 1

# counting generally adopted (from 0)
i = 0
while i < 3:
    print("meow")
    i = i + 1

# using for and lists
for i in [0, 1, 2]:
    print("meow")

# using for and range (for big numbers) and a default variable
for _ in range(3):
    print("meow")

# super succint
print("meow\n" * 3, end="")

# When you want to get user input that matches a certain expectation
while True:
    n = int(input("What's n?: "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
"""
# And now using main function
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()