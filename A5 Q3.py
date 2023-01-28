a = int(input("Enter first side of the triangle "))
b = int(input("Enter second side of the triangle "))
c = int(input("Enter third side of the triangle "))
if c>a+b or b>a+c or a>b+c:
    print("The given triangle is not possible ")
s = (a+b+c)/2
a = s*(s-a)*(s-b)*(s-c)
area = a**0.5
print(area)
