def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)
    print(f"{calculating(x, y, z):.1f}")

def calculating(x, y , z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    else:
        return x / z    
main()

