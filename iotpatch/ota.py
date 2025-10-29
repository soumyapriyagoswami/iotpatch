import hashlib

def sign_firmware(fw_path, private_key="iotpatch_secret"):
    """
    Very basic signature using SHA-256 (stub)
    """
    sha = hashlib.sha256()
    with open(fw_path, "rb") as fw:
        sha.update(fw.read())
    sha.update(private_key.encode())
    return sha.hexdigest()


def verify_firmware(signature, fw_path, private_key="iotpatch_secret"):
    expected = sign_firmware(fw_path, private_key)
    return signature == expected
