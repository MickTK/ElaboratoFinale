#!/bin/bash

file_list=(
  "src/Capitolo 2/2.1.digested_password.txt"
)

for file in "${file_list[@]}"; do
  [ -f "$file" ] && rm "$file"
done
