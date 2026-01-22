import json
import os
from .core import Expense

class FileStorage:
    def __init__(self, file_path: str = "expenses.json"):
        self.file_path = file_path

    def load_all(self) -> list[Expense]:
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as f:
            data = json.load(f)
            return [Expense(**item) for item in data]

    def save_all(self, expenses: list[Expense]):
        with open(self.file_path, "w") as f:
            # 將 dataclass 轉為字典儲存
            json.dump([e.__dict__ for e in expenses], f, indent=4)