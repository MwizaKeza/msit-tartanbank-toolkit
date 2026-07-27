class Account:
    def __init__(self, account_id, balance=0.0):
        self.account_id = account_id
        self.balance = balance
        self.transaction_count = 0
        

    def deposit(self, amount):
        amount = float(amount)
        self.transaction_count+=1
        self.balance += amount

    def withdraw(self, amount):
        amount = float(amount)
        if self.balance >= amount:
            self.transaction_count+=1
            self.balance -= amount
            print("Successful withdraw")
            return True
        else:
            print("Insufficient funds")
            return False
    
class Ledger:

    def __init__(self):
        self.accounts = {}
        self.flagged = []
        self.deposit_count = 0
        self.deposit_total = 0.0

    def get_or_create(self, acc_id):
        if acc_id not in self.accounts:
            self.accounts[acc_id] = Account(acc_id)
        return self.accounts[acc_id]

    def apply(self, acc_id, t_type, amount):
        amount = float(amount)
        acc = self.get_or_create(acc_id)
        deposit_count = 0
        if t_type == "deposit":
            acc.deposit(amount)
            self.deposit_total+=amount
            self.deposit_count+=1

        elif t_type == "withdraw":
            sufficient_bal = acc.withdraw(amount)
            if not sufficient_bal:
                self.flagged.append({
                    "account_id": acc_id,
                    "type": 'withdraw',
                    "amount": amount
                })

    def summary(self):
        summary_list = []
        summary_list.append("Ledger Summary:")
        for i, a in self.accounts.items():
            summary_list.append(f"Account ID: {i} | Balance: {a.balance} | Transactions: {a.transaction_count}")

        summary_list.append(f"\nDeclined list:")
        for i in self.flagged:
            summary_list.append(f"Account: {i['account_id']} | Unsuccessful {i['type']} of {i['amount']}")
        
        mean = self.deposit_total / self.deposit_count if self.deposit_count > 0 else 0.0
        summary_list.append("Bank's Deposit Summary Statistics:")
        summary_list.append(f"Total value of all deposits: {self.deposit_total:.2f}")
        summary_list.append(f"Average Deposit amount: {mean:.2f}")
        return "\n".join(summary_list)