from typing import Optional

from app.model.statement_data import StatementData

class StatementMatcher:
    def match(self, text:str) -> Optional[StatementData]: ...


class CimbCreditStatementMatcher(StatementMatcher):
    def match(self, text:str) -> Optional[StatementData]:
        if ("CIMB".casefold() in text.casefold()
                and "Credit Card Statement".casefold() in text.casefold()):
            return StatementData("CIMB", "Credit Card Statement")
        return None

# Register Matcher
STATEMENT_MATCHERS: list[StatementMatcher] = [CimbCreditStatementMatcher()]


