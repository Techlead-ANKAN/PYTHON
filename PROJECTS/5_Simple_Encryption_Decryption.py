# Simple Encryption and Decryption

# Encryption:

# Encryption is the process of encoding the data. i.e converting plain text into ciphertext. This conversion is done with a key called an encryption key.

# Decryption:

# Decryption is the process of decoding the encoded data. Converting the ciphertext into plain text. This process requires a key that we used for encryption.

# We require a key for encryption. There are two main types of keys used for encryption and decryption. They are Symmetric-key and Asymmetric-key.


# Symmetric-key Encryption:

# In symmetric-key encryption, the data is encoded and decoded with the same key. This is the easiest way of encryption, but also less secure. The receiver needs the key for decryption, so a safe way need for transferring keys. Anyone with the key can read the data in the middle.
from cryptography.fernet import Fernet

msg = input("Enter string: ")

key = Fernet.generate_key()

fernet = Fernet(key)

encmsg = fernet.encrypt(msg.encode())

print(f"Original String: {msg}")
print(f"Encrypted String: {encmsg}")

decmsg = fernet.decrypt(encmsg).decode()

print(f"Decrypted string: {decmsg}") 


# Asymmetric-key Encryption:

# In Asymmetric-key Encryption, we use two keys a public key and a private key. The public key is used to encrypt the data and the private key is used to decrypt the data. By the name, the public key can be public (can be sent to anyone who needs to send data). No one has your private key, so no one in the middle can read your data.

import rsa

public_key, private_key = rsa.newkeys(200)    # rsa.newkeys(length of the keys (atleast 16)) 

msg = input("Enter string: ")

encmsg = rsa.encrypt(msg.encode(), public_key)

print(f"Original String: {msg}")
print(f"Encrypted String: {encmsg}")

decmsg = rsa.decrypt(encmsg, private_key).decode()

print(f"Decrypted String: {decmsg}")