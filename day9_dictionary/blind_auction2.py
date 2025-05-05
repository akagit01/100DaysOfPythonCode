def highest_bidding(bidding_dictionary):
    highest_bidder=max(bidding_dictionary,key=bidding_dictionary.get)
    highest_bid=bidding_dictionary[highest_bidder]
    print(f'the highest bidder is {highest_bidder} with bid of {highest_bid}')

anymore=True
auctioneers={}

while anymore:
    name=input("what is your name: ")
    bid=int(input("'what's your bid: "))
    auctioneers[name]=bid

    more=input('are there any more bidders? Type y/n: ').lower()
    if more=='n':
        anymore=False
        highest_bidding(auctioneers)






