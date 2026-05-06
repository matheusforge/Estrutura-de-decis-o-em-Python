valor = float(input("Digite o valor acumulado: "))

if valor >= 25000:
    print("Partiu America do Norte")
else:
    falta = 25000 - valor
    print(f"Faltam R$ {falta} para atingir a meta")