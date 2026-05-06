nome = input("Digite o nome da criptomoeda: ")
variacao = float(input("Digite a variacao percentual nas ultimas 24h: "))

if variacao > 10:
    print(f"{nome}: Alta Relevante")
elif variacao < -10:
    print(f"{nome}: Correcao Forte")
else:
    print(f"{nome}: Estabilidade")