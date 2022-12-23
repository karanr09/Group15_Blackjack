from random import * #this will allow us to pull random cards
#we set up variables we will need in the code.
total = 0
total_dealer = 0
bet = 0
money = 0
play_again = 1
rules = " "
cards = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

#creating a function which returns the value of a received card
def value_card(card) : 
    value = card
    if (card > 10) :
        value = 10
    return value

print("Welcome to BlackJack !\n")



#RULES OF BLACKJACK - we give the player the option to read the rules
while True:
    rules = input("Do you want to read the rules of this special Blackjack, yes or no ? ")
    if rules == "yes": 
        print("\nBlackjack is a betting game between a player and a dealer. For our game these are the rules we used. \n\nIn the card game of blackjack, the objective is to get as near to 21 as you can without going over (busting). The players are dealt standard cards which have the following value: \n\nAce: 1 or 11 depending on the player \n2 through 10: Face value \nKing, Queen, and Jack: 10\n\nEach player and the dealer are dealt two cards at the start of the game. One of the dealer's cards is dealt face down, while the player's cards are dealt face up. The player's goal is to out-handicap the dealer by having a hand worth that is higher while staying under 21. \n\nThe option to hit (draw another card) or stand is given to the player (keep their current hand value). If a player hits and their hand totals more than 21, the round is over for them (bust). The dealer's turn starts if the player decides to stand.\n\nIf the dealer's hand value is less than 17, they must hit; if it is 17 or more, they must stand. The player wins the round if the dealer busts. The dealer wins the round if she or he stands and has a better hand value than the player. The round ends in a tie if both the player and the dealer have the same hand value.\n\nWe hope the rules are clear, enjoy the game!")
        print("*"*50)
        break
    if rules == "no":
        break
    
#we start by asking the player how much money he has, he must have between $100 and $1000 to sit at the table.
while True :
    try:
        money = int(input("To join this table, you must have between $100 and $1000, how much do you have ? "))
        #if the player doesn't respecting the prerequisites the program asks again
        if int(money) <= 1000 and int(money) >= 100 :
            break
        else:
            print("This  input is not valid, please try again. ")
    except ValueError:
        print("This  input is not valid, please try again. ")
        continue

