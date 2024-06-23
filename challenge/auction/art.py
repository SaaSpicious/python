logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def find_highest_bid(bid_dict):

    highest_bid={
        "name": "",
        "bid": 0
    }

    for bidder in bid_dict:
        if bid_dict[bidder] > highest_bid["bid"]:
            highest_bid["name"]=bidder
            highest_bid["bid"]=bid_dict[bidder]

    return highest_bid
