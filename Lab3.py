import math

runningTotal = 0
currentResult = 0.0
sum = 0.0
count = 0
result = 0
menuSelection = 1
validSelection = "yes"
print(f"Current Result: {currentResult}")
print("")

while menuSelection != 0:
    if validSelection != "no":
        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")
        print("")

    validSelection = "yes"
    menuSelection = int(input("Enter Menu Selection: "))

    if menuSelection == 0:
        break
    elif menuSelection == 1:
        count += 1

        firstOperand = input("Enter first operand: ")
        if firstOperand == "RESULT":
            firstOperand = currentResult
        else:
            firstOperand = float(firstOperand)
        secondOperand = input("Enter second operand: ")
        if secondOperand == "RESULT":
            secondOperand = currentResult
        else:
            secondOperand = float(secondOperand)

        currentResult = firstOperand + secondOperand
        sum += currentResult
        print(f"Current Result: {currentResult}")
        print("")
    elif menuSelection == 2:
        count += 1
        firstOperand = input("Enter first operand: ")
        if firstOperand == "RESULT":
            firstOperand = currentResult
        else:
            firstOperand = float(firstOperand)
        secondOperand = input("Enter second operand: ")
        if secondOperand == "RESULT":
            secondOperand = currentResult
        else:
            secondOperand = float(secondOperand)

        currentResult = firstOperand - secondOperand
        sum += currentResult
        print(f"Current Result: {currentResult}")
        print("")
    elif menuSelection == 3:
        count += 1
        firstOperand = input("Enter first operand: ")
        if firstOperand == "RESULT":
            firstOperand = currentResult
        else:
            firstOperand = float(firstOperand)
        secondOperand = input("Enter second operand: ")
        if secondOperand == "RESULT":
            secondOperand = currentResult
        else:
            secondOperand = float(secondOperand)

        currentResult = firstOperand * secondOperand
        sum += currentResult
        print(f"Current Result: {currentResult}")
        print("")
    elif menuSelection == 4:
        count += 1
        firstOperand = input("Enter first operand: ")
        if firstOperand == "RESULT":
            firstOperand = currentResult
        else:
            firstOperand = float(firstOperand)
        secondOperand = input("Enter second operand: ")
        if secondOperand == "RESULT":
            secondOperand = currentResult
        else:
            secondOperand = float(secondOperand)

        currentResult = firstOperand / secondOperand
        sum += currentResult
        print(f"Current Result: {currentResult}")
        print("")
    elif menuSelection == 5:
        count += 1
        firstOperand = input("Enter first operand: ")
        if firstOperand == "RESULT":
            firstOperand = currentResult
        else:
            firstOperand = float(firstOperand)
        secondOperand = input("Enter second operand: ")
        if secondOperand == "RESULT":
            secondOperand = currentResult
        else:
            secondOperand = float(secondOperand)

        currentResult = firstOperand ** secondOperand
        sum += currentResult
        print(f"Current Result: {currentResult}")
        print("")
    elif menuSelection == 6:
        count += 1
        firstOperand = input("Enter first operand: ")
        if firstOperand == "RESULT":
            firstOperand = currentResult
        else:
            firstOperand = float(firstOperand)
        secondOperand = input("Enter second operand: ")
        if secondOperand == "RESULT":
            secondOperand = currentResult
        else:
            secondOperand = float(secondOperand)

        currentResult = math.log(secondOperand, firstOperand)
        sum += currentResult
        print(f"Current Result: {currentResult}")
        print("")
    elif menuSelection == 7:
        if count != 0:
            print(f"Sum of calculations: {sum:.2f}")
            count = int(count)
            print(f"Number of calculations: {count}")
            print(f"Average of calculations: {(sum / count):.2f}")
            print("")
            validSelection = "no"
        else:
            validSelection = "no"
            print("Error: No calculations yet to average!")
            print("")
    else:
        validSelection = "no"
        print("Error: Invalid selection!")
        print("")
print("Thanks for using this calculator. Goodbye!")

