texto = "Exemplo de string"

texto_invertido = ""

for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]

print("Texto original:", texto)
print("Texto invertido:", texto_invertido)
