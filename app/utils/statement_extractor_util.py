import numpy as np

def maybank_credit_card_statement_extractor(obj, idx, text):
    if np.array_equal(idx, [25.0, 785.0]):
        obj.name = text
    elif np.array_equal(idx, [413.62, 756.0]):
        obj.statement_date = text
    elif np.array_equal(idx, [51.96, 651.2]):
        obj.account_number = text
    elif np.array_equal(idx, [250.48, 651.2]):
        obj.current_balance = text
    elif np.array_equal(idx, [538.48, 288.2]):
        obj.previous_balance = text
    elif np.array_equal(idx, [181.5, 853.0]):
        obj.title = text
    elif np.array_equal(idx, [466.9, 829.0]):
        obj.bank = text

def maybank_debit_card_statement_extractor(obj, idx, text):
    if np.array_equal(idx, [76.04, 711.0]):
        obj.name = text
    elif np.array_equal(idx, [448.69, 714.0]):
        obj.statement_date = text
    elif np.array_equal(idx, [422.87, 678.5]):
        obj.account_number = text
    elif np.array_equal(idx, [416.24, 646.0]):
        obj.title = text
    elif np.array_equal(idx, [214.42, 761.0]):
        obj.bank = text