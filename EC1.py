print("Available movies today:")
print("A)12 Strong:   1)2:30  2)4:40 3)7:50 4)10:50")
print("B)Coco:        1)12:40 2)3:45")
print("C)The Post:    1)12:45 2)3:35 3)7:05 4)9:55")

movie=input("Movie choice: ")
if (movie=="A"):
    showtime = int(input("Showtime: "))
    if(showtime==1 or showtime==2 or showtime==3 or showtime ==4):
        adult = int(input("Adult tickets: "))
        if(adult>30):
            print("Invalid option; please restart app...")
        else:
            kid = int(input("Kid tickets: "))
            if ((adult + kid) > 30):
                print("Invalid option; please restart app...")
            else:
                cost = (adult * 12.45) + (kid * 9.68)
                print(f"Total cost: ${cost:.2f}")


    else:
        print("Invalid option; please restart app...")

elif (movie=="B"):
    showtime = int(input("Showtime: "))
    if(showtime==1):
        adult = int(input("Adult tickets: "))
        if (adult > 30):
            print("Invalid option; please restart app...")
        else:
            kid = int(input("Kid tickets: "))
            if ((adult + kid) > 30):
                print("Invalid option; please restart app...")
            else:
                cost = (adult * 11.17) + (kid * 8.00)
                print(f"Total cost: ${cost:.2f}")

    elif(showtime==2):
        adult = int(input("Adult tickets: "))
        if (adult > 30):
            print("Invalid option; please restart app...")
        else:
            kid = int(input("Kid tickets: "))
            if ((adult + kid) > 30):
                print("Invalid option; please restart app...")
            else:
                cost = (adult * 12.45) + (kid * 9.68)
                print(f"Total cost: ${cost:.2f}")
    else:
        print("Invalid option; please restart app...")
elif (movie=="C"):
    showtime = int(input("Showtime: "))
    if (showtime == 1):
        adult = int(input("Adult tickets: "))
        if (adult > 30):
            print("Invalid option; please restart app...")
        else:
            kid = int(input("Kid tickets: "))
            if ((adult + kid) > 30):
                print("Invalid option; please restart app...")
            else:
                cost = (adult * 11.17) + (kid * 8.00)
                print(f"Total cost: ${cost:.2f}")

    elif (showtime == 2 or showtime==3 or showtime==4):
        adult = int(input("Adult tickets: "))
        if (adult > 30):
            print("Invalid option; please restart app...")
        else:
            kid = int(input("Kid tickets: "))
            if ((adult + kid) > 30):
                print("Invalid option; please restart app...")
            else:
                cost = (adult * 12.45) + (kid * 9.68)
                print(f"Total cost: ${cost:.2f}")
    else:
        print("Invalid option; please restart app...")
else:
    print("Invalid option; please restart app...")