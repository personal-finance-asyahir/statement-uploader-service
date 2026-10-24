from typing import Optional
from dataclasses import dataclass

@dataclass
class StatementData:
    name: Optional[str]
    bank: Optional[str]
    title: Optional[str]
    statement_date: Optional[str]
    account_number: Optional[str]
    current_balance: Optional[str] = None
    previous_balance: Optional[str] = None
    file_path: Optional[str] = None