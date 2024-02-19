class Mobank:
    #CONSTRUCTOR
    def __init__(self):
        self.balance=0
        self.passcode=""
        self.menu()
     #FUNCTION
    def menu(self):
        user_input =input('''
                         1.Press 1 to Create Passcode
                         2.Press 2 to Deposit
                         3.Press 3 to Fund Transfer
                         4.press 4 to Check Balance
                         ''')
     #C0NDITION
        if user_input=='1':
            self.create_passcode()
        elif user_input=='2':
             self.deposit()                
        elif user_input=='3':
             self.fundtransfer()
        elif user_input=='4':
            self.check_balance()
        else:
            print("Try Again")

    def create_passcode(self):
        self.passcode=input('Enter Your Passcode')
        print("Passcode Set Successfully")
        self.menu()

    def deposit(self):
        text= input("Enter Your Passcode") 
        if text==self.passcode:
            amount=int(input("Enter the Amount"))  
            self.balance=self.balance+amount
            print("Amount Deposited")
        else:
            print("Incorrect Passcode")
        self.menu()
    def fundtransfer(self):
        text=input("Enter Your Passcode")
        if text==self.passcode:
            amount=int(input("Enter the Amount You want to transfer"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Fund Transferred Successfully")

            else:
                print("Insufficient Funds")

        else:
            print("Enter a Valid Passcode")
        self.menu()
    def check_balance(self):
        text=input("Enter Your Passcode")
        if text==self.passcode:
            print(self.balance)
        else:
            print("Incorrect Passcode")
        self.menu()
 
sbi=Mobank() 


















        
