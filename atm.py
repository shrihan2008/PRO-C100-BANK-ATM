money=10000

class  Atm:
    def __init__(self,cardno,pinno) :
        self.cardno=cardno
        self.pinno=pinno
    def cash(self):
       print("Money for cash withdrawl")
       nemMoney=money-5000
       print("Money after Withdrawl is",nemMoney)   
    def cash1(self):
       print("Pin Number")
    def balance(self):
        print(money)
atm=Atm("1000","1")
print(atm.cash())      
print(atm.cash1())    
print(atm.balance())    