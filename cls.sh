#!/bin/bash

file_list=(
  "src/Capitolo 2/2.1.digested_password.txt"
  "src/Capitolo 3/3.2.key.pem"
  "src/Capitolo 3/3.2.message.txt"
  "src/Capitolo 3/3.3.decripted_image.jpg"
  "src/Capitolo 3/3.3.encripted_image.jpg"
)

for file in "${file_list[@]}"; do
  [ -f "$file" ] && rm "$file"
done
