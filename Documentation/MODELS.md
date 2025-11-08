# 💵 Budget Tracker - Data Models

This document describes the core data models used in the Budget Tracker application and their relationships.

## 🧬 Model Overview

**The Budget Tracker uses four main models that work together to track financial data**

1. **User** - Represents application users
2. **Account** - Represents financial accounts owned by users
3. **Category** - Represents transaction categories
4. **Transaction** - Represents individual financial transactions

## ⚙️ Model Relationships
- A **User** can have multiple **Accounts** (one-to-many)
- A **User** can have multiple **Transactions** (one-to-many)
- Each **Transaction** belongs to one **Account** (many-to-one)
- Each **Transaction** belongs to one **Category** (many-to-one)

```
User (1) 
  |──────< (Many) Account
  │
  └──────< (Many) Transaction
                    ├─────< (1) Account
                    └─────< (1) Category
```

## 📡 Data Flow 
**The transaction links together:**
- The **user** who made the purchase
- The **account** the money came from
- The **category** for classification
- All **transaction** details (amount, date, description)


## 👤 User Model

**Location:** `models/user.py`

**Represents a user of the budget tracker application and stores user profile information and preferences.**

### 🧪 Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | int | Unique identifier for the user |
| `name` | str | User's full name |
| `email` | str | User's email address |
| `currency` | str | User's preferred currency (default: "USD") |
| `created_at` | datetime | Timestamp when the user account was created |

<!-- ### 🔑 Key Features:
- Stores user profile and preferences
- Tracks preferred currency for display purposes
- Foundation for all user-specific financial data -->

### Create User Example
```python
from models.user import User

user = User(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    currency="USD"
)
```



## 💱 Account Model

**Location:** `models/account.py`

**Represents a financial account (checking, savings, credit card, cash) owned by a user.**

### 🧪 Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | int | Unique identifier for the account |
| `user_id` | User | Reference to the User who owns this account |
| `name` | str | Account name (e.g., "Chase Checking", "Wallet Cash") |
| `account_type` | AccountType | Type of account (CHECKING, SAVINGS, CREDIT_CARD, CASH) |
| `balance` | float | Current account balance (default: 0.0) |
| `created_at` | datetime | Timestamp when the account was created |

### 🏦 Account Types
**From `utils/constants.py`**
- `AccountType.CHECKING` - Checking account
- `AccountType.SAVINGS` - Savings account
- `AccountType.CREDIT_CARD` - Credit card account
- `AccountType.CASH` - Cash/wallet

### ⚙️ Relationships
- **Belongs to:** One User (via `user_id`)
- **Has many:** Transactions (transactions reference this account)

### Create Account Example
```python
from models.account import Account
from models.user import User
from utils.constants import AccountType

user = User(id=1, name="John Doe", email="john@example.com")

account = Account(
    id=1,
    user_id=user,
    name="Main Checking",
    account_type=AccountType.CHECKING,
    balance=1000.00
)
```

---

## 📚 Category Model

**Location:** `models/category.py`

**Represents a financial category used to classify transactions.**

### 🧪 Attributes:
| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | int | Unique identifier for the category |
| `name` | str | Category name (must be from default categories) |
| `description` | str | Optional description of the category (default: "") |

### 🌚Default Categories
**From `utils/constants.py`**

**Expense Categories:**
- Groceries
- Rent
- Utilities
- Transportation
- Entertainment
- Healthcare
- Other

**Income Categories:**
- Salary
- Freelance
- Investment
- Gift
- Other

### 🗹 Validation:
- Category names must be from the predefined lists in `DEFAULT_EXPENSE_CATEGORIES` or `DEFAULT_INCOME_CATEGORIES`
- Raises `ValueError` if an invalid category name is provided

### Create Category Example:
```python
from models.category import Category

category = Category(
    id=1,
    name="Groceries",
    description="Food and household supplies"
)
```

---

## 💸 Transaction Model

**Location:** `models/transaction.py`

Represents an individual financial transaction (income or expense).

### 🧪 Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | int | Unique identifier for the transaction |
| `user_id` | User | Reference to the User who made the transaction |
| `account_id` | Account | Reference to the Account associated with the transaction |
| `transaction_type` | TransactionType | Type of transaction (INCOME or EXPENSE) |
| `category` | Category | Category classification for the transaction |
| `amount` | float | Transaction amount (positive value) |
| `date` | datetime | Date/time of the transaction (defaults to current time) |
| `description` | str | Description or notes about the transaction |

### 💱 Transaction Types:
From `utils/constants.py`:
- `TransactionType.INCOME` - Money coming in
- `TransactionType.EXPENSE` - Money going out

### ⚙️ Relationships:
- **Belongs to:** One User (via `user_id`)
- **Belongs to:** One Account (via `account_id`)
- **Belongs to:** One Category (via `category`)

### Create Transaction Example:
```python
from datetime import datetime
from models.transaction import Transaction
from models.user import User
from models.account import Account
from models.category import Category
from utils.constants import TransactionType

user = User(id=1, name="John Doe", email="john@example.com")
account = Account(id=1, user_id=user, name="Checking", account_type=AccountType.CHECKING, balance=1000)
category = Category(id=1, name="Salary")

transaction = Transaction(
    id=1,
    user_id=user,
    account_id=account,
    transaction_type=TransactionType.INCOME,
    category=category,
    amount=5000.00,
    date=datetime.now(),
    description="Monthly salary deposit"
)
```

## 🖼️ Design Notes

1. **User → Account (One-to-Many):** Users can have multiple bank accounts, credit cards, and cash holdings

2. **User → Transaction (One-to-Many):** All transactions are tied to a specific user for data isolation and reporting

3. **Account → Transaction (One-to-Many):** Transactions must specify which account was used, allowing for per-account balance tracking

4. **Category → Transaction (One-to-Many):** Categories allow for transaction classification and budget analysis

### 🎟️ Future Considerations

- add a Budget model to track spending limits per category
- may need to add Transaction → Account relationship validation to ensure the account belongs to the transaction's user
- add support for transfers between accounts (special transaction type)
- support custom user-defined categories beyond the defaults