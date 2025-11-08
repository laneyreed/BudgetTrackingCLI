from enum import Enum

class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"

class CategoryType(Enum):
    INCOME = "income"
    EXPENSE = "expense"

class AccountType(Enum):
    CHECKING = "Checking"
    SAVINGS = "Savings"
    CREDIT_CARD = "Credit Card"
    CASH = "Cash"

class BudgetPeriod(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

# Default categories
DEFAULT_EXPENSE_CATEGORIES = [
    "Groceries", "Rent", "Utilities", "Transportation",
    "Entertainment", "Healthcare", "Other"
]

DEFAULT_INCOME_CATEGORIES = [
    "Salary", "Freelance", "Investment", "Gift", "Other"
]

# Date formats
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Currency
DEFAULT_CURRENCY = "USD"