valor = float(input("Digite o valor do investimento: "))
meses = int(input("Digite o prazo em meses: "))

if meses > 12:
    taxa = 0.12
else:
    taxa = 0.08

print(f"A taxa aplicada sera de {taxa * 100}% ao ano")