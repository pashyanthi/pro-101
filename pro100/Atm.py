class Atm(object):
        def __init__(self,cashwithdrawal,balanceenquiry,cardname,cardnumber):
            self.cashwithdrawal=cashwithdrawal
            self.balanceenquiry=balanceenquiry
            self.cardname=cardname
            self.cardnumber=cardnumber
            
def main():
            one=Atm(5000,25000,"debit",12348647)   
            two=Atm(23000,45080,"credit",27896756) 
            print("your withdrawed cash is ",one.cashwithdrawal)
            print("your balance remaining is ",one.balanceenquiry)
            print("your type of card is ",one.cardname)
            print("your card number is ",one.cardnumber)
            print("your withdrawed cash is ",two.cashwithdrawal)
            print("your balance remaining is ",two.balanceenquiry)
            print("your type of card is ",two.cardname) 
            print("your card number is ",one.cardnumber)
            
main()




