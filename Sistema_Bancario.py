import datetime

saldo = 2000
extrato_saque = []
extrato_deposito = []
data_hora_saque = []
data_hora_deposito = []
saque_do_dia = 1500
limite_dia_t = 10
data_atual = datetime.datetime.today()

def saque_dia(saque_atual, valor):
    return saque_atual - valor

def sacar(saldo, saque_do_dia, limite_dia_t,data_atual):
    valor = float(input("Digite o valor que deseja sacar: "))
    saque_restante = saque_dia(saque_do_dia, valor)

    if saldo > 0 and saque_restante >= 0 and limite_dia_t>0:
        if valor > 500:
            print("Você não pode sacar um valor acima de R$500,00")
        else:
            print("Você sacou R$", valor)
            saldo -= valor
            limite_dia_t-=1
            saque_do_dia = saque_restante
            data_formatada = data_atual.strftime("%d-%m-%Y %H:%M")
            data_hora_saque.append(data_formatada) 
            extrato_saque.append(-valor)
    else:
        print("Você está sem saldo ou excedeu o limite diário de transações")

    return saldo, saque_do_dia, limite_dia_t

def depositar(saldo,limite_dia_t,data_atual):
    valor_deposito = float(input("Digite o valor que deseja depositar: "))
    if valor_deposito > 0 and limite_dia_t>0:
        print("Você depositou o valor de", valor_deposito)
        extrato_deposito.append(valor_deposito)
        data_formatada = data_atual.strftime("%d-%m-%Y %H:%M")
        data_hora_deposito.append(data_formatada)
        saldo += valor_deposito
        limite_dia_t-=1
    else:
        print("Você está tentando depositar um valor negativo ou atendeu o limite diário de transações")
    return saldo, limite_dia_t

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
        saldo, saque_do_dia, limite_dia_t= sacar(saldo, saque_do_dia, limite_dia_t, data_atual)
        print("Extrato de saques:", extrato_saque)
        print("Saldo atual:", saldo)
        print("Limite restante de saque diário:", saque_do_dia)
        print("Data:",data_hora_saque)
        print(limite_dia_t)
    elif opcao == 2:
        saldo, limite_dia_t = depositar(saldo,limite_dia_t,data_atual)
        print("Saldo atual:", saldo)
        print(limite_dia_t)
    elif opcao == 3:
        extrato_final = extrato_saque + extrato_deposito
        data_final = data_hora_saque+data_hora_deposito
        print("========== EXTRATO BANCÁRIO ==========")
        for item, data in zip(extrato_final, data_final):
                print(f"{data}    R$ {item:.2f}")
        print("Saldo Final:",saldo)
        print("======================================")
    elif opcao == 4:
        print("Saindo... Volte sempre!")
        break
    else:
        print("Digite uma opção válida!")