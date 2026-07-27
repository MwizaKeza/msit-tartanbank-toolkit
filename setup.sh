#!/bin/bash
folders=("data" "reports" "src" "secrets")

for f in "${folders[@]}"; do
    if [! -d "$f"]; then
        mkdir "$f"
        echo "$f created"
    else 
        echo "$f already exists"
    fi
done

if [! -f "data/transactions.csv"]; then
    echo "Error: transactions.csv does not exist inside the data folder. You need to dd it."
else
    echo "transactions.csv exists in the data folder"
fi