"""
ATM Activity Scenarios (ultra-simple)
1) Successful Withdrawal
2) Rejected After Exceeding PIN Attempts
3) Balance = 0 → Close Account
4) Insufficient Funds → Back to Menu
"""

# tiny formatter for "Event [guard] / action"
e = lambda ev, g="", a="": f"{ev}{(' ['+g+']') if g else ''}{(' / '+a) if a else ''}"

def show(title, steps):
    print(title)
    print("-" * len(title))  # single underline
    for i, (actor, text) in enumerate(steps, 1):
        print(f"{i:02d}. {actor:12} | {text}")
    print()

# common start
PREFIX = [
    ("Customer",   "Start"),
    ("Customer",   "Insert Card"),
    ("ATM System", "PIN Entry — entry/showPinPrompt()"),
    ("ATM System", "PIN Entry — exit/clearPinBuffer()"),
    ("ATM System", "Prompt for PIN"),
    ("ATM System", "Validate PIN"),
]

# 1) Successful withdrawal
S1 = [
    *PREFIX,
    ("Decision",   e("CheckPin", "correct", "resetCounter()")),
    ("Customer",   "Select Withdraw"),
    ("ATM System", "Check Balance"),
    ("Decision",   e("CheckBalance", "balance ≥ amount", "debitAccount()")),
    ("ATM System", "Dispense Cash"),
    ("ATM System", e("PrintReceipt", a="logTxn")),
    ("ATM System", "Eject Card"),
    ("Customer",   "End (Success)"),
]

# 2) Rejected after exceeding PIN attempts
def reject_steps(limit=3):
    s = [*PREFIX]
    for _ in range(limit-1):
        s += [
            ("Decision",   e("CheckPin", "incorrect", "incrementCounter()")),
            ("ATM System", e("CheckCounter", a="evaluate")),
            ("Decision",   e("CheckCounter", "< limit", "promptRetry()")),
            ("ATM System", "Prompt for PIN"),
            ("ATM System", "Validate PIN"),
        ]
    s += [
        ("Decision",   e("CheckPin", "incorrect", "incrementCounter()")),
        ("ATM System", e("CheckCounter", a="evaluate")),
        ("Decision",   e("CheckCounter", "≥ limit", "retainCard(), rejectCustomer()")),
        ("Customer",   "End (Rejected)"),
    ]
    return s

# 3) Balance = 0 → Close account
S3 = [
    *PREFIX,
    ("Decision",   e("CheckPin", "correct", "resetCounter()")),
    ("Customer",   "Select Withdraw"),
    ("ATM System", "Check Balance"),
    ("Decision",   e("CheckBalance", "balance = 0", "closeAccount()")),
    ("Customer",   "End (Account Closed)"),
]

# 4) Insufficient funds → back to menu
S4 = [
    *PREFIX,
    ("Decision",   e("CheckPin", "correct", "resetCounter()")),
    ("Customer",   "Select Withdraw"),
    ("ATM System", "Check Balance"),
    ("Decision",   e("CheckBalance", "balance < amount", "showInsufficientFunds()")),
    ("ATM System", e("ReturnToMenu", a="notifyUser()")),
    ("Customer",   "Back to Select Withdraw (loop continues)"),
]

if __name__ == "__main__":
    show("Scenario 1: Successful Withdrawal", S1)
    show("Scenario 2: Rejected After Exceeding PIN Attempts", reject_steps(3))
    show("Scenario 3: Balance Equals Zero -> Close Account", S3)
    show("Scenario 4: Insufficient Funds -> Return to Menu", S4)