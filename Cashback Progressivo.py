valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 500:
    cashback = valor_compra * 0.10
elif valor_compra >= 200:
    cashback = valor_compra * 0.05
else:
    cashback = 0

print(f"Valor do cashback: R$ {cashback:.2f}")