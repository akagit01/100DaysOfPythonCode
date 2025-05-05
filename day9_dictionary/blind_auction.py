def highest_bidding(bidding_dictionary):
    highest_bid=0
    highest_bidder=''
    for bidder in auctioneers:
        if auctioneers[bidder]>highest_bid:
            highest_bid=auctioneers[bidder]
            highest_bidder=bidder
    print(f'the highest bidder is {highest_bidder} with bid of {highest_bid}')

anymore=True
auctioneers={}

while anymore:
    name=input("what is your name: ")
    bid=int(input("'what's your bid: $"))
    auctioneers[name]=bid

    more=input('are there any more bidders? Type y/n: ').lower()
    if more=='n':
        anymore=False
        highest_bidding(auctioneers)
    elif more=='y':
        print("\n" * 10)    #to hide previous bidders value to be displayed to new bidder in console





