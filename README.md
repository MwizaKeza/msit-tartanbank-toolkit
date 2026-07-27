# TartanBank Nightly Toolkit
TartanBank's nightly toolkit is a report that collects the day's transactions, applies them to the correct accounts and flags suspicious transactions.

### The set up:
Bash takes care of the operating system while Python handles the accounts and ledger logic. 
setup.sh creates the folder sturcture by checking for existing folders and creating important folders.
secure_cred.sh is used to hash the operator's passphrase.
Finally run.sh connects them all by checking existing input file (the transactions), calls the python program and stores
the report summary produced by the python, to a dated report file. Python handles classes Account and Ledger in bank.py,
which tracks the transactions and account balances. process.py then reads the day's transactions file, applies it to the ledger
and produces the summary report bash eventually uses.

> quiz.sh and quiz_result.png are files which tested my strength in bash and according to my results, I passed.

### Challenges:
I had a bit of difficulty connecting the summary report from process.py to run.sh. My solution was to create a list in method summary,
called summary_ist, and append the summary line so that it would be easier to print the report once run.sh ran.

### How to run it:
> Run the setup.sh first to ensure necessary files exist and to build your report folder
'./setup.sh'

> Finally generate your report . You will find the report generated in reports/reportYYYY-MM-DD.txt
'./run.sh'
