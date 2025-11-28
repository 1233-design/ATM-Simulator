# atm_gui.py
# 💳 Python ATM GUI (Connected to atm_simulator.py)mb
# Developed by Pranjal Nagar and Prarthna✨

import tkinter as tk
from tkinter import messagebox, simpledialog
from atm_simulator import accounts, check_balance, deposit, withdraw, mini_statement

current_user = None

# ------------------- GUI Functions -------------------

def login():
    global current_user
    acc_no = acc_entry.get().strip()
    pin = pin_entry.get().strip()
    account = accounts.get(acc_no)
    if account and account["pin"] == pin:
        current_user = acc_no
        messagebox.showinfo("Login Successful", f"Welcome, {account['name']}!")
        open_main_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid account number or PIN.")

def open_main_menu():
    login_frame.pack_forget()
    main_frame.pack(pady=20)

def check_balance_gui():
    if current_user:
        bal = accounts[current_user]["balance"]
        messagebox.showinfo("Balance", f"Your current balance is ₹{bal:.2f}")

def deposit_gui():
    if current_user:
        try:
            amount = float(simpledialog.askstring("Deposit", "Enter amount to deposit (₹):"))
            if amount <= 0:
                messagebox.showwarning("Error", "Enter an amount greater than 0.")
                return

            accounts[current_user]["balance"] += amount

            # Add to transaction history
            from datetime import datetime
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            accounts[current_user]["transactions"].append(f"[{timestamp}] Deposited ₹{amount:.2f}")

            messagebox.showinfo("Success", f"₹{amount:.2f} deposited successfully!")
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Invalid amount entered.")

def withdraw_gui():
    if current_user:
        try:
            amount = float(simpledialog.askstring("Withdraw", "Enter amount to withdraw (₹):"))
            if amount <= 0:
                messagebox.showwarning("Error", "Enter an amount greater than 0.")
                return
            if amount <= accounts[current_user]["balance"]:
                accounts[current_user]["balance"] -= amount

                # 🔥 Add to transaction history
                from datetime import datetime
                timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                accounts[current_user]["transactions"].append(f"[{timestamp}] Withdrew ₹{amount:.2f}")

                messagebox.showinfo("Success", f"₹{amount:.2f} withdrawn successfully!")
            else:
                messagebox.showerror("Error", "Insufficient balance.")
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Invalid amount entered.")

def mini_statement_gui():
    if current_user:
        txns = accounts[current_user]["transactions"][-5:]
        if not txns:
            messagebox.showinfo("Mini Statement", "No transactions yet.")
        else:
            history = "\n".join(txns)
            messagebox.showinfo("Mini Statement", f"{history}\n\nAvailable Balance: ₹{accounts[current_user]['balance']:.2f}")

def logout():
    global current_user
    current_user = None
    main_frame.pack_forget()
    login_frame.pack(pady=20)

# ------------------- UI Layout -------------------

root = tk.Tk()
root.title("💳 Python ATM Simulator")
root.geometry("400x400")
root.config(bg="#f1f1f1")

# Login Frame
login_frame = tk.Frame(root, bg="#f1f1f1")
tk.Label(login_frame, text="ATM Login", font=("Arial", 18, "bold"), bg="#f1f1f1").pack(pady=20)

tk.Label(login_frame, text="Account Number:", bg="#f1f1f1").pack()
acc_entry = tk.Entry(login_frame)
acc_entry.pack(pady=5)

tk.Label(login_frame, text="PIN:", bg="#f1f1f1").pack()
pin_entry = tk.Entry(login_frame, show="*")
pin_entry.pack(pady=5)

tk.Button(login_frame, text="Login", command=login, bg="#4CAF50", fg="white", width=10).pack(pady=20)
login_frame.pack(pady=20)

# Main Menu Frame
main_frame = tk.Frame(root, bg="#f1f1f1")

tk.Label(main_frame, text="Select an Option", font=("Arial", 16, "bold"), bg="#f1f1f1").pack(pady=10)
tk.Button(main_frame, text="💰 Check Balance", command=check_balance_gui, width=20, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(main_frame, text="➕ Deposit Money", command=deposit_gui, width=20, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(main_frame, text="💸 Withdraw Money", command=withdraw_gui, width=20, bg="#FF9800", fg="white").pack(pady=5)
tk.Button(main_frame, text="🧾 Mini Statement", command=mini_statement_gui, width=20, bg="#9C27B0", fg="white").pack(pady=5)
tk.Button(main_frame, text="🚪 Logout", command=logout, width=20, bg="#f44336", fg="white").pack(pady=10)

root.mainloop()
