a = int(input("How tall is sibiling A in cm? "))
b = int(input("How tall is sibiling B in cm? "))
c = int(input("How tall is sibiling C in cm? "))
if a > b and a > c:
    print("Sibiling A is the tallest")
elif b > a and b > c:
    print("sibiling B is the tallest")
elif c > a and c > b:
    print("sibiling C is the tallest")
else:
    print("invalid input")

