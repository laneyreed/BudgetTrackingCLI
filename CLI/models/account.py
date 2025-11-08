from datetime import datetime
from utils.constants import AccountType
from models.user import User

class Account:
    """
    Represents a financial account (checking, savings, credit card, cash).
    Tracks balance and transactions associated with the account.
    """

    def __init__(self, name, account_type: AccountType, user_id: User, id, created_at=datetime.now(), balance=0.0):
        """
        Initialize an Account.
        
        Args:
            name (str): Account name (e.g., "Chase Checking", "Wallet Cash")
            account_type (AccountType): Type of account (CHECKING, SAVINGS, etc.)
            balance (float): Current account balance (default: 0.0)
            user_id (User): User who owns this account
            id (int): Account ID (set by database)
            created_at (datetime): When account was created
        """
        self.id = id
        self.user_id = user_id
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.created_at = created_at
    
    # def deposit(self, amount):
    #     """Add money to the account."""
    #     if amount <= 0:
    #         raise ValueError("Deposit amount must be positive")
    #     self.balance += amount
    
    # def withdraw(self, amount):
    #     """Remove money from the account."""
    #     if amount <= 0:
    #         raise ValueError("Withdrawal amount must be positive")
    #     if amount > self.balance:
    #         raise ValueError("Insufficient funds")
    #     self.balance -= amount
    
    # def update_balance(self, amount, is_income=True):
    #     """
    #     Update balance based on transaction.
        
    #     Args:
    #         amount (float): Transaction amount
    #         is_income (bool): True for income, False for expense
    #     """
    #     if is_income:
    #         self.deposit(amount)
    #     else:
    #         self.withdraw(amount)
    
    # def __repr__(self):
    #     return f"Account(id={self.id}, name='{self.name}', type={self.account_type.value}, balance=${self.balance:.2f})"
    
    def __str__(self):
        return f"Account Owner: {self.user_id.name}, Account Name: {self.name} {self.account_type.value}, Added On: {self.created_at}, Balance: ${self.balance:.2f}"
    
    # def to_dict(self):
    #     """Convert account to dictionary for database storage."""
    #     return {
    #         'id': self.id,
    #         'user_id': self.user_id,
    #         'name': self.name,
    #         'account_type': self.account_type.value,
    #         'balance': self.balance,
    #         'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
    #     }
    
    # @classmethod
    # def from_dict(cls, data):
    #     """Create Account instance from dictionary (from database)."""
    #     return cls(
    #         id=data.get('id'),
    #         user_id=data.get('user_id'),
    #         name=data['name'],
    #         account_type=AccountType(data['account_type']),
    #         balance=data.get('balance', 0.0),
    #         created_at=datetime.strptime(data['created_at'], '%Y-%m-%d %H:%M:%S') if data.get('created_at') else None
    #     )