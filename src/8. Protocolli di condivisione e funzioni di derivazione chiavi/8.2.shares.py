from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.SecretSharing import Shamir
import random

# Macro
TOKEN_LENGTH = 16
NUMBER_OF_SHARES = 5
SHARES_FOR_RECONSTRUCTION = 2

# Generazione chiavi
key = get_random_bytes(TOKEN_LENGTH)
shares = Shamir.split(SHARES_FOR_RECONSTRUCTION, NUMBER_OF_SHARES, key)
print("Chiavi:")
for id, share in shares:
  print(f"Indice {id}: {share}")

# Cifratura messaggio
plaintext = "Ciao mondo!".encode()
print(f"Messaggio da cifrare: {plaintext.decode()}")
cipher = AES.new(key, AES.MODE_EAX)
ct, tag = cipher.encrypt_and_digest(plaintext)
ciphertext = cipher.nonce + tag + ct
print(f"Messaggio cifrato: {ciphertext}")

# Ricostruzione chiave
reconstruction = []
for x in range(SHARES_FOR_RECONSTRUCTION):
  id = random.randint(0,len(shares)-1)
  reconstruction.append(shares[id])
  shares.pop(id)
key = Shamir.combine(reconstruction)

# Decifratura messaggio
nonce = ciphertext[:16]
tag = ciphertext[16:32]
cipher = AES.new(key, AES.MODE_EAX, nonce)
try:
  result = cipher.decrypt(ciphertext[32:])
  cipher.verify(tag)
  print(f"Messaggio decifrato: {result.decode()}")
except ValueError:
  if len(reconstruction) < SHARES_FOR_RECONSTRUCTION:
    print("Il numero di chiavi inserite non è sufficiente.")
  else:
    print("Almeno una delle chiavi non è corretta.")
