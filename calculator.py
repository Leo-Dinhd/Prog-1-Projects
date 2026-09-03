operation=input("Enter the operation: ")
operand1=float(input("Enter the first operand: "))
operand2=float(input("Enter the second operand: "))
if operation == "add":
    total=operand1+operand2
    print(f"Result is {total:.1f}")
elif operation == "sub":
    total = operand1-operand2
    print(f"Result is {total:.1f}")
elif operation == "mul":
    total = operand1 * operand2
    print(f"Result is {total:.1f}")
elif operation == "div":
    total = operand1/operand2
    print(f"Result is {total:.2f}")
