menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

LIMITE_SAQUES = 3
LIMITE = 500.0
saldo = 0.0
extrato = ""
numero_saques = 0

while True:

    opcao = input(menu)

    if(opcao == "d"):
        valor_deposito = float(input("Insira a quantidade que vai ser depositada: "))

        if(valor_deposito > 0):
            saldo += valor_deposito
            print("Depósito realizado com sucesso!")
            extrato += f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!\n"

        else:
            print("Valor de depósito inválido! Tente novamente.")

    elif(opcao == "s"):

        if(numero_saques == LIMITE_SAQUES):
            print("Limite diário de saque excedido! Tente novamente amanhã")
            continue

        valor_saque = float(input("Insira o valor a ser sacado: "))
        if(valor_saque > LIMITE):
            print(f"Limite de operação excedido, não é possivel realizar um saque maior que R$ {LIMITE:.2f}. Tente realizar uma nova operação.")
            continue
        
        elif(valor_saque > saldo):
            print("Saldo insuficiente! Tente novamente.")
        
        else:
            saldo -= valor_saque
            numero_saques += 1
            print("Saque realizado com sucesso!")
            extrato += f"Saque de R$ {valor_saque:.2f} realizado com sucesso!\n"
    
    elif(opcao == "e"):
        print("================ EXTRATO =================")
        if not extrato:
            print(f"Não foram realizadas movimentações!\n")
        else:
            print(extrato)
        
        print(f"Saldo em conta: R$ {saldo:.2f}")
        print("===========================================")
    
    elif(opcao == "q"):
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")