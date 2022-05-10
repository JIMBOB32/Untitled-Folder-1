import threading
import time
import random

class BankAccount(threading.Thread):
    acct_balance = 100
    def __init__(self, name, money_request):
        threading.Thread.__init__(self)
        self.name = name
        self.money_request = money_request

    def run(self):
        thread_lock.acquire()
        BankAccount.get_money(self)
        thread_lock.release()

    @staticmethod
    def get_money(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name, customer.money_request, time.strftime("%H:%M:%S",time.gmtime())))
            
        if BankAccount.acct_balance - customer.money_request > 0: 
                BankAccount.acct_balance -= customer.money_request
                print("New Account Balance is : ${}".format(BankAccount.acct_balance))
            
        else:
            print("Not Enough Money in Account")
            print("Current Balance is : ${}".format(BankAccount.acct_balance))
        
        time.sleep(3)

thread_lock = threading.Lock()
bob = BankAccount("James", 1)
alice = BankAccount("Alice", 100)
sally = BankAccount("Sally", 50)

bob.start()
alice.start()
sally.start()

bob.join()
alice.join()
sally.join()

