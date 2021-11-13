a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

if a < b and a < c:
    print(f"The lowest number is {a}.")
elif b < a and b < c:
    print(f"The lowest number is {b}.")
else:
    print(f"The lowest number is {c}.")