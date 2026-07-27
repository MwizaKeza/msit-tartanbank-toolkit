#!/bin/bash
date=$(date +%Y-%m-%d)
today_report="reports/report_${date}.txt"
input="data/transactions.csv"

if [ -f "$input" ]; then
    transactions_tot=$(wc -l < "$input")
    transactions_tot=$((transactions_tot - 1))
else
    count=0
fi

echo "Summary---------------------------------------->" > "$today_report"
echo "Number of Transactions: $transactions_tot" >> "$today_report"
python3 src/process.py "$input" "$today_report"
echo "Report is saved to $today_report" 
