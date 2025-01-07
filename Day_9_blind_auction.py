logo_gavel = '''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
                      
'''
print(logo_gavel)



def win(bid_dict):
    winner = ""
    highest_bid = 0
    for i in bid_dict:
        bid_amt = bid_dict[i]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bid = {}
other = True
while other:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    continue_auction = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    bid[name] = price

    if continue_auction == "no":
        other = False
        win(bid)
    if continue_auction == "yes":
        print("\n" * 100)

