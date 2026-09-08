unitFrom=input("Enter the unit you are converting from: ")
unitTo=input("Enter the unit you are converting to: ")
temp=float(input(f"Enter the temperature in {unitFrom}: "))
if(unitFrom=="Fahrenheit"):
    if(unitTo=="Celsius"):
        temp=(temp-32)*(5/9)
    elif(unitTo=="Fahrenheit"):
        temp=temp
    else:
        temp=(temp-32)*(5/9)+273.15
elif (unitFrom == "Celsius"):
    if(unitTo=="Fahrenheit"):
        temp=(temp*(9/5))+32
    elif (unitTo == "Celsius"):
        temp = temp
    else:
        temp=temp+273.15
else:
    if(unitTo=="Celsius"):
        temp=temp-273.15
    elif (unitTo == "Kelvin"):
        temp = temp
    else:
        temp=(temp-273.15)*(9/5)+32
print(f"That is {temp:.1f} degrees {unitTo}.")