#main code 
while play_again == 1 :
    while money > 0 :
        while play_again == 1 :
            
                while True :
                    try:
                        bet = int(input("\nYou have " + str(money) + " dollars. How much do you wish to bet? "))
                        if int(bet) <= int(money) and int(bet) > 0 :
                                break
                        else:
                            print("Please provide a valid number, within your budget")
                    except ValueError:
                        print("Please provide a valid number, within your budget")
                        continue

                #drawing player's first and second card   
                #we use the randint function to pick a random element in our cards list. 
                card1 = randint(1,len(cards))
                name_card_1 = cards[card1-1]
                value_card1 = value_card(card1)
                #we print the value of the card, if it's an Ace, we print 1 or 11
                if card1 != 1 :
                    print("\nYou received : " + str(name_card_1) + " - this card has a value of " + str(value_card1))
                else :
                    print("\nYou received : " + str(name_card_1) + " - this card has a value of " + str(value_card1) + " or of 11")
                #repeat for second card   
                card2 = randint(1,len(cards))
                name_card_2 = cards[card2-1]
                value_card2 = value_card(card2)
                if card2 != 1 :
                    print("You received : " + str(name_card_2) + " - this card has a value of " + str(value_card2))
                else :
                    print("You received : " + str(name_card_2) + " - this card has a value of " + str(value_card2) + " or of 11")

                #If the first or the second card are Aces, the player can choose their values. 
                if card1 == 1 :
                    while True :
                        value_card1 = int(input("What value do you wish to attribute to the Ace, 1 or 11 ? "))
                        if value_card1 == 1 or value_card1 == 11 :
                             break
        
                if card2 == 1 :
                        while True :
                            value_card2 = int(input("What value do you wish to attribute to the Ace, 1 or 11 ? "))
                            if value_card2 == 1 or value_card2 == 11 :
                                break
                #Sum of value of the player's card
                total = int(value_card1) + int(value_card2)
                print("\nYou have a total of " +  str(total))

                #card 1 and 2 of the dealer
                card1_dealer = randint(1,len(cards))
                name_card_1d = cards[card1_dealer -1]
                value_card1_dealer = value_card(card1_dealer)
                if card1_dealer == 1 :
                        value_card1_dealer = 11
                print("\nThe dealer received : " + str(name_card_1d) + " this card has a value of " + str(value_card1_dealer))
                total_dealer = value_card1_dealer

                card2_dealer = randint(1,len(cards))
                name_card_2d = cards[card2_dealer -1]
                value_card2_dealer = value_card(card2_dealer)
                if card2_dealer == 1 :
                        if value_card1_dealer >= 11 :
                                value_card2_dealer = 1
                        else :
                                value_card2_dealer = 11
               
                #player's part of the game
                while True :
                    #the player wins, so we break out of the loop and do not give him the option to draw again
                    if total == 21 :
                        break
                    else :
                        again = input("\nWould you like to receive another card, yes or no : ")
                        #player's new card
                        if again == "yes" :
                                cardb = randint(1,len(cards))
                                name_card_b = cards[cardb-1]
                                value_cardb = value_card(cardb)
                                #if it isn't an Ace.
                                if cardb != 1 :
                                    print("You received : " + str(name_card_b) + " - this card has a value of " + str(value_cardb))
                                #if it is an Ace
                                else :
                                    print("You received : " + str(name_card_b) + " - this card has a value of " + str(value_cardb) + " or 11")

                                #if it is an Ace, the player has to choose if he wishes to attribute a value of 1 or 11
                                if cardb == 1 :
                                    while True :
                                        value_cardb = int(input("What value do you wish to attribute to the Ace, 1 or 11 ? "))
                                        if value_cardb == 1 or value_cardb == 11 :
                                             break
                                total = total + int(value_cardb)
                                print("\nYou have a total of " +  str(total))

                        #the player loses because his total is higher than 21. 
                        if total > 21 :
                                money = money - bet
                                print("\nYou lost because you have more than 21 ! You now have $" + str(money) + " left")
                                break
                        #if the player doesn't want to play again, it stops the program
                        elif again == "no" :
                            break
                
                #dealer plays
                if total <= 21 :
                    print("\nThe dealers hidden card was : " + str(name_card_2d) + " - this card has a value of " + str(value_card2_dealer))
                    total_dealer = total_dealer + value_card2_dealer
                    print("The dealer has a total of " + str(total_dealer)+ "\n")

                    #the dealer keeps to play if he has less than the player and less than 17
                    while total_dealer < 17 and total_dealer < total :
                                cardXc = randint(1,len(cards))
                                name_card_Xc = cards[cardXc -1]
                                value_card_Xc = value_card(cardXc)
                                if cardXc != 1 :
                                    print("The dealer received : " + str(name_card_Xc) + " - this card has a value of " + str(value_card_Xc))
                                else :
                                    print("The dealer received : " + str(name_card_Xc) + " - this card has a value of " + str(value_card_Xc) + " or of 11")
                                     ####Potentiellement inclure le bout de code des lignes suivantes dans le else en dessus

                                #If the dealer has an Ace, the program has to choose if it has a value of 1 or 11
                                if cardXc == 1 :
                                    if total_dealer >= 11 :
                                        value_card_Xc = 1
                                    else :
                                        value_card_Xc = 11

                                total_dealer = total_dealer + value_card_Xc
                                print("The dealer has a total of " + str(total_dealer)+ "\n")

                    #In this situation, the player wins because 1. the dealer has a hand above 21 or 2. he has more than the dealer 
                    if total_dealer > 21 or total_dealer < total :
                            money = money + bet
                            print("\nYou won ! You now have $" + str(money) + " left")
                            break
                    #if both have same total value, no winner
                    if total_dealer == total :
                            print("It's a draw ! There is no winner, you have $" + str(money) + " left")
                            break
                    #the dealer wins
                    if total_dealer > total and total_dealer <= 21 :
                            money = money - bet
                            print("\nOh no... You have lost, you have $" + str(money) + " left")
                            break
                break
                
                        
        #if the player has enough money he has the option to play again
        if money > 0 : #check if he has enough money
            while True:
                play_again = input("\nWould you like to play again, yes or no ? ")
                if play_again == "yes" :
                    play_again = 1
                    break
                if play_again == "no" :
                   play_again = 0
                   break

        # if the player doesn't want to play anymore
        if play_again == 0 :
            print("\nBye Bye, you have $" + str(money) + " left")
            break
                    

        # if the player hasn't money anymore it finishes the program 
        if money == 0 :
            print("\nYou have no more money, Bye Bye")
            break
        break
    

