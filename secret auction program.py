name = input("what is name")
price = int(input("what is your bid?"))
bids ={}
bids[name] = price

should_continue = input("are there any other bid?").lower()

def find_highest_bid(bids):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the lucky winner is{winner} with a bid of {highest_bid}")

continue_bidding = True

while continue_bidding:
    name = input("what is name")
    price = int(input("what is your bid?"))
    bids[name] = price
    should_continue = input("are there any other bid?").lower()
    if should_continue == "no":
        find_highest_bid(bids)
        continue_bidding = False
    elif should_continue == "yes":
        print("\n" *20)

