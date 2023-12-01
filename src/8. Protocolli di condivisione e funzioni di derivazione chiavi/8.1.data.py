# Il seguente script prende in input dall'utente una password e un dato sensibile, andando a cifrare tramite chiave derivata tale dato.

from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad

# Macro
TOKEN_LENGTH = 16
SCRYPT_PARAMS = (2**14, 8, 1)

# Master key
password = input('Password: ').encode()

# Dati sensibili da cifrare
plaintext = input('Messaggio da cifrare: ').encode()

data = {}

# Hashing password
hashing = SHA256.new(password)
hash = hashing.hexdigest()
data["hash"] = hash

# Generazione chiave derivata
salt = get_random_bytes(TOKEN_LENGTH)
secondary_key = scrypt(
  password,
  salt,
  TOKEN_LENGTH,
  N=SCRYPT_PARAMS[0],
  r=SCRYPT_PARAMS[1],
  p=SCRYPT_PARAMS[2]
)

# Cifratura dati sensibili
iv = get_random_bytes(TOKEN_LENGTH)
cipher = AES.new(secondary_key, AES.MODE_CBC, iv)
padded_plaintext = pad(plaintext, AES.block_size)
data["ciphertext"] = salt + iv + cipher.encrypt(padded_plaintext)

print('Data', data)
