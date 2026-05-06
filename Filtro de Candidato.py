idade = int(input("Digite sua idade: "))
projetos = int(input("Digite a quantidade de projetos no GitHub: "))

if idade >= 18 and projetos >= 5:
    print("Candidato aprovado para entrevista")
else:
    print("Candidato nao atende aos requisitos")