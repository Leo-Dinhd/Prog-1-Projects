price=float(input("Enter the price of the item:"))
salesTaxPercent=float(input("Enter the sales tax percentage:"))
total=price*(1+salesTaxPercent/100)
print(f"Your total is ${total:.2f}")