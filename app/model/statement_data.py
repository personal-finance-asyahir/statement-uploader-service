from typing import Optional
from dataclasses import dataclass

@dataclass
class StatementData:
    bank: Optional[str]
    title: Optional[str]
    user_id: Optional[str] = None