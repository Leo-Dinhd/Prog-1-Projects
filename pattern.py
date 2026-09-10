height=int(input("Height: "))
output=""
for i in range(1,height+1):
    for j in range(0,height-i):
        print(".",end="")
    for k in range(1,i+1):
        print(k,end="")
    print()