#Author: Alexander Christopher
#3/30/20
import random

suits = ['Clubs','Diamonds','Hearts','Spades']

ranks = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight',
         'Seven', 'Six', 'Five', 'Four', 'Three', 'Two']

types = ['Straight Flush','Four of a Kind','Full House','Flush',
         'Straight','Three of a Kind','Two Pair','Pair','High Card']

def player1():
    deck = createDeck()
    hand = count_hand(deck)
    counts = rank_counter(hand)
    cs = contains_straight(counts, hand)
    suit = suit_set(hand)
    letters = print_hand(hand)
    rank = evaluate(cs, counts, suits, hand)
    ranking = print_rank(cs, counts, suit, hand)
    return letters, ranking, rank

def player2():
    deck = createDeck()
    hand = count_hand(deck)
    counts = rank_counter(hand)
    cs = contains_straight(counts, hand)
    suit = suit_set(hand)
    letters = print_hand(hand)
    rank = evaluate(cs, counts, suits, hand)
    ranking = print_rank(cs, counts, suit, hand)
    return letters, ranking, rank
   
def createDeck():
    deck = []
    for i in range(13):
        for x in range(4):
            deck.append((i, x))        
    random.shuffle(deck)
    return deck

def count_hand(deck):
    hand = []
    for i in range(5):
        hand.append(deck[i])
    sortedHand = sort_hand(hand)
    return sortedHand

def sort_hand(hand):
    length = len(hand)
    for i in range(0, length):
        for x in range(0, length-i-1):
            if (hand[x][0] > hand[x + 1][0]):
                place = hand[x]
                hand[x] = hand[x + 1]
                hand[x + 1] = place        
    return hand
    
def suit_set(hand):
    suits = [[],[],[],[]]
    answer = []
    for i in range(len(hand)):
        value = hand[i]
        if hand[i][1] == 0:
            clubs = suits[0]
            clubs.append(value)
        elif hand[i][1] == 1:
            diamonds = suits[1]
            diamonds.append(value)
        elif hand[i][1] == 2:
            hearts = suits[2]
            hearts.append(value)
        elif hand[i][1] == 3:
            spades = suits[3]
            spades.append(value)
    for i in range(len(suits)):
        if i == 0:
            answer.append(len(suits[0]))
        elif i == 1:
            answer.append(len(suits[1]))
        elif i == 2:
            answer.append(len(suits[2]))
        elif i == 3:
            answer.append(len(suits[3]))
    return answer

def rank_counter(hand):
    counts = [0]*13
    saved = []
    for i in range(len(hand)):
        ii = hand[i][0]
        if ii not in saved:
            saved.append(ii)
            counts[ii] = 1
        else:
            if ii in saved:
                counts[ii] +=1
    return counts
    
def contains_straight(counts, hand):
    count = 0
    for i in range(len(counts)):
        if counts[i] == 1:
            count +=1
        else:
            if counts[i] > 1:
                return False
            elif count > 0 and count != len(hand):
                return False               
    if count == len(hand):
        return True
    else:
        return False

def evaluate(cs, counts, suits, hand):
    findRank = []
    if cs == True:
        if 5 in suits:
            handType = types.index('Straight Flush')
            highestCard = hand[0][0]
            return highestCard, handType
        else:
            handType = types.index('Straight')
            highestCard = hand[0][0]
            return highestCard, handType
    elif 4 in counts:
        find = counts.index(4)
        handType = types.index('Four of a Kind')
        for i in range(len(hand)):
            if hand[i][0] == find:
                highestCard = hand[i][0]
                return highestCard, handType
    elif 3 in counts and 2 in counts:
        handType = types.index('Full House')
        find = counts.index(3)
        for i in range(len(hand)):
            if hand[i][0] == find:
                highestCard = hand[i][0]
                return highestCard, handType
    elif 5 in suits:
        handType = types.index('Flush')
        highestCard = hand[0][0]
        return highestCard, handType
    elif 3 in counts and 1 in counts:
        handType = types.index('Three of a Kind')
        find = counts.index(3)
        for i in range(len(hand)):
            if hand[i][0] == find:
                highestCard = hand[i][0]
                return highestCard, handType
    elif 2 in counts:
        count = 0
        for i in range(len(counts)):
            if counts[i] == 2:
                count +=1
        find = counts.index(2)
        if count == 2:
            handType = types.index('Two Pair')
            for i in range(len(hand)):
                if hand[i][0] == find:
                    highestCard = hand[i][0]
                    return highestCard, handType
        if count == 1:
            handType = types.index('Pair')
            for i in range(len(hand)):
                if hand[i][0] == find:
                    highestCard = hand[i][0]
                    return highestCard, handType
    elif 1 in counts:
        handType = types.index('High Card')
        highestCard = hand[0][0]
        return highestCard, handType

def print_hand(hand):
    printHand = []
    numbers = [9,8,7,6,5,4,3,2]
    for i in range(len(hand)):
        find = hand[i]
        for x in range(len(find)):
            if x == 0:
                rank = hand[i][0]
                if rank < 5:
                    ranking = ranks[rank][0]
                else:
                    position = ranks[rank]
                    index = ranks.index(position)
                    numberIndex = index - 5
                    giveNumber = numbers[numberIndex]
                    ranking = giveNumber
            if x == 1:
                suit = hand[i][1]
                suitAnswer = suits[suit][0]
        add = str(ranking) + str(suitAnswer)
        printHand.append(add)
    newHand = ' '.join(printHand)[:]
    return newHand
    
def print_rank(cs, counts, suits, hand):
    defineRank = evaluate(cs, counts, suits, hand)
    returnValue = types[defineRank[1]]
    highestCard = ranks[defineRank[0]]
    return f"{returnValue} {highestCard} high"

def winning_hand():
    hand1 = player1()
    hand2 = player2()
    if hand1[2][1] == hand2[2][1]:
        if hand1[2][0] == hand2[2][0]:
            return hand1, hand2, "No winning hand"
        elif hand1[2][0] < hand2[2][0]:
            return hand1, hand2, "Hand one wins!"
        elif hand1[2][0] > hand2[2][0]:
            return hand1, hand2, "Hand two wins!"
        
    elif hand1[2][1] < hand2[2][1]:
        return hand1, hand2, "Hand one wins!"
    elif hand1[2][1] > hand2[2][1]:
        return hand1, hand2, "Hand two wins!"
    
def main():
    userInput = int(input("How many games do you want to play? "))
    for i in range(userInput):
        final = winning_hand()
        hand1 = final[0]
        hand2 = final[1]
        winner = final[2]
        print(hand1[0] + ' ' + hand1[1])
        print(hand2[0] + ' ' + hand2[1])
        print(winner)
        print("")

if __name__ == "__main__":
    main()

