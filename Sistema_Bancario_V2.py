import datetime

saldo = 2000
extrato_saque = []
extrato_deposito = []
data_hora_saque = []
data_hora_deposito = []
usuario_lista = []
usuario_contas = []
saque_do_dia = 1500
limite_dia_t = 10
data_atual = datetime.datetime.today()

class Usuario:
    def criarUsuario(nome, data_nas, cpf, log, num, bairro, cidade, UF):
        for usu in usuario_lista:
            if usu["cpf"] == cpf:
                print("❌ CPF já cadastrado. Não é possível cadastrar o mesmo usuário duas vezes.")
                return None

        usuario = {
            "nome": nome,
            "data_nasc": data_nas,
            "cpf": cpf,
            "endereco": {
                "logradouro": log,
                "numero": num,
                "bairro": bairro,
                "cidade": cidade,
                "UF": UF
            }
        }
        usuario_lista.append(usuario)
        print("✅ Usuário cadastrado com sucesso.")
        return usuario

class Conta:
    def criarContaCorrente(num_conta, usuario, cpf):
        conta = {
            "agencia": "0001",
            "num_conta": num_conta,
            "usuario": usuario,
            "cpf": cpf
        }
        usuario_contas.append(conta)
        print("✅ Conta criada com sucesso.")
        return conta

def saque_dia(saque_atual, valor):
    return saque_atual - valor

def sacar(saldo, saque_do_dia, limite_dia_t, data_atual):
    valor = float(input("Digite o valor que deseja sacar: "))
    saque_restante = saque_dia(saque_do_dia, valor)

    if saldo > 0 and saque_restante >= 0 and limite_dia_t > 0:
        if valor > 500:
            print("❌ Você não pode sacar um valor acima de R$500,00")
        else:
            print("✅ Você sacou R$", valor)
            saldo -= valor
            limite_dia_t -= 1
            saque_do_dia = saque_restante
            data_formatada = data_atual.strftime("%d-%m-%Y %H:%M")
            data_hora_saque.append(data_formatada)
            extrato_saque.append(-valor)
    else:
        print("❌ Você está sem saldo ou excedeu o limite diário de transações")

    return saldo, saque_do_dia, limite_dia_t

def depositar(saldo, limite_dia_t, data_atual):
    valor_deposito = float(input("Digite o valor que deseja depositar: "))
    if valor_deposito > 0 and limite_dia_t > 0:
        print("✅ Você depositou o valor de", valor_deposito)
        extrato_deposito.append(valor_deposito)
        data_formatada = data_atual.strftime("%d-%m-%Y %H:%M")
        data_hora_deposito.append(data_formatada)
        saldo += valor_deposito
        limite_dia_t -= 1
    else:
        print("❌ Valor inválido ou limite de transações excedido")
    return saldo, limite_dia_t

def extrato():
    print("Esse é o extrato")

menu = """========== MENU ==========

1. Sacar
2. Depositar
3. Extrato
4. Cadastrar Usuário
5. Cadastrar Conta
6. Listar Usuários
7. Listar Contas
8. Sair

==========================\n"""

opcao = 0

while opcao != 8:
    try:
        opcao = int(input(menu))
    except ValueError:
        print("Digite uma opção válida!")
        continue

    if opcao == 1:
        saldo, saque_do_dia, limite_dia_t = sacar(saldo, saque_do_dia, limite_dia_t, data_atual)
        print("Extrato de saques:", extrato_saque)
        print("Saldo atual:", saldo)
        print("Limite restante de saque diário:", saque_do_dia)
        print("Data:", data_hora_saque)
        print("Limite de transações restantes:", limite_dia_t)

    elif opcao == 2:
        saldo, limite_dia_t = depositar(saldo, limite_dia_t, data_atual)
        print("Saldo atual:", saldo)
        print("Limite de transações restantes:", limite_dia_t)

    elif opcao == 3:
        extrato_final = extrato_saque + extrato_deposito
        data_final = data_hora_saque + data_hora_deposito
        print("========== EXTRATO BANCÁRIO ==========")
        for item, data in zip(extrato_final, data_final):
            print(f"{data}    R$ {item:.2f}")
        print("Saldo Final:", saldo)
        print("======================================")

    elif opcao == 4:
        print("Bem-vindo ao cadastro de Usuários")
        nome = input("Digite seu nome: ")
        data_nas = input("Digite sua data de nascimento: ")
        cpf = input("Digite seu CPF: ")
        logradouro = input("Digite seu endereço: ")
        numero = input("Digite o número: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite sua cidade: ")
        uf = input("Digite seu estado (UF): ")

        Usuario.criarUsuario(nome, data_nas, cpf, logradouro, numero, bairro, cidade, uf)

    elif opcao == 5:
        print("Bem-vindo ao cadastro de Contas")
        numero_da_conta = input("Digite o número da conta: ")
        atrela = input("Deseja atrelar essa conta a um usuário (S/N): ").strip().upper()

        if atrela == "S":
            cpf_atrela = input("Digite o CPF do usuário para atrelar a conta: ")
            usuario_encontrado = None

            for usu in usuario_lista:
                if cpf_atrela == usu["cpf"]:
                    usuario_encontrado = usu
                    break

            if usuario_encontrado:
                Conta.criarContaCorrente(numero_da_conta, usuario_encontrado["nome"], usuario_encontrado["cpf"])
                print("✅ Conta atrelada ao usuário com sucesso.")
            else:
                print("❌ CPF não encontrado. Conta não foi criada.")
        else:
            Conta.criarContaCorrente(numero_da_conta, None, None)
            print("✅ Conta cadastrada sem vínculo com usuário.")

    elif opcao == 6:
        print("====== Lista de Usuários ======")
        for usu in usuario_lista:
            print(f"Nome: {usu['nome']}")
            print(f"CPF: {usu['cpf']}")
            print(f"Data de nascimento: {usu['data_nasc']}")
            endereco = usu['endereco']
            print(f"Endereço: {endereco['logradouro']}, {endereco['numero']} - {endereco['bairro']}, {endereco['cidade']} - {endereco['UF']}")
            print("-------------------------------")

    elif opcao == 7:
        print("====== Lista de Contas ======")
        for cont in usuario_contas:
            print(f"Agência: {cont['agencia']}")
            print(f"Conta: {cont['num_conta']}")
            print(f"Usuário: {cont['usuario'] if cont['usuario'] else '--- Não vinculado ---'}")
            print(f"CPF: {cont['cpf'] if cont['cpf'] else '--- Não vinculado ---'}")
            print("-----------------------------")

    elif opcao == 8:
        print("Saindo... Volte sempre!")
        break

    else:
        print("Digite uma opção válida!")
