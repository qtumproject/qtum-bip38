#!/usr/bin/env python3

from qtum_bip38 import (
    bip38_encrypt, bip38_decrypt
)
from typing import Literal

import json

# Passphrase / password
PASSPHRASE: str = "qtum123"
# Wallet important format
WIF: str = "5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR"
# Network type
NETWORK: Literal["mainnet", "testnet"] = "testnet"
# To show detail
DETAIL: bool = True

encrypted_wif: str = bip38_encrypt(
    wif=WIF, passphrase=PASSPHRASE, network=NETWORK
)
print("BIP38 Encrypted WIF:", encrypted_wif)

print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
    encrypted_wif=encrypted_wif, passphrase=PASSPHRASE, network=NETWORK, detail=DETAIL
), indent=4))
