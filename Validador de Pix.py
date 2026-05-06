valor = float(input("Digite o valor da transferencia: "))
saldo = float(input("Digite o saldo atual: "))

if saldo >= valor:
    print("Transacao realizada")
else:
    cheque = float(input("Digite o limite do cheque especial: "))

    if (saldo + cheque) >= valor:
        print("Transacao via Cheque Especial")
    else:
        print("Saldo Insuficiente")