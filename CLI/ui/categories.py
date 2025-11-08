from models.category import Category

from utils.constants import (
    DEFAULT_EXPENSE_CATEGORIES, 
    DEFAULT_INCOME_CATEGORIES
)


categories = []
# Initialize some default categories
def initialize_categories():
    """Initialize default categories for the application."""
    global categories
    category_id = 1
    
    for cat_name in DEFAULT_EXPENSE_CATEGORIES:
        categories.append(Category(id=category_id, name=cat_name, description=f"Expense: {cat_name}"))
        category_id += 1
    
    for cat_name in DEFAULT_INCOME_CATEGORIES:
        categories.append(Category(id=category_id, name=cat_name, description=f"Income: {cat_name}"))
        category_id += 1
