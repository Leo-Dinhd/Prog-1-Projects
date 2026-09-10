word1=input("Enter a word: ")
letter1=input("Enter the letter to count: ")
count=0
for i in range(0,len(word1)):
    if(word1[i]==letter1):
        count+=1
print(f"{letter1} appears {count} times.")