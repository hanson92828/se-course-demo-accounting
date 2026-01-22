from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

class ExpenseError(Exception): 
    pass
class InvalidAmountError(ExpenseError): 
    pass

class StorageProtocol(Protocol):
    def load_all(self) -> list["Expense"]: ...
    def save_all(self, expenses: list["Expense"]) -> None: ...

@dataclass
class Expense:
    id: int
    amount: float
    category: str
    description: str
    date: str = datetime.now().strftime("%Y-%m-%d")
    
class ExpenseService:
    def __init__(self, storage: StorageProtocol):
        self.storage = storage

    def add_expense(self, amount: float, category: str, description: str) -> Expense:
        if amount <= 0:
            raise InvalidAmountError("金額必須大於 0")
        
        expenses = self.storage.load_all()
        new_id = max([e.id for e in expenses], default=0) + 1
        
        new_expense = Expense(
            id=new_id, 
            amount=amount,
            category=category, 
            description=description
        )
        expenses.append(new_expense)
        self.storage.save_all(expenses)
        return new_expense

    def get_total_by_category(self, category: str) -> float:
        expenses = self.storage.load_all()
        total = sum((e.amount for e in expenses if e.category == category), 0.0)
        return float(total)