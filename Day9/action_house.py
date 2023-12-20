from art import logo
from clear import clear

print(logo)
print("Welcome to the action house game. ")

bids = {}

def auction_house(plain_name, plain_bid):
    bids[plain_name] = plain_bid

def auction_winner():
    amount = 0
    winner = ""
    for key in bids:
        if bids[key] > amount:
            amount = bids[key]
            winner = key
    print(f"The user {winner} with an amount of {amount}$ won the bid")
    
 
flag = True 
while flag:
    name = input("Please give us your name: ")
    bid = int(input("Please provide your bid: "))
    auction_house(plain_name=name, plain_bid=bid)
    other_player = input("Are there any other bidders? Press Y is there are. Otherwise type N. ")
    if other_player.lower() == "y":
        clear()
        auction_house(plain_name=name, plain_bid=bid)
    else:
        flag = False

auction_winner()
