import datetime

saldo = 2000
extrato_saque = []
extrato_deposito = []
data_hora_saque = []
data_hora_deposito = []
usuario_lista =[]
usuario_contas = []
saque_do_dia = 1500
limite_dia_t = 10
data_atual = datetime.datetime.today()

class Usuario:
    def criarUsuario(nome,data_nas,cpf,log,num,bairro,cidade,UF):
        usuario = {
            "nome":nome,
            "data_nasc": data_nas,
            "cpf": cpf,
            "endereco":{
                "logradouro": log,
                "numero": num,
                "bairro": bairro,
                "cidade": cidade,
                "UF": UF
            }
        }
        usuario_lista.append(usuario)
        print(usuario_lista)
        return usuario

class Conta:
    def criarContaCorrente(num_conta,usuario):
        conta = {
            "agencia": "0001",
            "num_conta": num_conta,
            "usuario": usuario
        }
        usuario_contas.append(conta)
        print(usuario_contas)
        return conta

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
4. Cadastar Usuário
5. Cadastrar Conta
6. Listar Usuários
7. Listar Contas
8. Sair

==========================\n"""

opcao = 0

while opcao != 8:
    opcao = int(input(menu))

    if opcao == 1:
        saldo, saque_do_dia, limite_dia_t= sacar(saldo=saldo, saque_do_dia=saque_do_dia, limite_dia_t= limite_dia_t, data_atual=data_atual)
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

        print("Bem vindo ao cadastro de Usuários")
        nome = input("Digite seu nome:")
        data_nas = input("Digite sua data de nascimento:")
        cpf = input("Digite seu cpf:")
        logradouro = input("Digite seu endereço:")
        numero = input("Digite o numero:")
        bairro = input("Digite o bairro:")
        cidade = input("Digite sua cidade:")
        uf = input("Digite seu estado:")
           
        Usuario.criarUsuario(nome,data_nas,cpf,logradouro,numero,bairro,cidade,uf)
        print("Usuário Cadastrado com sucesso")

    elif opcao ==5:
        print("Bem Vindo ao cadastro de Contas")
        numero_da_conta = input("Digite o numero da conta:")
        usuario = input("Digite o usuário cadastrado no sistema:")
        Conta.criarContaCorrente(numero_da_conta,usuario)
        print("Conta cadastrado com sucesso")
    elif opcao ==6:
        for usu in usuario_lista:
            print(usu)
    elif opcao ==7:
        for cont in usuario_contas:
            print(f"Agencia:",cont['agencia'])
            print(f"Conta:",cont['num_conta'])
            print(f"Usuário:",cont['usuario'])
            print("\n")
    elif opcao == 8:
        print("Saindo... Volte sempre!")
        break
    else:
        print("Digite uma opção válida!")