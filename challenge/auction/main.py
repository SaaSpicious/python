import art

print(art.logo)
print("--- This is the secret auction program ---")

feedback = ("yes")

bid_dict={}

while feedback == "yes":
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bid_dict[name]=bid
    feedback = input("Are there any other bidders? (yes/no) ")

highest_bidder=art.find_highest_bid(bid_dict)

print(f"The highest bidder is {highest_bidder["name"]} with a bid of ${highest_bidder["bid"]}!")

