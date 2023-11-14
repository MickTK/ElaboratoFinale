#!/bin/bash

pandoc \
--highlight-style tango \
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
"Elaborato/02. Algoritmi di hashing.md" \
"Elaborato/03. Generazione valori casuali.md" \
"Elaborato/04. Formati di importazione ed esportazione chiavi.md" \
"Elaborato/05. Schemi di cifratura a chiave privata.md" \
"Elaborato/06. Schemi di cifratura a chiave pubblica.md" \
"Elaborato/07. Meccanismi di firma digitale.md" \
#"Elaborato/08. Protocolli.md" \
#"Elaborato/09. Conclusioni.md" \
