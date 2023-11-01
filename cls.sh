#!/bin/bash

file_list=(
  "src/2. Hashing/2.1.digested_password.txt"
  "src/2. Hashing/2.3.message.txt"
  "src/5. Cifratura/5.1.key.pem"
  "src/5. Cifratura/5.1.message.txt"
  "src/5. Cifratura/5.2.decripted_image.jpg"
  "src/5. Cifratura/5.2.encripted_image.jpg"
)

for file in "${file_list[@]}"; do
  [ -f "$file" ] && rm "$file"
done
