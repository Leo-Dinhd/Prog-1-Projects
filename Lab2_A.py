sLength1=float(input("Side length 1: "))
sLength2=float(input("Side length 2: "))
sLength3=float(input("Side length 3: "))

if (sLength1==sLength2 and sLength2==sLength3):
    print("This is an equilateral triangle!")
elif(sLength1==sLength2 or sLength2==sLength3 or sLength1==sLength3):
    print("This is an isosceles triangle!")
else:
    print("This is a scalene triangle!")
