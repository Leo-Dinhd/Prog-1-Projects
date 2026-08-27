initialPrinciple=float(input("Initial principle: "))
interestRate=float(input("Interest rate: "))
timesInterestApplied=float(input("How many times does interest apply annually: "))
yearsPassed=float(input("How may years have passed: "))

total=initialPrinciple*(1+(interestRate/100)/timesInterestApplied)**(timesInterestApplied*yearsPassed)

print(f"You now have ${total:.2f}")