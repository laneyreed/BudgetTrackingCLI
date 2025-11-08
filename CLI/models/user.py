from datetime import datetime

class User:
    """
    Represents a user of the budget tracker application.
    Stores user profile information and preferences.
    """
    
    def __init__(self, id: int, name: str, email: str, created_at=datetime.now(), currency="USD"):
        """
        Initialize a User.
        
        Args:
            name (str): User's full name
            email (str): User's email address
            id (int): User ID (set by database)
            created_at (datetime): When user account was created
            currency (str): User's preferred currency (default: USD)
        """
        self.id = id
        self.name = name
        self.email = email
        self.currency = currency
        self.created_at = created_at 
    
    # def update_name(self, new_name):
    #     """Update user's name."""
    #     if not new_name or not new_name.strip():
    #         raise ValueError("Name cannot be empty")
    #     self.name = new_name.strip()
    
    # def update_email(self, new_email):
    #     """Update user's email."""
    #     if new_email and '@' not in new_email:
    #         raise ValueError("Invalid email format")
    #     self.email = new_email
    
    # def update_currency(self, new_currency):
    #     """Update user's preferred currency."""
    #     if not new_currency or len(new_currency) != 3:
    #         raise ValueError("Currency must be 3-letter code (e.g., USD, EUR)")
    #     self.currency = new_currency.upper()
    
    # def __repr__(self):
    #     return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
    
    def __str__(self):
        return f"User id: {self.id}, Name: {self.name}, Email: {self.email}, Added On: {self.created_at}, Preferred Currency: {self.currency}"
    # def to_dict(self):
    #     """Convert user to dictionary for database storage."""
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'email': self.email,
    #         'currency': self.currency,
    #         'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
    #     }
    
    # @classmethod
    # def from_dict(cls, data):
    #     """Create User instance from dictionary (from database)."""
    #     return cls(
    #         id=data.get('id'),
    #         name=data['name'],
    #         email=data.get('email'),
    #         currency=data.get('currency', 'USD'),
    #         created_at=datetime.strptime(data['created_at'], '%Y-%m-%d %H:%M:%S') if data.get('created_at') else None
    #     )