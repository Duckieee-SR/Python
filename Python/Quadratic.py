a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

x1 = (-float(b) + (float(b) ** 2 - 4 * float(a) * float(c)) ** 0.5) / (2 * float(a))
x2 = (-float(b) - (float(b) ** 2 - 4 * float(a) * float(c)) ** 0.5) / (2 * float(a))

print("x1 is: ", x1)
print("x2 is: ", x2)