import numpy as np

def maybank_credit_card_statement_extractor(obj, idx, text):
    if np.array_equal(idx, [25.0, 785.0]):
        obj.name = text
        print("Name: " + text)
    elif np.array_equal(idx, [413.62, 756.0]):
        obj.statement_date = text
        print("Statment Date: " + text)
    elif np.array_equal(idx, [51.96, 651.2]):
        obj.account_number = text
        print("Account Number: " + text)
    elif np.array_equal(idx, [250.48, 651.2]):
        obj.current_balance = text
        print("Current Balance: " + text)
    elif np.array_equal(idx, [538.48, 288.2]):
        obj.previous_balance = text
        print("Previous Statement Balance: " + text)
    elif np.array_equal(idx, [181.5, 853.0]):
        obj.title = text
        print("Title: " + text)
    elif np.array_equal(idx, [466.9, 829.0]):
        obj.bank = text
        print("Bank Name: " + text)