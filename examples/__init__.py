#!/usr/bin/env python3

from qtum_bip38 import (
    private_key_to_wif, bip38_encrypt, bip38_decrypt
)
from typing import List

import json

# Private key
PRIVATE_KEY: str = "cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5"
# Passphrase / password
PASSPHRASE: str = "qtum123"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
# To show detail
DETAIL: bool = True
# Wallet important format's
WIFs: List[str] = [
    private_key_to_wif(private_key=PRIVATE_KEY, wif_type="wif"),  # No compression
    private_key_to_wif(private_key=PRIVATE_KEY, wif_type="wif-compressed")  # Compression
]

for WIF in WIFs:
    print("WIF:", WIF)

    encrypted_wif: str = bip38_encrypt(
        wif=WIF, passphrase=PASSPHRASE
    )
    print("BIP38 Encrypted WIF:", encrypted_wif)

    print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
        encrypted_wif=encrypted_wif, passphrase=PASSPHRASE, detail=DETAIL
    ), indent=4))

    print("-" * 125)
