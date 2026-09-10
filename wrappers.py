money=int(input("How much money do you have: "))
count=0
wrappers=0
for i in range(4,money+1,4):
    count+=1
    wrappers+=1
    if(wrappers==3):
        count+=1
        wrappers=1
        continue

print(f"You can purchase {int(count)} candy bars!")