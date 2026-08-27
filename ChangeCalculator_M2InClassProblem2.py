listedPrice=float(input("What is the listed price of the item: "))
customerPay=float(input("How much did the customer pay: "))
salesTaxPercent=6
totalPrice=listedPrice*(1+salesTaxPercent/100)
total=customerPay-totalPrice
print(f"They get ${total:.2f}")