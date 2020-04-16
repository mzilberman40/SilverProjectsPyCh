class Currency:
    def __init__(self, name):
        self.name = name



class Account:
    def __init__(self, currency, balance=0):
        self.currency = currency
        self.balance = balance
