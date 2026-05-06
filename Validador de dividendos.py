dy = float(input("Digite o Dividend Yield (DY): "))

if dy > 6:
    print("Estrategia de Renda Passiva OK")
elif 4 <= dy <= 6:
    print("Atencao: Rendimento Medio")
else:
    print("Rendimento Baixo")