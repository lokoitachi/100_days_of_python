from art import logo
from clear import clear

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    """This function will return the winner of the auction house program and will also prompt up their bid. """
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    ask_name = input("Could you kindly tell us your name?: ")
    ask_bid = int(input("Could you kindly tell us your bid?: $"))
    bids[ask_name] = ask_bid
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()






