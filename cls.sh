#!/bin/bash

file_list=(
  "src/2. Algoritmi di hashing/2.1.digested_password.txt"
  "src/2. Algoritmi di hashing/2.3.message.txt"
  "src/5. Schemi di cifratura a chiave privata/5.1.key.pem"
  "src/5. Schemi di cifratura a chiave privata/5.1.message.txt"
  "src/5. Schemi di cifratura a chiave privata/5.2.decripted_image.jpg"
  "src/5. Schemi di cifratura a chiave privata/5.2.encripted_image.jpg"
  "src/6. Schemi di cifratura a chiave pubblica/6.1.private.pem"
  "src/6. Schemi di cifratura a chiave pubblica/6.1.public.pem"
  "src/6. Schemi di cifratura a chiave pubblica/6.1.encrypted.txt"
  "src/7. Schemi di firma digitale/7.1.public.pem"
  "src/7. Schemi di firma digitale/7.1.private.pem"
  "src/7. Schemi di firma digitale/7.1.signature.p7s"
)

for file in "${file_list[@]}"; do
  [ -f "$file" ] && rm "$file"
done
