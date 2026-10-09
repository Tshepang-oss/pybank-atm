import csv
import hashlib
import random
from datetime import datetime


class Account:
    """Represent a bank account and store user details."""

    def __init__(self):
        self.file = "account_balance.txt"
        self.log_files = "log.txt"

    def hash_pin(self, pin):
        """Hash the PIN using SHA-256."""

        return hashlib.sha256(pin.encode()).hexdigest()

    def generate_account_number(self):
        """Generate a unique 8-digit account number."""

        while True:
            acc_num = str(
                random.randint(10000000, 99999999)
            )

            try:
                with open(self.file, "r") as file:
                    reader = csv.reader(file)

                    if any(
                        row[0] == acc_num
                        for row in reader
                    ):
                        continue

            except FileNotFoundError:
                pass

            return acc_num

    def log_event(self, phone, event):
        """Log account events with timestamp."""

        with open(
            self.log_files,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                phone,
                event
            ])

    def register(self):
        """Register a new user account."""

        print("\n--- Account Registration ---")

        phone = input(
            "Enter your phone number (10 digits): "
        )

        if len(phone) != 10 or not phone.isdigit():
            print(
                "Error: Please enter a valid "
                "10-digit phone number."
            )
            return

        try:
            with open(self.file, "r") as file:
                reader = csv.reader(file)

                if any(
                    row[1] == phone
                    for row in reader
                ):
                    print(
                        "Phone number already registered."
                    )
                    return

        except FileNotFoundError:
            pass

        pin = input("Create a PIN (4-5 digits): ")

        if (
            not pin.isdigit()
            or len(pin) not in [4, 5]
        ):
            print(
                "Error: PIN must be 4-5 digits."
            )
            return

        confirm = input("Confirm your PIN: ")

        if pin != confirm:
            print("Error: PINs do not match.")
            return

        acc_num = self.generate_account_number()

        hashed_pin = self.hash_pin(pin)

        with open(
            self.file,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                acc_num,
                phone,
                hashed_pin,
                0.00
            ])

        self.log_event(phone, "REGISTERED")

        print("\nRegistration successful!")

        print(
            f"Your account number is: {acc_num}"
        )

        print(
            "Please save this number. "
            "You will need it to access "
            "your account."
        )

    def login(self):
        """Authenticate user login with 3 attempts."""

        print("\n--- Login ---")

        attempts = 0

        while attempts < 3:

            phone = input(
                "Enter your phone number "
                "(10 digits): "
            )

            if (
                len(phone) != 10
                or not phone.isdigit()
            ):
                print(
                    "Error: Please enter a valid "
                    "10-digit phone number."
                )
                return None

            pin = input("Enter your PIN: ")

            hashed_pin = self.hash_pin(pin)

            try:
                with open(self.file, "r") as file:
                    reader = csv.reader(file)

                    for row in reader:

                        if (
                            row[1].strip() == phone
                            and row[2].strip()
                            == hashed_pin
                        ):

                            print(
                                "\nLogin successful!"
                            )

                            self.log_event(
                                phone,
                                "LOGIN_SUCCESS"
                            )

                            return row

                attempts += 1

                self.log_event(
                    phone,
                    "LOGIN_FAILED"
                )

                print(
                    f"Incorrect phone number "
                    f"or PIN. Attempts left: "
                    f"{3 - attempts}"
                )

            except FileNotFoundError:
                print(
                    "Error: No accounts found. "
                    "Please register first."
                )
                return None

        print(
            "Too many failed attempts. "
            "Please try again later."
        )

        return None
