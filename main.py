from account import Account
from transaction import Transaction


def main():
    """Run the PyBank ATM system."""

    acc = Account()
    trans = Transaction()

    while True:

        print("\n=============================")
        print("      Welcome to PyBank ATM")
        print("=============================")

        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":

            acc.register()

        elif choice == "2":

            user = acc.login()

            if user:

                while True:

                    print("\n--- Main Menu ---")

                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Transfer (EFT)")
                    print("4. View Statement")
                    print("5. Logout")

                    option = input(
                        "Select an option: "
                    )

                    if option == "1":

                        trans.withdraw(user)

                    elif option == "2":

                        trans.deposit(user)

                    elif option == "3":

                        trans.transfer(user)

                    elif option == "4":

                        trans.view_statements(
                            user[1]
                        )

                    elif option == "5":

                        print(
                            "Logged out. "
                            "Stay safe."
                        )

                        break

                    else:
                        print(
                            "Invalid option. "
                            "Please try again."
                        )

        elif choice == "3":

            print("GOODBYE")
            break

        else:
            print(
                "Invalid option. "
                "Please try again."
            )


if __name__ == "__main__":
    main()
