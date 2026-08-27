tankSize=float(input(f"How big is your car's gas tank: "))
gallonsInTank=float(input(f"How many gallons are in your tank now: "))
priceOfGas=float(input(f"What is the price of gas per gallon: "))
total=(tankSize-gallonsInTank)*priceOfGas
print(f"Your gas will cost: ${total:.2f}" )
