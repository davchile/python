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
    print(convert(feel))

def convert(how):
    return how.replace(":)", "🙂").replace(":(", "🙁")

main()
"""