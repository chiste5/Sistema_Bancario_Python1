import datetime

saldo = 2000
extrato_saque = []
extrato_deposito = []
saque_do_dia = 150

def saque_dia(saque_atual, valor):
    return saque_atual - valor

def sacar(saldo, saque_do_dia):  # 👈 agora recebe dois argumentos!
    valor = float(input("Digite o valor que deseja sacar: "))
    saque_restante = saque_dia(saque_do_dia, valor)

    if saldo > 0 and saque_restante >= 0:
        if valor > 500:
            print("Você não pode sacar um valor acima de R$500,00")
        else:
            print("Você sacou R$", valor)
            saldo -= valor
            saque_do_dia = saque_restante  # 👈 atualiza o limite restante
            extrato_saque.append(-valor)
    else:
        print("Você está sem saldo ou excedeu o limite diário de saque.")

    return saldo, saque_do_dia  # 👈 retorna os dois valores atualizados

def depositar(saldo):
    valor_deposito = float(input("Digite o valor que deseja depositar: "))
    if valor_deposito > 0:
        print("Você depositou o valor de", valor_deposito)
        extrato_deposito.append(valor_deposito)
        saldo += valor_deposito
    else:
        print("Não é possível depositar valores negativos")
    return saldo

def extrato():
    print("Esse é o extrato")

menu = """========== MENU ==========

1. Sacar
2. Depositar
3. Extrato
4. Sair

==========================\n"""

opcao = 0

while opcao != 4:
    opcao = int(input(menu))

    if opcao == 1:
        saldo, saque_do_dia = sacar(saldo, saque_do_dia)
        print("Extrato de saques:", extrato_saque)
        print("Saldo atual:", saldo)
        print("Limite restante de saque diário:", saque_do_dia)
    elif opcao == 2:
        saldo = depositar(saldo)
        print("Saldo atual:", saldo)
    elif opcao == 3:
        extrato_final = extrato_saque + extrato_deposito
        print("========== EXTRATO BANCÁRIO ==========")
        for item in extrato_final:
            print(f"R$ {item:.2f}")
        print("Saldo Final:",saldo)
        print("======================================")
    elif opcao == 4:
        print("Saindo... Volte sempre!")
        break
    else:
        print("Digite uma opção válida!")