S = int(input("what is the number of small treats? "))
M = int(input("what is the number of medium treats? "))
L = int(input("what is the number of large treats? "))

Barley_happiness = 1 * S + 2 * M + 3 * L
if Barley_happiness >= 10:
    print("barley is happy")
else:
    print("Barley is Sad")
