import pytest
from src.expense_tracker.core import ExpenseService, InvalidAmountError

# 建立一個假的 Storage 類別來模擬檔案讀寫
class EmptyStorage:
    def __init__(self):
        self.data = []
    def load_all(self):
        return self.data
    def save_all(self, expenses):
        self.data = expenses

# 測試正常新增支出的情況     
def test_add_expense_valid_data():
    # 1. 準備：建立 Mock 物件並注入 Service
    mock = EmptyStorage()
    service = ExpenseService(storage=mock)
    
    # 2. 執行：新增一筆支出
    expense = service.add_expense(amount=100.0, category="Food", description="Lunch")
    
    # 3. 驗證：檢查回傳值與儲存狀態
    assert expense.amount == 100.0
    assert expense.id == 1
    assert len(mock.data) == 1  # 確保資料有被「存入」mock 中

# 回歸測試：確保金額為負數時會拋出錯誤
def test_add_expense_negative_amount():
    mock = EmptyStorage()
    service = ExpenseService(storage=mock)
    
    # 驗證是否拋出自定義的 InvalidAmountError
    with pytest.raises(InvalidAmountError):
        service.add_expense(amount=-50, category="Test", description="Error Case")