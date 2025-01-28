from validacao.cliente_negocio import ClienteNegocio
from validacao.observer import LogObserver
from acesso_dados.cliente_persistencia import ClientePersistencia


def menu():
    cliente_negocio = ClienteNegocio()
    cliente_negocio.registrar_observer(LogObserver())

    while True:
        print("\n1. Criar cliente")
        print("2. Listar clientes")
        print("3. Atualizar cliente")
        print("4. Deletar cliente")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                nome = input("Nome: ")
                cpf = input("CPF: ")
                data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
                endereco = input("Endereço: ")
                telefone = input("Telefone: ")
                email = input("E-mail: ")
                sexo = input("Sexo: ")
                cliente_negocio.criar_cliente(
                    nome, cpf, data_nascimento, endereco, telefone, email, sexo)

            elif opcao == '2':
                clientes = ClientePersistencia.listar_clientes()
                for c in clientes:
                    print(f"ID: {c.id}, Nome: {c.nome}, CPF: {c.cpf}, Data de Nascimento: {c.data_nascimento}, Endereço: {
                          c.endereco}, Telefone: {c.telefone}, E-mail: {c.email}, Sexo: {c.sexo}")

            elif opcao == '3':
                cliente_id = int(input("ID do cliente: "))
                nome = input("Novo nome: ")
                cpf = input("Novo CPF: ")
                data_nascimento = input(
                    "Nova data de nascimento (DD/MM/AAAA): ")
                endereco = input("Novo endereço: ")
                telefone = input("Novo telefone: ")
                email = input("Novo e-mail: ")
                sexo = input("Novo sexo: ")
                cliente_negocio.atualizar_cliente(
                    cliente_id, nome, cpf, data_nascimento, endereco, telefone, email, sexo)

            elif opcao == '4':
                cliente_id = int(input("ID do cliente: "))
                cliente_negocio.deletar_cliente(cliente_id)

            elif opcao == '5':
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print(f"Erro: {e}")
