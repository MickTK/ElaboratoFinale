import hmac, os, json

# Nome del file che conterrà il codice di autenticazione del messaggio
FILENAME = os.path.dirname(os.path.realpath(__file__)) + '/2.3.message.txt'

SECRET = 'chiavesegreta123' # Chiave privata (condivisa)

# Operazioni
print('Operazione da eseguire:')
print('1) Genera un messaggio con codice mac')
print('2) Autentica un messaggio')
op = input()

# Genera un codice mac
if op == '1':
  text_message = input('Messaggio: ') # Messaggio da inoltrare
  # Inizializzazione dell'oggetto HMAC e digestione del messaggio
  HMAC = hmac.new(SECRET.encode(), text_message.encode(), 'sha256')
  mac = HMAC.hexdigest()
  message = { 'text': text_message, 'mac': mac }
  message = json.dumps(message)
  # Salvataggio del messaggio su file
  with open(FILENAME, 'wb') as file:
    file.write(message.encode())
    print('Il messaggio è stato salvato su file.')

# Autentica un messaggio
elif op == '2':
  # Se il file contenente il messaggio esiste
  if os.path.exists(FILENAME):
    # Viene letto il messaggio
    with open(FILENAME, 'rb') as file:
      message = file.read().decode()
      message = json.loads(message)
    # Inizializzazione dell'oggetto HMAC
    HMAC = hmac.new(SECRET.encode(), message['text'].encode(), 'sha256')
    # Esegue la verifica del mac
    if hmac.compare_digest(message['mac'], HMAC.hexdigest()):
      print('Il messaggio è autentico.')
    else:
      print('Il messaggio NON è autentico.')
  # Se il file contenente il messaggio non è presente nella cartella corrente
  else:
    print('Non è stato trovato nessun messaggio.')
