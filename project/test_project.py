import pytest
from io import StringIO
import os

# Assuming all functions are in a file named Bank.py
from project import add_account, show_balance, deposit_money, withdraw_money, transfer_money

@pytest.fixture
def setup_customers_file():
    """Create a sample customers.txt file before each test and remove it after."""
    with open("customers.txt", "w") as f:
        f.write("Alice,123,1000\nBob,456,500\nCharlie,789,2000\n")
    yield
    os.remove("customers.txt")

def test_add_account(monkeypatch, setup_customers_file):
    inputs = iter(["David", "999", "3000"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_account()

    with open("customers.txt", "r") as file:
        lines = file.readlines()

    assert "David,999,3000\n" in lines

def test_show_balance(monkeypatch, capsys, setup_customers_file):
    monkeypatch.setattr("builtins.input", lambda _: "123")
    show_balance()
    captured = capsys.readouterr()
    assert "Name: Alice" in captured.out
    assert "Balance: 1000" in captured.out

def test_deposit_money(monkeypatch, setup_customers_file):
    inputs = iter(["123", "500"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    deposit_money()

    with open("customers.txt", "r") as file:
        lines = file.readlines()

    assert "Alice,123,1500\n" in lines

def test_withdraw_money(monkeypatch, setup_customers_file):
    inputs = iter(["123", "300"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    withdraw_money()

    with open("customers.txt", "r") as file:
        lines = file.readlines()

    assert "Alice,123,700\n" in lines

def test_transfer_money(monkeypatch, setup_customers_file):
    inputs = iter(["123", "456", "200"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    transfer_money()

    with open("customers.txt", "r") as file:
        lines = file.readlines()

    assert "Alice,123,800\n" in lines
    assert "Bob,456,700\n" in lines
