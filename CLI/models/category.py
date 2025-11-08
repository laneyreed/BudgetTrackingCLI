from utils.constants import DEFAULT_EXPENSE_CATEGORIES, DEFAULT_INCOME_CATEGORIES

class Category:
    """A class to represent a financial category."""
    def __init__(self, id: int, name: str, description: str = ""):
        """Initialize a Category instance.
        Args:
            id (int): The unique identifier for the category.
            name (str): The name of the category.
            description (str, optional): A description of the category. Defaults to "".
        Raises:
            ValueError: If the category name is not in the list of default categories.
        """

        if name not in DEFAULT_EXPENSE_CATEGORIES + DEFAULT_INCOME_CATEGORIES:
            raise ValueError(f"Category name '{name}' is not in the list of default categories.")
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the Category instance.
        """
        return f"Category(id={self.id}, name={self.name}, description={self.description})"