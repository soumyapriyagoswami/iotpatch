from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import base64

def generate_key():
    return get_random_bytes(16)  # AES-128


def pad(data: bytes) -> bytes:
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len


def unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]


def encrypt_data(data: bytes, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data))
    return base64.b64encode(cipher.iv + ciphertext).decode()


def decrypt_data(enc_data: str, key: bytes) -> bytes:
    raw = base64.b64decode(enc_data)
    iv, ciphertext = raw[:16], raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext))


def hash_file(path: str) -> str:
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()
