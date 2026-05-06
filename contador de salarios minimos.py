salario_minimo = 1600.0

salario = float(input("Digite o seu salário: R$ "))

if salario <= salario_minimo:
    print("voce recebe um salario minimo ou menos, trabalhe mais!")
else:
    quantidade = salario / salario_minimo
    print(f"voce recebe {quantidade:.2f} salarios minimos")