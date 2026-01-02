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

def sort_cards(final_cards):
    #insertion sort to not interfere with suites
    sorted_cards = []
    for rank in numbers:
            for card in final_cards:
                if rank in card:
                    sorted_cards.append(card)
    return sorted_cards

def check_pair(final_cards):
    pair_count = 0
    for x in numbers:
        for y in final_cards:
            if x in y:
                pair_count += 1
                if (pair_count == 2):
                    return 1
        pair_count = 0
    return 0

def check_two_pair(final_cards):
    pair_count  = 0
    pairs_count = 0
    for x in numbers:
        for y in final_cards:
            if x in y:
                pair_count += 1
                if (pair_count == 2):
                    pairs_count += 1
                    if(pairs_count == 2):
                        print("There is a two pair present")
                        return 2
        pair_count = 0
    return 0

def check_three(final_cards):
    pair_count = 0
    for x in numbers:
        for y in final_cards:
            if x in y:
                pair_count += 1
                if (pair_count == 3):
                    print("There is a three of a kind present")
                    return 3
        pair_count = 0
    return 0

def check_flush(final_cards):
    flush = 0
    for x in suites:
        for y in final_cards:
            if x in y:
                flush += 1
                if (flush == 5):
                    print("Flush is present")
                    return 1
        flush = 0
    return 0

def check_fullHouse(final_cards):
    check_three(final_cards)
    check_pair(final_cards)
#set up cards

suites = ["♠", "♦", "♣", "♥"]
numbers = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

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
    hand = sort_cards(hand + commu_cards)
    print(hand)
    msvcrt.getch()
    hand = []
    drawn = []
    commu_cards = []
    player_cards = []