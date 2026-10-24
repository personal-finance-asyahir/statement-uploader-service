class StatementMatcher:
    def match(self, text:str) -> tuple[str | None, str | None]: ...


class CimbCreditStatementMatcher(StatementMatcher):
    def match(self, text:str) -> tuple[str | None, str | None]:
        if ("CIMB".casefold() in text.casefold()
                and "Credit Card Statement".casefold() in text.casefold()):
            return "CIMB", "Credit Card Statement"
        return None

# Register Matcher
STATEMENT_MATCHERS: list[StatementMatcher] = [CimbCreditStatementMatcher()]


