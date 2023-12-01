# Il seguente script cifra un messaggio inserito dall'utente, stampa a video le informazioni prodotte dall'algoritmo di cifratura ed esegue la decifratura, mostrando a video il messaggio ottenuto.

from base64 import b64encode, b64decode
from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes

# Cifratura
header = 'Informazioni generiche'.encode()
plaintext = input('Messaggio da cifrare: ').encode()
key = get_random_bytes(32)
cipher = ChaCha20_Poly1305.new(key=key)
cipher.update(header)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
data = {
  'nonce': b64encode(cipher.nonce).decode('utf-8'),
  'header': b64encode(header).decode('utf-8'),
  'ciphertext': b64encode(ciphertext).decode('utf-8'),
  'tag': b64encode(tag).decode('utf-8')
}
print('Data:', data)

# Decifratura con autenticazione
try:
  nonce = b64decode(data['nonce'])
  header = b64decode(data['header'])
  ciphertext = b64decode(data['ciphertext'])
  tag = b64decode(data['tag'])
  cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)
  cipher.update(header)
  plaintext = cipher.decrypt_and_verify(ciphertext, tag)
  print('Messaggio decifrato: ' + plaintext.decode())
except (ValueError, KeyError):
  print('Si è verificato un errore durante la decifratura.')
