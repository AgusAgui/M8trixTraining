import random
import msvcrt

def draw(drawn, deck):
    repeat = True
    while(repeat):
        repeat = False
        num = random.randint(0,51)
        for x in drawn:
            if (num == x):
                repeat = True
                break
    drawn.append(num) #no real need to shuffle, we can just clear drawn to get a new set of cards
    return deck[num]

#set up cards
suites = {"♠", "♦", "♣", "♥"}
numbers = {"Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"}

deck = []
for x in numbers:
    for y in suites:
        deck.append(y + ' ' + x)

players = int(input("The amount of players are..."))

#print(deck)
drawn = []
hand = []
commu_cards = []
player_cards = []
for x in range(100):
    #pre-flop    
    hand.append(draw(drawn, deck))
    hand.append(draw(drawn, deck))
    for x in range((players - 1)):
        p_hand = []
        p_hand.append(draw(drawn, deck))
        p_hand.append(draw(drawn, deck))
        player_cards.append(p_hand)
    print(hand)
    msvcrt.getch()
    #flop
    for y in range(3):
        commu_cards.append(draw(drawn,deck))
    print(commu_cards)
    #turn
    commu_cards.append(draw(drawn,deck))
    print(commu_cards)
    msvcrt.getch()
    #river
    commu_cards.append(draw(drawn,deck))
    print(commu_cards)
    msvcrt.getch()
    hand = []
    drawn = []
    commu_cards = []
    player_cards = []