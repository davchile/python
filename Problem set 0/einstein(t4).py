# First try
def main():
    m = int(input("m= "))
    print("E=", m * (square(300000000)))

def square(e):
    return pow(e, 2)

main()

# Second try (wrong formula)
def main():
    mass = int(input("m: "))
    print("E=", square(mass))
    
def square(e):
    return pow(e * 300000000, 2)

main()

# Best way according to GPT
def main():
    m = int(input("m= "))
    print("E=", energy(m))

def energy(m):
    return m * pow(300000000, 2)

main()