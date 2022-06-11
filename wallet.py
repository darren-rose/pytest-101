class InsufficientAmount(Exception):
    pass

class Wallet(object):
    def __init__(self, amount=0):
      self.balance = amount

    def spend_cash(self, amount):
      if self.balance < amount:
        raise InsufficientAmount('balance too low')
      self.balance -= amount

    def add_cash(self, amount):
      self.balance += amount


