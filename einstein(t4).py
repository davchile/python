def main():
    m = int(input("m= "))
    print("E=", m * (square(300000000)))

def square(e):
    return pow(e, 2)

main()