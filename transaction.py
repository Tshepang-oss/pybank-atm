import csv
from datetime import datetime


class Transaction:
    """Handles all ATM transactions."""

    def __init__(self):
        self.acc_file = "account_balance.txt"
        self.trans_file = "transactions.txt"

    def log_transaction(self, phone, t_type, amount, balance):
        """Log transactions with timestamp."""

        with open(self.trans_file, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                phone,
                t_type,
                f"{amount:.2f}",
                f"{balance:.2f}"
            ])

    def write_accounts(self, rows):
        """Write updated account data to file."""

        with open(self.acc_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def deposit(self, user):
        """Deposit money into the user's account."""

        amount = float(input("Amount to deposit: R"))

        rows = []
        new_balance = 0.0

        with open(self.acc_file, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == user[0]:
                    new_balance = float(row[3]) + amount
                    row[3] = f"{new_balance:.2f}"

                rows.append(row)

        self.write_accounts(rows)

        self.log_transaction(
            user[1],
            "DEPOSIT",
            amount,
            new_balance
        )

        print(
            f"Deposit successful! "
            f"New balance: R{new_balance:.2f}"
        )

    def withdraw(self, user):
        """Withdraw money from the user's account."""

        amount = float(input("Amount to withdraw: R"))

        rows = []
        new_balance = 0.0

        with open(self.acc_file, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == user[0]:
                    balance = float(row[3])

                    if amount > balance:
                        print("Insufficient funds.")
                        return

                    new_balance = balance - amount
                    row[3] = f"{new_balance:.2f}"

                rows.append(row)

        self.write_accounts(rows)

        self.log_transaction(
            user[1],
            "WITHDRAWAL",
            amount,
            new_balance
        )

        print(
            f"Withdrawal successful! "
            f"New balance: R{new_balance:.2f}"
        )

    def transfer(self, user):
        """Transfer money to another account."""

        print("\n--- Transfer Funds ---")

        dest = input("Enter recipient's account number: ")

        if len(dest) != 8:
            print("Error: Account number must be 8 digits.")
            return

        if dest == user[0]:
            print("Error: Cannot transfer to your own account.")
            return

        amount = float(input("Amount to transfer: R"))

        rows = []
        sender_balance = 0.0
        recipient_balance = 0.0
        found = False

        with open(self.acc_file, "r") as file:
            reader = csv.reader(file)

            for row in reader:

                if row[0] == user[0]:
                    sender_balance = float(row[3])

                    if amount > sender_balance:
                        print("Insufficient funds.")
                        return

                    row[3] = (
                        f"{sender_balance - amount:.2f}"
                    )

                elif row[0] == dest:
                    recipient_balance = (
                        float(row[3]) + amount
                    )

                    row[3] = (
                        f"{recipient_balance:.2f}"
                    )

                    found = True

                rows.append(row)

        if not found:
            print(
                "Error: Account not found. "
                "Please check the account number "
                "and try again."
            )
            return

        self.write_accounts(rows)

        new_balance = sender_balance - amount

        self.log_transaction(
            user[1],
            "EFT OUT",
            amount,
            new_balance
        )

        self.log_transaction(
            dest,
            "EFT IN",
            amount,
            recipient_balance
        )

        print(
            f"Transfer successful. "
            f"R{amount:.2f} sent to account {dest}."
        )

        print(
            f"Your new balance: "
            f"R{new_balance:.2f}"
        )

    def view_statements(self, phone):
        """Display transaction history for the user."""

        print("\n--- Transaction History ---")

        print(
            "DATE & TIME          | "
            "TYPE       | "
            "AMOUNT     | "
            "BALANCE"
        )

        print("-" * 60)

        with open(self.trans_file, "r") as file:
            reader = csv.reader(file)

            for row in reader:

                if row[1] == phone:
                    date, _, t_type, amount, balance = row

                    sign = (
                        "+"
                        if t_type in ["DEPOSIT", "EFT IN"]
                        else "-"
                    )

                    print(
                        f"{date} | "
                        f"{t_type:<8} | "
                        f"{sign}R{float(amount):<7.2f} | "
                        f"R{float(balance):<8.2f}"
                    )
