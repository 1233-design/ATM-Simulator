# 💳 Python ATM Simulator (Cute, Colorful & Multi-Account Version)
# Developed by Pranjal Nagar and Prarthna ✨

from colorama import Fore, Style, init
from datetime import datetime
import time
import os

# Initialize colorama for colorful output
init(autoreset=True)

# In-memory database for multiple accounts
accounts = {
    "123456": {
        "name": "Pranjal Nagar",
        "pin": "1234",
        "balance": 5000.0,
        "transactions": []
    },
    "654321": {
        "name": "Prarthna Singh",
        "pin": "4321",
        "balance": 3000.0,
        "transactions": []
    }
}

# Clear console for better UX
def clear_screen():
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')

# Simulate card insertion animation
def simulate_card_insertion():
    print(Fore.CYAN + "💳 Please insert your card", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(Fore.CYAN + ".", end="", flush=True)
    print(Fore.GREEN + "\n✅ Card detected! Reading details...")
    time.sleep(1)

# Authenticate account and PIN
def login():
    acc_no = input(Fore.LIGHTWHITE_EX + "🔢 Enter your Account Number: ").strip()
    pin = input(Fore.LIGHTWHITE_EX + "🔑 Enter your PIN: ").strip()
    account = accounts.get(acc_no)

    if account and account["pin"] == pin:
        print(Fore.GREEN + f"\n✅ Welcome, {account['name']}!\n")
        return acc_no
    else:
        print(Fore.RED + "\n❌ Invalid account number or PIN.\n")
        return None

# Colorful loading animation
def loading_effect():
    print(Fore.CYAN + "Processing", end="")
    for i in range(3):
        print(Fore.CYAN + ".", end="", flush=True)
        time.sleep(0.5)
    print("\n" + Fore.GREEN + "✅ Done!\n")

# Check balance
def check_balance(acc_no):
    bal = accounts[acc_no]["balance"]
    print(Fore.LIGHTBLUE_EX + f"\n💰 Your current balance is: ₹{bal:.2f}\n")

# Deposit money
def deposit(acc_no):
    try:
        amount = float(input(Fore.LIGHTYELLOW_EX + "\nEnter amount to deposit: ₹"))
        if amount <= 0:
            print(Fore.RED + "⚠️ Please enter a valid amount!")
            return
    except ValueError:
        print(Fore.RED + "⚠️ Invalid input! Please enter numbers only.")
        return

    loading_effect()
    accounts[acc_no]["balance"] += amount
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    accounts[acc_no]["transactions"].append(f"[{timestamp}] Deposited ₹{amount:.2f}")
    print(Fore.GREEN + f"✅ ₹{amount} deposited successfully!")
    print(Fore.LIGHTBLUE_EX + f"💰 Updated Balance: ₹{accounts[acc_no]['balance']:.2f}")

# Withdraw money
def withdraw(acc_no):
    try:
        amount = float(input(Fore.LIGHTYELLOW_EX + "\nEnter amount to withdraw: ₹"))
        if amount <= 0:
            print(Fore.RED + "⚠️ Please enter a valid amount!")
            return
    except ValueError:
        print(Fore.RED + "⚠️ Invalid input! Please enter numbers only.")
        return

    if amount <= accounts[acc_no]["balance"]:
        loading_effect()
        accounts[acc_no]["balance"] -= amount
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        accounts[acc_no]["transactions"].append(f"[{timestamp}] Withdrew ₹{amount:.2f}")
        print(Fore.GREEN + f"✅ ₹{amount} withdrawn successfully!")
        print(Fore.LIGHTBLUE_EX + f"💰 Remaining Balance: ₹{accounts[acc_no]['balance']:.2f}")
    else:
        print(Fore.RED + "🚫 Insufficient balance!\n")

# Show last 5 transactions
def mini_statement(acc_no):
    print(Fore.MAGENTA + "\n📜 Mini Statement (Last 5 Transactions):")
    txns = accounts[acc_no]["transactions"][-5:]
    if not txns:
        print(Fore.LIGHTBLACK_EX + "No transactions yet.")
    else:
        for t in txns:
            print(Fore.CYAN + "-", t)
    print(Fore.LIGHTBLUE_EX + f"\nAvailable Balance: ₹{accounts[acc_no]['balance']:.2f}\n")

# ATM main menu
def main_menu(acc_no):
    while True:
        print(Fore.YELLOW + "-------------------------------------")
        print(Fore.MAGENTA + Style.BRIGHT + "\n🏦 ATM Main Menu")
        print(Fore.CYAN + "1️⃣  Check Balance")
        print(Fore.CYAN + "2️⃣  Deposit Money")
        print(Fore.CYAN + "3️⃣  Withdraw Money")
        print(Fore.CYAN + "4️⃣  View Mini Statement")
        print(Fore.CYAN + "5️⃣  Exit")
        print(Fore.YELLOW + "-------------------------------------")

        choice = input(Fore.LIGHTWHITE_EX + "\n👉 Enter your choice (1–5): ").strip()

        if choice == "1":
            check_balance(acc_no)
        elif choice == "2":
            deposit(acc_no)
        elif choice == "3":
            withdraw(acc_no)
        elif choice == "4":
            mini_statement(acc_no)
        elif choice == "5":
            print(Fore.MAGENTA + "\n🙏 Thank you for using Python ATM! Have a great day! 🌸\n")
            break
        else:
            print(Fore.RED + "❌ Invalid choice! Please select between 1–5.")

        input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue...")
        clear_screen()

# Program entry point
def main():
    clear_screen()
    print(Fore.CYAN + "=== Welcome to Python ATM Simulator ===\n")
    simulate_card_insertion()
    acc_no = login()
    if acc_no:
        clear_screen()
        main_menu(acc_no)
    else:
        print(Fore.RED + "Exiting program. Please try again later.")

if __name__ == "__main__":
    main()
