#!/bin/bash
OPERATOR_ID=$(awk -F ':' 'NR ==1 {print $2}' ../secrets/credentials.txt| awk '{print$1}')
PASSPHR_HASH=$(awk -F ':' 'NR ==2 {print $2}' ../secrets/credentials.txt| sha256sum | awk '{print$1}')
echo -e "Operator id: $OPERATOR_ID\nPassphrase: $PASSPHR_HASH" > ../secrets/operator.hash
if [[ -f ../secrets/operator.hash ]]; then
    echo "Operator id and hashed passphrase successfully stored in secrets/operator.hash"
else
    echo "Failed to create file and store Operator id and hashed passphrase"
fi