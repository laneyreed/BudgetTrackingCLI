# 💸 Transaction Model

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