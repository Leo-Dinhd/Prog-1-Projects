price=float(input("Enter the price: "))
blackFriday=input("Is it black friday [y/n]: ")
coupon=input("Do you have a coupon [y/n]: ")
employeeDiscount=input("Do you have an employee discount [y/n]: ")

if(blackFriday=="y"):
    price=price*.60
if(coupon=="y"):
    price=price*.95
if(employeeDiscount=="y"):
    price=price*.80

print(f"The final price is: ${price:.2f}")