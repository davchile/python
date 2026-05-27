"""
x = int(input("What's x? "))
 
if x % 2 == 0:
    print("Even")
 
else:
    print("Odd")
"""
# Using a main function
def main():
    x = int(input("what's x? ")) # I'm using is_even here to make a decision, in this case by printing "Even" or "Odd".
    if is_even(x):
        print("Even")
    else:
        print("Odd")
"""        
def is_even(n): # now that I have my own boolean function that answers this question for me, I can use it in this program forward or in another one.
    if n % 2 == 0:
        return True
    else:
        return False
"""
# this is the most succint and elegant way of using conditional in Python
def is_even(n):
    return n % 2 == 0

main()