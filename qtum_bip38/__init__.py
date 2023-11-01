#!/usr/bin/env python3

# Copyright © 2023, Meheret Tesfaye Batu <meherett@qtum.info>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import List

from .bip38 import (
    uncompress_public_key,
    compress_public_key,
    private_key_to_public_key,
    private_key_to_wif,
    wif_to_private_key,
    get_wif_type,
    get_wif_checksum,
    get_wif_network,
    public_key_to_addresses,
    bip38_encrypt,
    bip38_decrypt,
    intermediate_code,
    create_new_encrypted_wif,
    confirm_code
)

__version__, __license__, __author__, __email__, __description__ = (
    "v0.3.0",
    "MIT",
    "Meheret Tesfaye Batu",
    "meherett@qtum.info",
    "Python library for implementation of BIP38 for Qtum."
)

__all__: List[str] = [
    "uncompress_public_key",
    "compress_public_key",
    "private_key_to_public_key",
    "private_key_to_wif",
    "wif_to_private_key",
    "get_wif_type",
    "get_wif_checksum",
    "get_wif_network",
    "public_key_to_addresses",
    "bip38_encrypt",
    "bip38_decrypt",
    "intermediate_code",
    "create_new_encrypted_wif",
    "confirm_code",

    "__version__",
    "__license__",
    "__author__",
    "__email__",
    "__description__",
]
