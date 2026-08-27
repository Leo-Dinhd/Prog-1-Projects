tankSize=int(input(f"How big is your car's gas tank: "))
gallonsInTank=int(input(f"How many gallons are in your tank now: "))
priceOfGas=int(input(f"What is the price of gas per gallon: "))
total=(tankSize-gallonsInTank)*priceOfGas
print(f"Your gas will cost: $" {total})
