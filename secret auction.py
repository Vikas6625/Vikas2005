import random

def logo():
    pr_logo = '''
                          _____________
                          \ \\        /
                           \)_(      /
                            |"""""""|.-.,.---------.,.-. 
                            |       | | |             | | '-.
                            |       | | |             | |.'-.
                            |_| '-' '---------' '-'--.-.
                            )"""""""(
                           /_\\ _____\
                           
                       .-------------.
                      /_\\_ _ _ _ _ _ \    
    '''
    print(pr_logo)
    

# step-1: ask the user for input
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)


    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"the winner is {winner} with a bid of Rs.{highest_bid}.")

#call the logo
logo()


bids = {}
continue_bidding = True

while continue_bidding:
    name = input("what is your name?: ")
    price = int(input("what is your bid?: "))
    bids[name] = price

    should_continue = input("Are there any other bidders? type 'yes' or 'no' . \n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" *20)


   

