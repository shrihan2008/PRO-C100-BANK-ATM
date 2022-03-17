class  Atm:
    def __init__(self,cardno,pinno) :
        self.cardno=cardno
        self.pinno=pinno
    def cash(self):
       print("Money for cash withdrawl")
    def cash1(self):
       print("Pin Number")
atm=Atm("1000","1")
print(atm.cash())      
print(atm.cash1())    
