# Il seguente script simula un sistema di concessione permessi, permettendo ad un utente di richiedere dei permessi speciali ad un utente amministratore. Quest'ultimo può o meno concedere tali permessi.

from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

# Utente amministratore
class SuperUser:
  # Costruttore
  def __init__(self, username, password):
    self.username = username
    key = ECC.generate(curve = 'P-256')
    self._private_key = key.export_key(
      format = 'PEM',
      use_pkcs8 = True,
      passphrase = password,
      protection = 'PBKDF2WithHMAC-SHA1AndAES128-CBC'
    )
    self.public_key = key.public_key()
  # Concessione permessi ad un utente semplice
  def _grant_permissions_to_user(self, operation_token, password):
    try:
      key = ECC.import_key(self._private_key, passphrase = password)
      print('Password accettata.')
    except ValueError:
      print('Password rifiutata.')
      return ''
    # Firma del token di operazione
    hash = SHA256.new(operation_token)
    signer = DSS.new(key, 'fips-186-3')
    return signer.sign(hash)
  # Richiesta permessi da parte di un utente semplice
  def permissions_request(self, user):
    # Messaggio di richiesta permessi
    print(f'Vuoi concedere i permessi a {user.username}? [Si/No]')
    print(f'Token: {user.operation_token}')
    if input().lower() == 'si':
      password = input('Inserire password amministratore: ')
      return self._grant_permissions_to_user(user.operation_token, password)
    else:
      return ''

# Utente semplice
class User:
  # Costruttore
  def __init__(self, username, superuser):
    self.username = username
    self.superuser = superuser
  # Svolge un'operazione che richiede permessi speciali
  def do_something_with_permissions(self):
    # Generazione token operazione
    self.operation_token = get_random_bytes(16)
    # Richiesta permessi
    signature = self.superuser.permissions_request(self)
    # Inizializzazione oggetti per la verifica
    hash = SHA256.new(self.operation_token)
    verifier = DSS.new(self.superuser.public_key, 'fips-186-3')
    # Verifica permessi
    try:
      verifier.verify(hash, signature)
      print('Permessi concessi.')
    except ValueError:
      print('Permessi NON concessi.')
    # Ripristino token
    self.operation_token = None

# Sistema
superuser = SuperUser('Mario', 'password')
user = User('Luigi', superuser)
user.do_something_with_permissions()
