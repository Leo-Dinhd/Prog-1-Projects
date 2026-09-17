import p1_random as p1
rng = p1.P1Random()

gameNumber, playerWins, dealerWins, gamesTied = 1, 0, 0, 0
inProgress = True

while inProgress:

    print(f"START GAME #{gameNumber}")
    print("")
    card = rng.next_int(13) + 1  # [0,12]

    if card <= 10:
        hand = card
    else:
        hand = 10

    if card == 1:
        print(f"Your card is a ACE!")
    elif card == 11:
        print(f"Your card is a JACK!")
    elif card == 12:
        print(f"Your card is a QUEEN!")
    elif card == 13:
        print(f"Your card is a KING!")
    else:
        print(f"Your card is a {card}!")
    print(f"Your hand is: {hand}")

    while True:
        print("")
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")
        print("")
        choice = int(input("Choose an option: "))


        if choice == 1:
            print("")
            card = rng.next_int(13) + 1
            if card == 1:
                hand += 1
                print(f"Your card is a ACE!")
                print(f"Your hand is: {hand}")
            elif 2 <= card <= 10:
                hand += card
                print(f"Your card is a {card}!")
                print(f"Your hand is: {hand}")
            elif card == 11:
                hand += 10
                print(f"Your card is a JACK!")
                print(f"Your hand is: {hand}")
            elif card == 12:
                hand += 10
                print(f"Your card is a QUEEN!")
                print(f"Your hand is: {hand}")
            elif card == 13:
                hand += 10
                print(f"Your card is a KING!")
                print(f"Your hand is: {hand}")

            if hand == 21:
                playerWins += 1
                print("")
                print("BLACKJACK! You win!")
                print("")
                gameNumber += 1
                break
            elif hand > 21:
                dealerWins += 1
                print("Dealer Wins")
                gameNumber += 1
                break
        elif choice == 2:
            print("")
            # dealer's draw
            dealersHand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealersHand}")
            print(f"Your hand is: {hand}")
            print("")
            if dealersHand == 21:
                dealerWins += 1
                print("Dealer wins!")
                print("")
                gameNumber += 1
                break
            elif dealersHand > 21:
                playerWins += 1
                print("You win!")
                print("")
                gameNumber += 1
                break
            elif hand == dealersHand:
                gamesTied += 1
                print("It's a tie! No one wins!")
                print("")
                gameNumber += 1
                break
            elif hand > dealersHand:
                playerWins += 1
                print("You win!")
                gameNumber += 1
                break
            elif dealersHand > hand:
                dealerWins += 1
                print("Dealer wins!")
                print("")
                gameNumber += 1
                break
        elif choice == 3:
            print("")
            # print stats
            gameNumber-=1
            percentagePlayerWins=(playerWins/gameNumber)*100
            float(percentagePlayerWins)
            print(f"Number of Player wins: {playerWins}")
            print(f"Number of Dealer wins: {dealerWins}")
            print(f"Number of tie games: {gamesTied}")
            print(f"Total # of games played is: {gameNumber}")
            print(f"Percentage of Player wins: {percentagePlayerWins:.1f}%")

        elif choice == 4:
            print("")
            inProgress = False
            break
        else:
            print("")
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
