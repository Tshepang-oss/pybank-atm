# PyBank ATM

A Python command-line ATM simulation built to practise object-oriented programming, file handling, and user input.

## Features

- Register an account with a phone number and PIN.
- Log in using a phone number and PIN.
- Deposit and withdraw money.
- Transfer money between registered accounts.
- View transaction history.
- Save account data and activity in local text files.

## Requirements

Python 3. No additional packages are required.

## How to run

1. Download the project and extract it into a folder.
2. Open a terminal in that folder.
3. Run:

```bash
python main.py
```

4. Choose **Register** to create a demo account, then log in.

Use fictional details for testing. Account and activity files are created as you use the application. Make a transaction before viewing your statement.

## Project files

- `main.py` — application menus and navigation.
- `account.py` — registration, login, PIN hashing, and account event logging.
- `transaction.py` — deposits, withdrawals, transfers, and statements.

## Future improvements

- Validate transaction amounts and handle invalid input.
- Handle missing transaction files gracefully.
- Improve account security and transaction storage.

## Purpose

This is an educational simulation, intended for learning Python rather than handling real money or banking credentials.
