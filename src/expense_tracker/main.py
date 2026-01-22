from expense_tracker.core import ExpenseService
from expense_tracker.storage import FileStorage

my_storage = FileStorage(file_path="my_data.json")

service = ExpenseService(storage=my_storage)

service.add_expense(100, "Food", "Lunch")