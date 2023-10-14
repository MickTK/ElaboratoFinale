\newpage
\pagestyle{fancy}
\fancyhead{}
\fancyfoot{}
\fancyfoot[R]{\thepage}

# 1. Ambiente di sviluppo e strumenti

## 1.1. Python

### Librerie

### Codifica e decodifica stringhe
Nel corso dei capitoli andremo a cifrare e a decifrare diversi tipi di dati, tra i quali le stringhe.

Per le stringhe verrà utilizzata la codifica UTF-8 in quanto standard di Python e compatibile con qualsiasi elaboratore moderno.

```python
message = 'Ciao mondo!'
encoded_message = messagge.encode('UTF-8') # b'Ciao mondo!'
decoded_message = encoded_message.decode('UTF-8') # 'Ciao mondo!'
```

### Valori pseudocasuali
