# Il seguente script permette di cifrare e decifrare un messaggio tramite chiave pubblica.

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os

# Informazioni sui file
PRIVATEKEY = os.path.dirname(os.path.realpath(__file__)) + "/6.1.private.pem"
PUBLICKEY = os.path.dirname(os.path.realpath(__file__)) + "/6.1.public.pem"
ENCRYPTEDMESSAGE = os.path.dirname(os.path.realpath(__file__)) + "/6.1.encrypted.txt"

# Operazioni
print('Operazione da eseguire:')
print('1) Genera chiavi (privata e pubblica)')
print('2) Scrivi un messaggio')
print('3) Leggi un messaggio')
op = input()

# Generazione chiavi (privata e pubblica)
if op == '1':
  # Generazione chiavi
  key = RSA.generate(2048) # 256B
  # Suddivisione chiavi
  private_key = key.export_key()
  public_key = key.publickey().export_key()
  # Scrittura chiavi su file
  with open(PRIVATEKEY, "wb") as private_file, open(PUBLICKEY, "wb") as public_file:
    private_file.write(private_key)
    public_file.write(public_key)
  print('Le chiavi sono state generate con successo.')

# Scrittura di un messaggio
elif op == '2':
  # Raccolta messaggio da trasmettere
  message = input('Messaggio da trasmettere: ').encode()
  # Importazione chiave pubblica
  public_key = RSA.import_key(open(PUBLICKEY).read())
  rsa = PKCS1_OAEP.new(public_key)
  # Generazione e cifratura chiave di sessione
  session_key = get_random_bytes(AES.block_size)
  encrypted_session_key = rsa.encrypt(session_key)
  # Cifratura messaggio tramite chiave di sessione
  aes = AES.new(session_key, AES.MODE_EAX)
  ciphertext, tag = aes.encrypt_and_digest(message)
  # Scrittura informazioni su file
  with open(ENCRYPTEDMESSAGE, "wb") as file_out:
    for x in (encrypted_session_key, aes.nonce, tag, ciphertext):
      file_out.write(x)
  print('Il messaggio è stato spedito.')

# Lettura di un messaggio
elif op == '3':
  # Importazione chiave privata
  private_key = RSA.import_key(open(PRIVATEKEY).read())
  # Lettura informazioni dal file
  with open(ENCRYPTEDMESSAGE, "rb") as file_in:
    data = [ file_in.read(x) for x in (
      private_key.size_in_bytes(),
      AES.block_size, # Nonce
      AES.block_size, # Tag
      -1
    )]
    encrypted_session_key, nonce, tag, ciphertext = data
  # Decifratura chiave di sessione con chiave privata
  rsa = PKCS1_OAEP.new(private_key)
  try:
    session_key = rsa.decrypt(encrypted_session_key)
  except ValueError:
    print('La chiave privata non è in grado di decifrare il messaggio.')
    exit()
  # Decifratura messaggio con chiave di sessione
  aes = AES.new(session_key, AES.MODE_EAX, nonce)
  message = aes.decrypt_and_verify(ciphertext, tag)
  print('Messaggio ricevuto:', message.decode())
