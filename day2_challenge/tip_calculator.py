print("Welcome to the tip calculator")
bill=float(input("what was the total bill? $"))
tip=int(input("what % tip would you like to give? 10, 12, 15: "))
percent_tip=(tip/100)*bill
total_bill=bill+percent_tip
people=float(input("how many people to split the bill? "))
each_person_share=round(total_bill/people,2)
print(f"each person should pay: ${each_person_share}")
