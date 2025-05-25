class Account:

    def __init__(self,bal,acc_no):
        self.bal=bal
        self.acc_no=acc_no

    def debit(self,amt):
        cur_bal=self.bal
        self.bal-=amt
        print(f"Rs.{amt} debited from {cur_bal}.Current bal= {self.bal}")

    def credit(self):
        print("account credited")

    def print_bal(self):
        print(self.bal)