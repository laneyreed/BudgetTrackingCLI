# 👤 User Model

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


