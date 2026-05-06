idade = int(input("Digite a idade do jogador: "))

if 12 <= idade <= 14:
    print("Categoria: Mirim")
elif 15 <= idade <= 17:
    print("Categoria: Junior")
elif 18 <= idade <= 25:
    print("Categoria: Profissional")
else:
    print("Categoria: Master")