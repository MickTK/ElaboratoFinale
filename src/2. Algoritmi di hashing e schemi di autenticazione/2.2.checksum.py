# Il seguente script prende in ingresso il nome di un file. Se il file esiste, restituisce i valori di checksum prodotti, altrimenti stampa a video un messaggio di errore.

from Crypto.Hash import MD5, SHA256
import os

# Dimensione dei blocchi da leggere su file
BLOCKSIZE = 65536

# File d'esempio
# Link del file: https://file-examples.com/storage/feaade38c1651bd01984236/2017/04/file_example_MP4_480_1_5MG.mp4
EXPECTED_DIGEST_FOR_MD5 = "d9061d3da8601932e98f79ec8ba1c877"
EXPECTED_DIGEST_FOR_SHA256 = "71944d7430c461f0cd6e7fd10cee7eb72786352a3678fc7bc0ae3d410f72aece"

# Richiesta di inserimento nome del file di cui calcolare i checksum
filename = input("Inserire nome del file: ")

# Se il file esiste
if filename != "" and os.path.exists(filename):

  # Dichiarazione classi di hashing
  md5 = MD5.new()
  sha256 = SHA256.new()

  # Lettura del file
  with open(filename,"rb") as file:
    buffer = file.read(BLOCKSIZE)
    while len(buffer) > 0:
      # Incorporamento dei blocchi
      md5.update(buffer)
      sha256.update(buffer)
      buffer = file.read(BLOCKSIZE)

  # Digestione
  md5_digest = md5.hexdigest()
  sha256_digest = sha256.hexdigest()

  # Risultati
  print("Checksum (MD5): " + md5_digest)
  print("Checksum (SHA256): " + sha256_digest)

# Se il file non esiste
else:
  print("Non è stato trovato nessun file chiamato: " + filename)
