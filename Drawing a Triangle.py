import math
a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
c = int(input("Enter your third number"))
if a+b>c and a+c>b and b+c>a:
    print("The Triangle's Perimeter is:")
    print(int(a+b+c))
    print("The Area of the triangle is:")
    print(int(math.sqrt((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c)))
else:
    print("The numbers do not form a triangle")
input("Press any key to continue")