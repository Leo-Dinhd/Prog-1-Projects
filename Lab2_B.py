income=float(input("Enter your total income this year:"))
totalTax=0
temp1,temp2,temp3,temp4,temp5,temp6,temp7=0,0,0,0,0,0,0
if(income>609350):
    temp1=income-609350
    totalTax+=temp1*.37
    income=609350
if(income>243725):
    temp2=income-243725
    totalTax+=temp2*.35
    income = 243725
if(income>191950):
    temp3=income-191950
    totalTax+=temp3*.32
    income = 191950
if(income>100525):
    temp4=income-100525
    totalTax+=temp4*.24
    income = 100525
if(income>47150):
    temp5=income-47150
    totalTax+=temp5*.22
    income = 47150
if(income>11600):
    temp6=income-11600
    totalTax+=temp6*.12
    income = 11600
if(income>0):
    totalTax+=income*.10

print(f"You owe ${totalTax:.2f} this year.")
