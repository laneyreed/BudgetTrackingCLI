# 📚 Category Model

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