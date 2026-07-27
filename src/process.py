import sys
import os
import csv
from bank import Account
from bank import Ledger

if len(sys.argv) < 3:
    print("Provide transactions.csv as a second arguement")
    sys.exit(1)

data_file = sys.argv[1]
report_file = sys.argv[2]

ledger = Ledger()
with open(data_file, "r") as f:
    r = csv.reader(f)
    next(r)
    
    for row in r:
        account_id = row[0].strip()
        the_type = row[1].strip()
        amount = row[2].strip()
        ledger.apply(account_id, the_type, amount)
    ledger_summary = ledger.summary()

with open(report_file, "a", encoding="utf-8") as f:
    f.write(str(ledger_summary))
if os.path.exists(report_file):
    print(f"Report summary generated")  
     
        
