# Qtum-BIP38

[![GitHub Workflow](https://github.com/qtumproject/qtum-bip38/actions/workflows/workflow.yml/badge.svg)](https://github.com/qtumproject/qtum-bip38)
[![PyPI Version](https://img.shields.io/pypi/v/qtum-bip38.svg?color=blue)](https://pypi.org/project/qtum-bip38)
[![PyPI License](https://img.shields.io/pypi/l/qtum-bip38?color=black)](https://pypi.org/project/qtum-bip38)
[![PyPI Python Version](https://img.shields.io/pypi/pyversions/qtum-bip38.svg)](https://pypi.org/project/qtum-bip38)

Python library for implementation of BIP38 for Qtum. It supports both [No EC-multiply](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki#encryption-when-ec-multiply-flag-is-not-used) and [EC-multiply](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki#encryption-when-ec-multiply-mode-is-used) modes.

For more info see the [Passphrase-protected private key - BIP38](https://en.bitcoin.it/wiki/BIP_0038) spec.

## Installation

The easiest way to install `qtum-bip38` is via pip:

```
pip install qtum-bip38
```

If you want to run the latest version of the code, you can install from the git:

```
pip install git+git://github.com/qtumproject/qtum-bip38.git
```

## Documentation

Read here: https://bip38.readthedocs.io

When you import, replace `bip38` to `qtum_bip38` package name.

## Quick Usage

##### no EC multiply:

```python
#!/usr/bin/env python3

from qtum_bip38 import (
    private_key_to_wif, bip38_encrypt, bip38_decrypt
)
from typing import (
    List, Literal
)

import json

# Private key
PRIVATE_KEY: str = "cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5"
# Passphrase / password
PASSPHRASE: str = "qtum123"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
# Network type
NETWORK: Literal["mainnet", "testnet"] = "mainnet"
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
        wif=WIF, passphrase=PASSPHRASE, network=NETWORK
    )
    print("BIP38 Encrypted WIF:", encrypted_wif)
    
    print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
        encrypted_wif=encrypted_wif, passphrase=PASSPHRASE, network=NETWORK, detail=DETAIL
    ), indent=4))

    print("-" * 125)
```

<details open>
  <summary>Output</summary><br/>

```shell
WIF: 5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR
BIP38 Encrypted WIF: 6PRP4FDk4BWidB539rEWBH26DRcG2tavQg52WRcyuK5dxMdu8WHVftRZof
BIP38 Decrypted: {
    "wif": "5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR",
    "private_key": "cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5",
    "wif_type": "wif",
    "public_key": "04d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360ea7f23327b49ba7f10d17fad15f068b8807dbbc9e4ace5d4a0b40264eefaf31a4",
    "public_key_type": "uncompressed",
    "seed": null,
    "address": "QeS5U4AEaxPpJ8swzLHEcNbAaNkDfpWjQN",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
WIF: L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP
BIP38 Encrypted WIF: 6PYUYP8xySgSbqtYXHGfWUn1xL9F3r9qKru8CUbqeK94QSrJcrSAmZoaEd
BIP38 Decrypted: {
    "wif": "L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP",
    "private_key": "cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5",
    "wif_type": "wif-compressed",
    "public_key": "02d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360e",
    "public_key_type": "compressed",
    "seed": null,
    "address": "QRfLX1RpJN25v2jKGPYsQHu8G1ag3sHJeL",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
```
</details>

##### EC multiply:

```python
#!/usr/bin/env python3

from qtum_bip38 import (
    intermediate_code, create_new_encrypted_wif, confirm_code, bip38_decrypt
)
from typing import (
    List, Literal
)

import json
import os

# Passphrase / password
PASSPHRASE: str = "qtum123"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
# Network type
NETWORK: Literal["mainnet", "testnet"] = "mainnet"
# To show detail
DETAIL: bool = True
# List of samples with owner salt, seed, public key type, lot, and sequence
SAMPLES: List[dict] = [
    # Random owner salt & seed, No compression, No lot & sequence
    {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "uncompressed", "lot": None, "sequence": None},
    # Random owner salt & seed, No compression, With lot & sequence
    {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "uncompressed", "lot": 863741, "sequence": 1},
    # Random owner salt & seed, Compression, No lot & sequence
    {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "compressed", "lot": None, "sequence": None},
    # Random owner salt & seed, Compression, With lot & sequence
    {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "compressed", "lot": 863741, "sequence": 1},
    # With owner salt & seed, No compression, No lot & sequence
    {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "uncompressed", "lot": None, "sequence": None},
    # With owner salt & seed, No compression, With lot & sequence
    {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "uncompressed", "lot": 567885, "sequence": 1},
    # With owner salt & seed, Compression, No lot & sequence
    {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "compressed", "lot": None, "sequence": None},
    # With owner salt & seed, Compression, With lot & sequence
    {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "compressed", "lot": 369861, "sequence": 1},
]

for SAMPLE in SAMPLES:
    
    intermediate_passphrase: str = intermediate_code(
        passphrase=PASSPHRASE, owner_salt=SAMPLE["owner_salt"], lot=SAMPLE["lot"], sequence=SAMPLE["sequence"]
    )
    print("Intermediate Passphrase:", intermediate_passphrase)

    encrypted_wif: dict = create_new_encrypted_wif(
        intermediate_passphrase=intermediate_passphrase, public_key_type=SAMPLE["public_key_type"], seed=SAMPLE["seed"], network=NETWORK
    )
    print("Encrypted WIF:", json.dumps(encrypted_wif, indent=4))

    print("Confirm Code:", json.dumps(confirm_code(
        passphrase=PASSPHRASE, confirmation_code=encrypted_wif["confirmation_code"], network=NETWORK, detail=DETAIL
    ), indent=4))

    print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
        encrypted_wif=encrypted_wif["encrypted_wif"], passphrase=PASSPHRASE, network=NETWORK, detail=DETAIL
    ), indent=4))

    print("-" * 125)
```

<details>
  <summary>Output</summary><br/>

```shell
Intermediate Passphrase: passphraserBh92DkAgrAfqUTZoL8daK85X4UtSzQnEFABTmZf6prj1bAa6kPihApMd92xmw
Encrypted WIF: {
    "encrypted_wif": "6PfVzPRrrLrv3geDZV6GWcLfGRHBGagK31jBTTBd5f5QknK2S1p1ajLMe6",
    "confirmation_code": "cfrm38V5kycvZygpKdQmq3TjNED2womqd24UgVxFaxCuBnEAqp1aCUqQLSSAJBifBkcQDj33EcP",
    "public_key": "0440097fbf7fc6a3dea0962ee4e1701a9cd3964eb0223f243b759e1c04fda754ab88efcdb76753217c7d7b6456932bb8d77e5db1b4de3b22ce561d5daec1c8f809",
    "seed": "8637d0313eac9aab134ace0d010cf7856ffd2275cd4aba4c",
    "public_key_type": "uncompressed",
    "address": "QTPiD2P1zBz5fiGXxBkLdDyhySqTR7dvuy"
}
Confirm Code: {
    "public_key": "0440097fbf7fc6a3dea0962ee4e1701a9cd3964eb0223f243b759e1c04fda754ab88efcdb76753217c7d7b6456932bb8d77e5db1b4de3b22ce561d5daec1c8f809",
    "public_key_type": "uncompressed",
    "address": "QTPiD2P1zBz5fiGXxBkLdDyhySqTR7dvuy",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "5JSLzkUVB6ifEHgQBYrNKBpupV9SFccSfYiVjazAu3bpykVLJ5z",
    "private_key": "51e047d800758ea123d778f0bc7b375ef7a4a980ed5defaa9d535bc22d728e60",
    "wif_type": "wif",
    "public_key": "0440097fbf7fc6a3dea0962ee4e1701a9cd3964eb0223f243b759e1c04fda754ab88efcdb76753217c7d7b6456932bb8d77e5db1b4de3b22ce561d5daec1c8f809",
    "public_key_type": "uncompressed",
    "seed": "8637d0313eac9aab134ace0d010cf7856ffd2275cd4aba4c",
    "address": "QTPiD2P1zBz5fiGXxBkLdDyhySqTR7dvuy",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphrasea9wRhemdARJDoZzZMiVcmZaBrQYhofqaNuTAHgLyQmoUjLmpwFtyzFvjcoPRqA
Encrypted WIF: {
    "encrypted_wif": "6PgP82oWUAUAVAT41HBXsWih74ZSC5GT5dMbFWoxPYgLHHYbgo3XM7yJ3C",
    "confirmation_code": "cfrm38V8dbJk9zPFcbN84DF4u4mnkGBMrmM56rtWQyt22aDLNqfYmgEyYuLVq1uEW41LdqVfaf7",
    "public_key": "045c68c340753c4f416f44cf94eaa2240f0ed054332c87d9a6c4e0bcb4f6f5ebaaaf325b62f066a4e561ec1fd8d3bc546cddbe97889c59a2fd60e2d89b101a1171",
    "seed": "88cfd3b2a526ff29a62d429e52e597c24af6465edd011de3",
    "public_key_type": "uncompressed",
    "address": "Qf5NdtPRxsNeUTPckEyMW6cc7JpipJRJSw"
}
Confirm Code: {
    "public_key": "045c68c340753c4f416f44cf94eaa2240f0ed054332c87d9a6c4e0bcb4f6f5ebaaaf325b62f066a4e561ec1fd8d3bc546cddbe97889c59a2fd60e2d89b101a1171",
    "public_key_type": "uncompressed",
    "address": "Qf5NdtPRxsNeUTPckEyMW6cc7JpipJRJSw",
    "lot": 863741,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "5JhYHSPBT4XHuzyjGgxiL6be1zGJzQGoSrRRm7ijWccASdLiCkC",
    "private_key": "746098bcac5ecbd247f8fd1ca75340bc95bffa53e800169deb77b7e7143b246b",
    "wif_type": "wif",
    "public_key": "045c68c340753c4f416f44cf94eaa2240f0ed054332c87d9a6c4e0bcb4f6f5ebaaaf325b62f066a4e561ec1fd8d3bc546cddbe97889c59a2fd60e2d89b101a1171",
    "public_key_type": "uncompressed",
    "seed": "88cfd3b2a526ff29a62d429e52e597c24af6465edd011de3",
    "address": "Qf5NdtPRxsNeUTPckEyMW6cc7JpipJRJSw",
    "lot": 863741,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphrasemh3J6kj36t1846BnPFZL1caQN55pJfdcSSCztsQLBzF3jETYppiU5xYSsZrC5e
Encrypted WIF: {
    "encrypted_wif": "6PnSDkPgRS869GdKSHbUkm6VdKzUZiEtuDSUQUuYAJ2VumpTo3Y7cXbjFc",
    "confirmation_code": "cfrm38VUMfQFA5nUna7HpkQoiQSWMmw64rnPF3Zwu6g6S6CnXoXDey3Ptovhr9DKZymFQRYnesB",
    "public_key": "0208d6c6104daf76cdf8eb4ee75afd83b5776fd120e2d9a7cb78df5268fe534a37",
    "seed": "4bc118a7011b225af9e475f21816e8e71d47c103846e19c2",
    "public_key_type": "compressed",
    "address": "QgCL3wEfZP7RPQ3RRhazRx9Buuq2PLLqoG"
}
Confirm Code: {
    "public_key": "0208d6c6104daf76cdf8eb4ee75afd83b5776fd120e2d9a7cb78df5268fe534a37",
    "public_key_type": "compressed",
    "address": "QgCL3wEfZP7RPQ3RRhazRx9Buuq2PLLqoG",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "L4ybEBRKhicidQbeGHjy4f4Wyvad5Kgnwk7FqeQntqwUMcr7ERF1",
    "private_key": "e76f72811b89f63d88a7329eeedef16710ea66714672021a177e07fd5473f61a",
    "wif_type": "wif-compressed",
    "public_key": "0208d6c6104daf76cdf8eb4ee75afd83b5776fd120e2d9a7cb78df5268fe534a37",
    "public_key_type": "compressed",
    "seed": "4bc118a7011b225af9e475f21816e8e71d47c103846e19c2",
    "address": "QgCL3wEfZP7RPQ3RRhazRx9Buuq2PLLqoG",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseZi3JhthoBvhc8wenvQW7Hd7jBcmNjMKg544pQE2kVd5NCvt8qqoV6RLUaWZrEV
Encrypted WIF: {
    "encrypted_wif": "6PoE1PPV7YBVbkPZLsKZGE3T6imCpuDq9pxF1v779xtzo4dd8W13tAn2qD",
    "confirmation_code": "cfrm38VWvrvCAhjKDVmjnJp1dsTcJphB8YkK9jXygpLAEDQVCoeguazChN5JCpP6EsmWr5iB4wb",
    "public_key": "036a8f9c1a4d769b7326037cea69009560dbdb35b749ce1b8e716485a8730cfc09",
    "seed": "1140bf8c4f8c4ca09f90cce6da1ea8de1e43ac37165fe27f",
    "public_key_type": "compressed",
    "address": "QdxToVfxRc5PXtf28STR8u2JpmvpQsevF4"
}
Confirm Code: {
    "public_key": "036a8f9c1a4d769b7326037cea69009560dbdb35b749ce1b8e716485a8730cfc09",
    "public_key_type": "compressed",
    "address": "QdxToVfxRc5PXtf28STR8u2JpmvpQsevF4",
    "lot": 863741,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "L5BrcjdARTnCVjZa9AbeRR6GpZoP9bqp44Puj7VzvWeBUTYUu597",
    "private_key": "edbebe261a5eca1164911bf523f890a4a99051947c34bec7df71db16b29cfb98",
    "wif_type": "wif-compressed",
    "public_key": "036a8f9c1a4d769b7326037cea69009560dbdb35b749ce1b8e716485a8730cfc09",
    "public_key_type": "compressed",
    "seed": "1140bf8c4f8c4ca09f90cce6da1ea8de1e43ac37165fe27f",
    "address": "QdxToVfxRc5PXtf28STR8u2JpmvpQsevF4",
    "lot": 863741,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseondJwvQGEWFNsbiN6AVu4r4dPFz4xeJoLg2vQGULvMzgYRKiGezwNDzaAxfX57
Encrypted WIF: {
    "encrypted_wif": "6PfMmFWzXobLGrJReqJaNnGcaCMd9T3Xhcwp2jkCHZ6jZoDJ2MnKk15ZuV",
    "confirmation_code": "cfrm38V5JArEGuKEKE8VSMDSKvS8eZXYq3DckKyFDtw76GxW1TBzdKcovWdL4PbQnPLvJ5EpmZp",
    "public_key": "049e60857454bff0635324e132e00f102fbe1ab6b0846b12737eca18a05b473e2a0afa7d996c7b49b03fb4d070d94fd765841f7e172f7727bfceed65e98f940c2d",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "uncompressed",
    "address": "QXsy25WUg3kARS1o4t8si4AsyuwZjLkY9R"
}
Confirm Code: {
    "public_key": "049e60857454bff0635324e132e00f102fbe1ab6b0846b12737eca18a05b473e2a0afa7d996c7b49b03fb4d070d94fd765841f7e172f7727bfceed65e98f940c2d",
    "public_key_type": "uncompressed",
    "address": "QXsy25WUg3kARS1o4t8si4AsyuwZjLkY9R",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "5JDa1CcN3iLbFeexZC2RhyEkFU2B7oieHAVs5YDwieMhgVS9S9c",
    "private_key": "34de039d8e90172f246ec3190fc8bd98e46f11bc5d50d062d0d6f806e43372a9",
    "wif_type": "wif",
    "public_key": "049e60857454bff0635324e132e00f102fbe1ab6b0846b12737eca18a05b473e2a0afa7d996c7b49b03fb4d070d94fd765841f7e172f7727bfceed65e98f940c2d",
    "public_key_type": "uncompressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "QXsy25WUg3kARS1o4t8si4AsyuwZjLkY9R",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseb7ruSNPsLdQF57XQM4waP887G6qoGhPVpDS7jEorTKpfXYFxnUSSVwtpQZPT4U
Encrypted WIF: {
    "encrypted_wif": "6PgLaWLw6fb6uDBtnN6QVyT9AbvN4zFi8E4oLdSiEWCqsHZFAtcY4wP4LW",
    "confirmation_code": "cfrm38V8VJb8xnvVY1kkRRVanmL4F91nfuQAZctydcGYKS8ZjPxyZHnACqfJ3ni1AwaCkDMsWVF",
    "public_key": "04263351adcb7d9298c6865a597ef63094a8e79f35110aab71d29347acd29ddb0c22e139924e329ae9a84b806c27f919c5e60f8f299ed004256109658b5c11b7b7",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "uncompressed",
    "address": "QfAtAjYNEQMAVtxNaXCWcg1rws3ubJJAED"
}
Confirm Code: {
    "public_key": "04263351adcb7d9298c6865a597ef63094a8e79f35110aab71d29347acd29ddb0c22e139924e329ae9a84b806c27f919c5e60f8f299ed004256109658b5c11b7b7",
    "public_key_type": "uncompressed",
    "address": "QfAtAjYNEQMAVtxNaXCWcg1rws3ubJJAED",
    "lot": 567885,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "5KXP2dhbmUsgPAFU6Uu6iY4ePafMc53fLjs9mdQXbmPvoLtxiSj",
    "private_key": "e1013f4521ffeefb06aad092a040189075a5163af3c6cb7ca1622cbea2d498fc",
    "wif_type": "wif",
    "public_key": "04263351adcb7d9298c6865a597ef63094a8e79f35110aab71d29347acd29ddb0c22e139924e329ae9a84b806c27f919c5e60f8f299ed004256109658b5c11b7b7",
    "public_key_type": "uncompressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "QfAtAjYNEQMAVtxNaXCWcg1rws3ubJJAED",
    "lot": 567885,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseondJwvQGEWFNsbiN6AVu4r4dPFz4xeJoLg2vQGULvMzgYRKiGezwNDzaAxfX57
Encrypted WIF: {
    "encrypted_wif": "6PnQ3P5GdsSJSUcJCAmtvn74U9gqPs8JMZLdVBkBYsUvSVd4TjgSZEqB7w",
    "confirmation_code": "cfrm38VUEZdLCyEmCMZqbbvdhUdsuPZdYy2tmBcbDdmdkyFiLyiScPQSeotgvS6vQZjPXhj92Xj",
    "public_key": "039e60857454bff0635324e132e00f102fbe1ab6b0846b12737eca18a05b473e2a",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "compressed",
    "address": "QS3xSF9psn8DMT6uBExPDkm258eJPqJbsB"
}
Confirm Code: {
    "public_key": "039e60857454bff0635324e132e00f102fbe1ab6b0846b12737eca18a05b473e2a",
    "public_key_type": "compressed",
    "address": "QS3xSF9psn8DMT6uBExPDkm258eJPqJbsB",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "KxzUftF5tyTUBfCYD5fJ3qDftrGBf3CoYLvQ32p8WotNYrMW4c3t",
    "private_key": "34de039d8e90172f246ec3190fc8bd98e46f11bc5d50d062d0d6f806e43372a9",
    "wif_type": "wif-compressed",
    "public_key": "039e60857454bff0635324e132e00f102fbe1ab6b0846b12737eca18a05b473e2a",
    "public_key_type": "compressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "QS3xSF9psn8DMT6uBExPDkm258eJPqJbsB",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseb7ruSNDGP7cmphxdxHWx8oo88zHuBBeFyvaWYD2zqHUpLwvXYhqTBnwxiiCUf6
Encrypted WIF: {
    "encrypted_wif": "6PoLtrDYSMopr5nRKDN9LDanSPiSPRQ3vkfmT2gj4c3E3S5FeGTmyuG12z",
    "confirmation_code": "cfrm38VXKJasUvzUJiyuBsX5TqVdhNV4BhzXEE8ge9TAm3Y13jobt5x8BMqcXNEpdDLgumedBBW",
    "public_key": "03548814ac8ce03397f544dfa9bde1d148b503237103362da170fd3f330cf3e094",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "compressed",
    "address": "QQ2yBHc39h3Fyb8AnKuwtw1Soxpq9f4GRt"
}
Confirm Code: {
    "public_key": "03548814ac8ce03397f544dfa9bde1d148b503237103362da170fd3f330cf3e094",
    "public_key_type": "compressed",
    "address": "QQ2yBHc39h3Fyb8AnKuwtw1Soxpq9f4GRt",
    "lot": 369861,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "L3uXqD8dC2zNpRdDVfsmUCNrz6HMXk2j9fVkgftwd3SM35W6XNVL",
    "private_key": "c7829407b0a6aee68539bcc4f58878722ac0f441aa462b303da31ab232253d64",
    "wif_type": "wif-compressed",
    "public_key": "03548814ac8ce03397f544dfa9bde1d148b503237103362da170fd3f330cf3e094",
    "public_key_type": "compressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "QQ2yBHc39h3Fyb8AnKuwtw1Soxpq9f4GRt",
    "lot": 369861,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
```
</details>

## Development

To get started, just fork this repo, clone it locally, and run:

```
pip install -e .[tests] -r requirements.txt
```

## Testing

You can run the tests with:

```
pytest
```

Or use `tox` to run the complete suite against the full set of build targets, or pytest to run specific 
tests against a specific version of Python.

## License

Distributed under the [MIT](https://github.com/qtumproject/qtum-bip38/blob/master/LICENSE) license. See ``LICENSE`` for more information.
