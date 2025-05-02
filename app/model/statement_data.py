from typing import Optional
from dataclasses import dataclass

@dataclass
class StatementData:
    bank: Optional[str]
    title: Optional[str]
    file_path: Optional[str] = None