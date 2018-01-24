import random
import numpy as np

def playTurn(pSus,pRoom,pWeap):
    randS = random.random()
    randR = random.random()
    randW = random.random()

    susIndex = -1
    while randS>0.0:
        susIndex += 1
        randS -= pSus[susIndex]

    roomIndex = -1
    while randR > 0.0:
        roomIndex += 1
        randR -= pRoom[roomIndex]

    weapIndex = -1
    while randW > 0.0:
        weapIndex += 1
        randW -= pWeap[weapIndex]
    incName = True
    while(incName==True):
        incName = False
        text = input("I make a suggestion:\nSuspect: "+suspects[susIndex]+"\nRoom: "+rooms[roomIndex]+"\nWeapon: "+weapons[weapIndex]+"\nIf it is non of these please type 'n':\n").lower()

        if text == 'n':
            print("Yay baby. I make a accusation:\nSuspect: "+suspects[susIndex]+"\nRoom: ",rooms[roomIndex]+"\nWeapon: "+weapons[weapIndex]+"\nI win:) Hopefully:/")
            exit(0)
        elif text == suspects[susIndex]:
            pSus[susIndex] = 0.0
            pSus /= sum(pSus)
        elif text == rooms[roomIndex]:
            pRoom[roomIndex] = 0.0
            pRoom /= sum(pRoom)
        elif text ==  weapons[weapIndex]:
            pWeap[weapIndex] = 0.0
            pWeap /= sum(pWeap)
        else:
            incName = True
            print("Gulp.. You cannot spell.. What is a " + text + "?")

def suggestionToBot(givenCards):
    searchCards = []
    for i in range(3):
        text = input("Enter card number " + str((i + 1)) + ":\n")
        searchCards.append(text.lower())
    cardMatch = []

    for i in range(3):
        for j in range(len(givenCards)):
            if searchCards[i] == givenCards[j]:
                cardMatch.append(searchCards[i])

    if len(cardMatch) > 0:
        randNum = random.random() * len(cardMatch)
        print("Here is my card: ", cardMatch[int(randNum)])
    else:
        print("I have non of the cards:/")

suspects = ['colonel mustard','miss scarlett','mrs white','reverend green','professor plum','mrs peacock']
rooms = ['ballroom','hall','billiard room','lounge','dinning room','conservatory','kitchen','library','study']
weapons = ['dagger','candlestick','revolver','spanner','lead piping','rope']

#Num players
numPlay = int(input("Enter the number of players(only '2' or '3'):\n"))
cardNum = int(18/numPlay)

#Passive or active player
activePlayer = False
if(input("Should I be a passive or active player? Enter 'p' for passive and 'a' for active:\n").lower()=='a'):
    activePlayer = True

#Enter the bots cards
givenCards = []

pSus = np.ones(6)
pRoom = np.ones(9)
pWeap = np.ones(6)
i = 0
while i < cardNum:
    text = input("Enter card number "+str(i+1)+":\n").lower()
    found = False
    for j in range(6):
        if text == suspects[j]:
            pSus[j] = 0.0
            found = True
            break

        elif text == rooms[j]:
            pRoom[j] = 0.0
            found = True
            break
        elif text == weapons[j]:
            pWeap[j] = 0.0
            found = True
            break
    if not found:
        for j in range(6,9):
            if text == rooms[j]:
                pRoom[j] = 0.0
                found = True
                break


    if found:
        givenCards.append(text)
        i+=1
    else:
        print("Oops! You spelled the card's name wrong.")

pSus /= sum(pSus)
pRoom /= sum(pRoom)
pWeap /= sum(pWeap)

print("pSus: ",pSus)
print("pRoom: ",pRoom)
print("pWeap: ",pWeap)

print("Here is all the computer's cards:\n",givenCards)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPrint spaced...")

print ("Enter 3 cards in a row with an enter between each other")
while(True):
    if activePlayer:
        if input("Type 'p' if it is my turn and 's' if a suggestion is made by another player:\n").lower() == 's':
            suggestionToBot(givenCards)
        else:
            playTurn(pSus,pRoom,pWeap)
            print("pSus: ", pSus)
            print("pRoom: ", pRoom)
            print("pWeap: ", pWeap)
    else:
        suggestionToBot(givenCards)
