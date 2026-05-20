x = int(input("What's x? "))
y = int(input("What's y? "))
"""
if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")
"""
# Now let's try a courser answer
"""
if x < y or x > y:
    print("x is not equal to y")

else:
    print("x is equal to y")
"""
# and now even more succint

"""if x != y:
    print("x is not equal to y")

else:
    print("x is equal to y")
"""
# and opposed in terms of order to the one before
if x == y:
    print("x is equal to y")

else:
    print("x is not equal to y")