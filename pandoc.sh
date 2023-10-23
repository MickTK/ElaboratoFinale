#!/bin/bash

pandoc \
--output "Elaborato/bin/Elaborato.pdf" \
-H "Elaborato/meta/template.tex" \
-V lang=it \
-V geometry:left=2.5cm \
-V geometry:right=2.5cm \
-V geometry:top=3cm \
-V geometry:bottom=3cm \
-V geometry:a4paper \
"Elaborato/00. Copertina.md" \
"Elaborato/00. Introduzione.md" \
"Elaborato/01. Ambiente di sviluppo e strumenti.md" \
"Elaborato/02. Hashing.md" \
"Elaborato/03. Cifratura simmetrica.md" \
