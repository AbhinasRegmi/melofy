import os
import binascii


def generate_random_hash() -> str:
    return binascii.hexlify(os.urandom(16)).decode()