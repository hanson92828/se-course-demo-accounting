import re

def validate_category(category: str) -> bool:
    """檢查類別是否只包含字母與底線，且長度在 2-20 之間"""
    return bool(re.match(r"^[a-zA-Z_]{2,20}$", category))

def format_currency(amount: float) -> str:
    """格式化金額展示"""
    return f"${amount:,.2f}"