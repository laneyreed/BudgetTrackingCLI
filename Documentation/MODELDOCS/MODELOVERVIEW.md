# 💵 Budget Tracker - Data Models

This document describes the core data models used in the Budget Tracker application and their relationships.

## 🧬 Model Overview

**The Budget Tracker uses four main models that work together to track financial data**

1. **[User](./USER.md)** - Represents application users
2. **[Account](./ACCOUNT.md)** - Represents financial accounts owned by users
3. **[Category](./CATEGORY.md)** - Represents transaction categories
4. **[Transaction](./TRANSACTION.md)** - Represents individual financial transactions

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