class Account:
    def __init__(self) -> None:
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.balance = 1000
    account.deposit(45)
    print("Balance:", account.balance)
    account.withdraw(23)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()
