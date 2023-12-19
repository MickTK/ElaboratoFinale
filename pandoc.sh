#!/bin/bash

pandoc \
--output "Elaborato/bin/Elaborato.pdf" \
--highlight-style tango \
-H "Elaborato/meta/template.tex" \
-V lang=it \
-V geometry:left=2.5cm \
-V geometry:right=2.5cm \
-V geometry:top=3cm \
-V geometry:bottom=3cm \
-V geometry:a4paper \
-V colorlinks=true \
-V linkcolor=black \
-V urlcolor=blue \
-V toccolor=black \
"Elaborato/00. Copertina.md" \
"Elaborato/01. Introduzione.md" \
"Elaborato/02. Algoritmi di hashing.md" \
"Elaborato/03. Generazione numeri pseudo-casuali.md" \
"Elaborato/04. Formati di importazione ed esportazione chiavi.md" \
"Elaborato/05. Schemi di cifratura a chiave privata.md" \
"Elaborato/06. Schemi di cifratura a chiave pubblica.md" \
"Elaborato/07. Schemi di firma digitale.md" \
"Elaborato/08. Protocolli di condivisione e funzioni di derivazione chiavi.md" \
"Elaborato/09. Conclusioni.md" \
"Elaborato/10. Sitografia.md"
