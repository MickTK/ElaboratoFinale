#!/bin/bash

pandoc \
--output "Elaborato/bin/Elaborato.pdf" \
-H "Elaborato/meta/packages.tex" \
-V lang=it \
-V geometry:left=2.5cm \
-V geometry:right=2.5cm \
-V geometry:top=3cm \
-V geometry:bottom=3cm \
-V geometry:a4paper \
"Elaborato/00 - Copertina.md" \
"Elaborato/01 - Introduzione.md" \
"Elaborato/02 - Capitolo 1.md" \
"Elaborato/03 - Capitolo 2.md" \
# "Elaborato/04 - Capitolo 3.md" \
# "Elaborato/05 - Capitolo 4.md" \
# "Elaborato/06 - Capitolo 5.md" \
# "Elaborato/07 - Capitolo 6.md" \
# "Elaborato/08 - Conclusioni.md"
