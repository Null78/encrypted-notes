from Crypto.Cipher import AES
from Crypto.Util.Padding import pad



def encrypt(key: str, data: str):
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    return ciphertext, cipher.iv

def decrypt(key, iv, data):
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC, iv)
    return cipher.decrypt(data)