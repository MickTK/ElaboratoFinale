# Il seguente script cifra un file e decifra il file cifrato, ottenendo un'immagine cifrata e due immagini in chiaro (quella originale e quella decifrata).

import os
import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Informazioni sul file da cifrare/decifrare
FILENAME = os.path.dirname(os.path.realpath(__file__)) + "/5.2.image.jpg"
ENCRIPTED_FILENAME = os.path.dirname(os.path.realpath(__file__)) + "/5.2.encripted_image.jpg"
DECRIPTED_FILENAME = os.path.dirname(os.path.realpath(__file__)) + "/5.2.decripted_image.jpg"

IV_LENGTH = AES.block_size # Lunghezza vettore iniziale (byte)
KEY_LENGTH = 16            # Lunghezza chiave (byte) (AES-128 -> 16B)
RESERVED_BYTES = 64        # Byte riservati ai metadata

# Generazione valori
iv = secrets.token_bytes(IV_LENGTH)
key = secrets.token_bytes(KEY_LENGTH)

# Cifratura file
def encrypt(file_in, file_out):
  # Inizializzazione cifrario
  cipher = AES.new(key, AES.MODE_CBC, iv)
  # Lettura file da cifrare
  with open(file_in, "rb") as file:
    byteblock = file.read()
  # Padding dei dati da cifrare
  plaintext = pad(byteblock[RESERVED_BYTES:], AES.block_size)
  # Cifratura dati
  ciphertext = byteblock[:RESERVED_BYTES] + cipher.encrypt(plaintext)
  # Scrittura file con dati cifrati
  with open(file_out, "wb") as file:
    file.write(ciphertext)

# Decifratura file
def decrypt(file_in, file_out):
  # Inizializzazione cifrario
  cipher = AES.new(key, AES.MODE_CBC)
  # Lettura file da decifrare
  with open(file_in, "rb") as file:
    byteblock = file.read()
  # Decifratura dati
  plaintext = cipher.decrypt(byteblock[RESERVED_BYTES:])
  # Unpadding dei dati da decifrare
  plaintext = unpad(plaintext, AES.block_size)
  # Concatenazione byte riservati con dati decifrati
  plaintext = byteblock[:RESERVED_BYTES] + plaintext
  # Scrittura dati decifrati
  with open(file_out, "wb") as file:
    byteblock = file.write(plaintext)

encrypt(FILENAME, ENCRIPTED_FILENAME)
decrypt(ENCRIPTED_FILENAME, DECRIPTED_FILENAME)
