from Auction_art import logo
print(logo)

bidders_and_values = {}

def find_highest_bidder(bidders_and_values):
    winner = ''
    highest_bid = 0
    for bidder in bidders_and_values:
        bid_amount = bidders_and_values[bidder]
        if bid_amount >highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

more_bids = True
while more_bids:

    participant = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    bidders_and_values[participant] = bid

    carry_on = input("Are there any more bidders?: Type 'yes' or 'no'").lower()

    if carry_on == 'no':
        more_bids = False
        find_highest_bidder(bidders_and_values)
    elif carry_on == 'yes':
        print("\n" *20)

