score = int(input("Score: "))
"""
if score >=90 and score <= 100:
    print("Grade: A")

elif score >=80 and score < 90:
    print("Grade: B")

elif score >=70 and score <80:
    print("Grade: C")

elif score >= 60 and score <70:
    print("Grade: D")

else:
    print("Grade: F")
"""
# Python allows you to nest and chain boolean expressions
"""
if 90 <= score <= 100:
    print("Grade: A")

elif 80 <= score < 90:
    print("Grade: B")

elif 70 <= score <80:
    print("Grade: C")

elif 60 <= score <70:
    print("Grade: D")

else:
    print("Grade: F")
"""
# Why should I make two questions in every conditional?
if score >= 90:
    print("Grade: A")

elif score >= 80: # we implicity know that B is between 80 and 89 and so on
    print("Grade: B")

elif score >=70:
    print("Grade: C")

elif score >=60:
    print("Grade: D")

else:
    print("Grade: F")