# Budget Tracker CLI - Features 

### Main CLI Application(`ui/cli.py`)
- User management (create/select users)
- Account management (create/view accounts)
- Transaction tracking (add/view transactions)
- Financial summaries and reports
- Beautiful rich-formatted interface with colors and tables

### Application Runner(`run_cli.py`)
- Handles Python import paths automatically
- Makes running the app easy
- Avoids module import errors\

### Color Guide
**The CLI uses colors to make information easier to scan**

| Color | Meaning |
|-------|---------|
| 🟢 **Green** | Income, positive balances, success messages |
| 🔴 **Red** | Expenses, negative amounts, errors |
| 🔵 **Blue** | Account information, prompts |
| 🟡 **Yellow** | Warnings, prompts for input, net balances |
| 🟣 **Magenta** | Headers, category information |
| 🔵 **Cyan** | Menu options, labels |

### 💾 Data Storage
- In-memory storage
  - Fast and simple
  - No database setup required
- Data stored in Python lists
- Fast and simple
- **Data is lost when you exit the app**

### User Management
- Create new users with name, email, and currency preference
- Select from existing users
- Switch between users
- Each user has isolated financial data

### Account Management
- Create accounts with types: Checking, Savings, Credit Card, Cash
- Set initial balance
- View all accounts with balances
- Calculate total balance across accounts

### Transaction Tracking
- Add income transactions
- Add expense transactions
- Categorize with default categories
- Automatic balance updates
- Add descriptions to transactions
- Timestamp all transactions

### Financial Reports
- View all transactions in table format
- Sort by date (newest first)
- Color-coded amounts (green for income, red for expenses)
- Financial summary dashboard:
  - Total income
  - Total expenses
  - Net balance
  - Account balances
  - Transaction counts
- Expense breakdown by category with percentages

### User Interface
- Color-coded interface using Rich library
- Clear menu navigation
- Interactive prompts
- Beautiful tables and panels
- Input validation
- Error handling

