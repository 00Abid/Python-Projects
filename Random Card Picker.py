import random
cards = ["Daimonds" , "Spades" , "Hearts" , "Clubs"]
ranks = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , "Jack" , "Queen" , "King" , "Joker" , "Ace" ]

def pick_a_card():
    card = random.choices(cards)
    rank = random.choices(ranks)
    return(f"The {    rank   } of {   card   } ")


print(pick_a_card())
