import binascii
import secrets
import string

# Conversione di un messaggio da stringa a intero
def toInt(message):
  msg = message.encode()      # Conversione in binario
  msg = binascii.hexlify(msg) # Conversione in esadecimale
  msg = int(msg, 16)          # Conversione in intero
  return msg

# Conversione di un messaggio da intero a stringa
def toStr(message):
  msg = format(message, 'x')         # Conversione in esadecimale
  msg = ('0' * (len(msg) % 2)) + msg # Padding del messaggio
  msg = binascii.unhexlify(msg)      # Conversione in binario
  msg = msg.decode()                 # Conversione in stringa
  return msg

# Generazione chiave casuale
def genKey(length):
  key = ''
  for i in range(length):
    key += secrets.choice(string.ascii_letters)
  return key

message = 'Ciao mondo!'
print("Messaggio:", message)
key = genKey(len(message))
print("Chiave:", key)
encrypted_message = toInt(message) ^ toInt(key)
print("Messaggio cifrato:", toStr(encrypted_message))
decrypted_message = toStr(encrypted_message ^ toInt(key))
print("Messaggio decifrato:", decrypted_message)
