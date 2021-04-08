import unittest

class Account:

    def __init__(self, accountNumber, dateOfOpening, interestRate, oppeningBalance):
        self.accountNumber = accountNumber
        self.dateOfOpening = dateOfOpening
        self.interestRate = interestRate
        self.oppeningBalance = oppeningBalance
    
    def deposit(*args):
        pass

    def withdraw(*args):
        pass

    def transfer(*args,**kwargs):
        pass

a = Account("111222333", "12-12-2012", 0.1, 120.0)
b = Account("222233344", "10-01-2015", 0.2, 100.0)

class Tests(unittest.TestCase):
    

    def test_deposit_with_positive_amount(self):
        result = a.deposit(2)
        self.assertEqual(result, 122)


    def test_deposit_with_negative_amount(self):
        amount = float(-2)
        result = a.deposit(amount)
        self.assertEqual(Exception, result)


    def test_withdraw_with_positive_amount(self):
        amount = 2
        result = a.withdraw(2)
        self.assertEqual(result, 118)


    def test_withdraw_with_negative_amount(self):
        amount = float(-2)
        result = a.withdraw(amount)
        self.assertEqual(Exception, result)


    def test_transfer_when_sending_money(self):
        result = a.transfer(2, b)
        self.assertEqual(result, 118)


    def test_transfer_when_receiving_money(self):
        trasfer = b.transfer(2,a)
        result = a.oppeningBalance
        self.assertEqual(result, 122)


if __name__ == "__main__":
    unittest.main()    