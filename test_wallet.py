import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 25'''
    return Wallet(25)

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions_with_empty_wallet(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 45),
    (20, 2, 43),
])
def test_transactions_with_wallet(wallet, earned, spent, expected):
    wallet.add_cash(earned)
    wallet.spend_cash(spent)
    assert wallet.balance == expected
