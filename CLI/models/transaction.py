from datetime import datetime
from models.category import Category
from models.user import User
from models.account import Account
from utils.constants import TransactionType


class Transaction:
    '''A class to represent a financial transaction.
    
    Attributes:
        id (int): The unique identifier for the transaction.
        transaction_type (TransactionType): The type of the transaction (income or expense).
        category (Category): The category associated with the transaction.
        amount (float): The amount of the transaction.
        date (datetime): The date of the transaction.
        description (str): A description of the transaction.
    '''
    def __init__(self, id: int, user_id: User, account_id: Account, transaction_type: TransactionType, category: Category, amount: float, date: datetime, description: str):
        self.id = id
        self.user_id = user_id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.category = category
        self.amount = amount
        self.date = date or datetime.now()
        self.description = description
        


    def __str__(self):
        return f"Transaction(id={self.id}, User: {self.user_id}, Account: {self.account_id}, category={self.category}, amount={self.amount}, date={self.date}, description={self.description}, transaction_type={self.transaction_type})"
