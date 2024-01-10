# Il seguente script prende in input una password, esegue l'hashing e salva il risultato su file.
# Successivamente viene chiesto all'utente di reinserire la password, effettuando un confronto dell'hash value con il valore precedentemente salvato su file.

from Crypto.Hash import SHA512
import os

# Nome del file che contiene la password cifrata
FILENAME = os.path.dirname(os.path.realpath(__file__)) + "/2.1.digested_password.txt"

# Richiesta di inserimento password
password = input("Inserire una nuova password: ")
# Se è stata inserita una password
if password != "":
  # Viene eseguita la digestione della password
  hashing = SHA512.new(password.encode())
  digest = hashing.hexdigest()
  # Salva la password cifrata in un file
  with open(FILENAME, 'wb') as file:
    file.write(digest.encode())
    print("Password salvata.")
  # Legge la password cifrata dal file
  with open(FILENAME, 'rb') as file:
    digest = file.read()

  while True:
    # Chiede all'utente di reinserire la password
    password = input("Reinserire la password: ")
    # Viene eseguita la digestione della password inserita
    hashing = SHA512.new(password.encode())
    digested_password = hashing.hexdigest()
    # Legge la password cifrata presente sul file
    with open(FILENAME, 'rb') as file:
      digest = file.read().decode()
    # Se la digestione produce lo stesso risultato presente nel file
    if digested_password == digest:
      # La password inserita corrisponde a quella presente sul file
      print("Password accettata.")
      break
    else:
      # La password inserita non corrisponde a quella presente sul file
      print("Password rifiutata. La password non corrisponde quella precedentemente inserita.")
