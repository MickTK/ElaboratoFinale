from Crypto.Cipher import Salsa20
import secrets
import os

# Nomi dei file che contengono la chiave e il messaggio cifrato
KEY_FILENAME = os.path.dirname(os.path.realpath(__file__)) + "/3.2.key.pem"
MESSAGE_FILENAME = os.path.dirname(os.path.realpath(__file__)) + "/3.2.message.txt"

# Se non esiste un file con la chiave
if not os.path.exists(KEY_FILENAME):
  # Viene chiesto l'inserimento di un messaggio da cifrare
  plaintext = input("Inserire un messaggio da cifrare: ").encode()
  # Viene generata e salvata su file una chiave privata
  key = secrets.token_bytes(32)
  with open(KEY_FILENAME, 'wb') as file:
    file.write(key)
  # Viene inizializzato l'oggetto che effettuerà la cifratura
  cipher = Salsa20.new(key)
  # Viene cifrato e salvato su file il messaggio inserito precedentemente
  message = cipher.nonce + cipher.encrypt(plaintext)
  with open(MESSAGE_FILENAME, 'wb') as file:
    file.write(message)
    print("Il messaggio cifrato è stato salvato su file.")

# Se esiste sia il file con la chiave sia il file con il messaggio cifrato
elif os.path.exists(KEY_FILENAME) and os.path.exists(MESSAGE_FILENAME):
  # Viene letto il messaggio
  with open(MESSAGE_FILENAME, 'rb') as file:
    message = file.read()
  # Viene suddiviso il messaggio in nonce e testo cifrato
  nonce, ciphertext = message[:8], message[8:]
  # Viene letta la chiave
  with open(KEY_FILENAME, 'rb') as file:
    key = file.read()
    # Viene inizializzato l'oggetto che effettuerà la decifratura
    cipher = Salsa20.new(key, nonce)
    # Viene decifrato e decodificato il messaggio
    plaintext = cipher.decrypt(ciphertext).decode()
    print("Messaggio decifrato:", plaintext)
