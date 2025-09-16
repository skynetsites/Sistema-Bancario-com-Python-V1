menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis principais
saldo = 0.0
limite = 500.0
movimentacoes = []
saques_realizados = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            movimentacoes.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite permitido.")
        elif saques_realizados >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            saldo -= valor
            movimentacoes.append(f"Saque: R$ {valor:.2f}")
            saques_realizados += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not movimentacoes:
            print("Não foram realizadas movimentações.")
        else:
            for item in movimentacoes:
                print(item)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Saindo do sistema. Obrigado por utilizar nosso banco!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
