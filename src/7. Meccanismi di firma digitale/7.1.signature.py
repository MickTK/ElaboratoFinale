from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import os

# Informazioni sui file
PRIVATEKEY = os.path.dirname(os.path.realpath(__file__)) + '/7.1.private.pem'
PUBLICKEY = os.path.dirname(os.path.realpath(__file__)) + '/7.1.public.pem'
SIGNATURE = os.path.dirname(os.path.realpath(__file__)) + '/7.1.signature.p7s'
DOCUMENT = os.path.dirname(os.path.realpath(__file__)) + '/7.1.agreement.pdf'

# Operazioni
print('Operazione da eseguire:')
print('1) Genera chiavi')
print('2) Firma documento')
print('3) Verifica firma del documento')
op = input()

# Genera chiavi
if op == '1':
  key = RSA.generate(2048)
  private_key = key.export_key()
  public_key = key.publickey().export_key()
  with open(PRIVATEKEY, 'wb') as private_file, open(PUBLICKEY, 'wb') as public_file:
    private_file.write(private_key)
    public_file.write(public_key)
  print('Le chiavi sono state generate con successo.')

# Firma documento
elif op == '2':
  # Lettura documento
  with open(DOCUMENT, 'rb') as file:
    document = file.read()
  # Lettura chiave privata
  with open(PRIVATEKEY, 'rb') as file:
    key = RSA.import_key(file.read())
  # Hashing del documento
  h = SHA256.new(document)
  # Firma
  signature = pss.new(key).sign(h)
  # Salvataggio firma
  with open(SIGNATURE, 'wb') as file:
    file.write(signature)
  print('Il documento è stato firmato con successo.')

# Verifica firma del documento
elif op == '3':
  # Lettura chiave pubblica
  with open(PUBLICKEY, 'rb') as file:
    key = RSA.import_key(file.read())
  # Lettura documento
  with open(DOCUMENT, 'rb') as file:
    document = file.read()
  # Hashing del documento
  h = SHA256.new(document)
  # Lettura firma
  with open(SIGNATURE, 'rb') as file:
    signature = file.read()
  # Verifica firma
  try:
    pss.new(key).verify(h, signature)
    print('La firma è autentica.')
  except (ValueError, TypeError):
    print('La firma non è autentica.')
