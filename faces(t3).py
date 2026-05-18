# My way

def main():
    feel = input("How do you feel today →:) or :( →")
    convert(feel)

def convert(how):
    how = how.replace(":)","🙂").replace(":(","🙁")
    print("I feel", how)

main()
"""
# Best way to do it (according to GPT)
def main():
    feel = input("How do you feel today? ")
    print(convert(feel)) # print the result and could be also used in another function or saved anywhere else

def convert(how): # transform and return and can be used any time
    return how.replace(":)", "🙂").replace(":(", "🙁")

main()
"""
# how to leverage return insted of print
"""
def main():
    feel = input("How do you feel? ")
    result = convert(feel)
    excited(result)

def convert(how):
    return how.replace(":)", "🙂") # this line of code returns the value but it doesn't print it yet

def excited(text):
    print(text + "!!!") # here is where I print the argument of the variable "feel"

main()
"""