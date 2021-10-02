from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


key = b'ctfchallengekeyy'

cipher = AES.new(key,AES.MODE_CBC)
plaintext = b'this is my super secret message to encrypt'
ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))

print(ciphertext)

with open('cipher_file','wb')as c_file:
    c_file.write(cipher.iv)
    c_file.write(ciphertext)
