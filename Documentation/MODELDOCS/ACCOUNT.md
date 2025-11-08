# 💱 Account Model

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