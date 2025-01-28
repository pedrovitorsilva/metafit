import requests

def menu():
    while True:
        print("\nMenu de Clientes")
        print("1. Listar clientes")
        print("2. Adicionar cliente")
        print("3. Editar cliente")
        print("4. Excluir cliente")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                resposta = requests.get('http://127.0.0.1:5000/clientes')
                if resposta.status_code == 200:
                    clientes = resposta.json()

                    if clientes == []:
                        print("Nenhum cliente encontrado.")
                    else:
                        print("\nClientes:")
                        for cliente in clientes:
                            print(cliente)
                else:
                    print("Erro ao listar clientes.")

            elif opcao == '2':
                nome = input("Digite o nome do cliente: ")
                cpf = input("Digite o CPF do cliente: ")
                data_nascimento = input(
                    "Digite a data de nascimento (DD/MM/YYYY): ")
                endereco = input("Digite o endereço do cliente: ")
                telefone = input("Digite o telefone do cliente: ")
                email = input("Digite o email do cliente: ")
                sexo = input("Digite o sexo do cliente: ")
                dados = {
                    "nome": nome,
                    "cpf": cpf,
                    "data_nascimento": data_nascimento,
                    "endereco": endereco,
                    "telefone": telefone,
                    "email": email,
                    "sexo": sexo
                }
                resposta = requests.post(
                    'http://127.0.0.1:5000/clientes', json=dados)
                if resposta.status_code == 201:
                    print("Cliente adicionado com sucesso!")
                else:
                    print("Erro ao adicionar cliente.", resposta.json())

            elif opcao == '3':
                id_cliente = input("Digite o ID do cliente a ser editado: ")
                nome = input("Digite o novo nome do cliente: ")
                cpf = input("Digite o novo CPF do cliente: ")
                data_nascimento = input(
                    "Digite a nova data de nascimento (YYYY-MM-DD): ")
                endereco = input("Digite o novo endereço do cliente: ")
                telefone = input("Digite o novo telefone do cliente: ")
                email = input("Digite o novo email do cliente: ")
                sexo = input("Digite o novo sexo do cliente: ")
                dados = {
                    "nome": nome,
                    "cpf": cpf,
                    "data_nascimento": data_nascimento,
                    "endereco": endereco,
                    "telefone": telefone,
                    "email": email,
                    "sexo": sexo
                }
                resposta = requests.put(
                    f'http://127.0.0.1:5000/clientes/{id_cliente}', json=dados)
                if resposta.status_code == 200:
                    print("Cliente editado com sucesso!")
                else:
                    print("Erro ao editar cliente.", resposta.json())

            elif opcao == '4':
                id_cliente = input("Digite o ID do cliente a ser excluído: ")
                resposta = requests.delete(
                    f'http://127.0.0.1:5000/clientes/{id_cliente}')
                if resposta.status_code == 200:
                    print("Cliente excluído com sucesso!")
                else:
                    print("Erro ao excluir cliente.", resposta.json())

            elif opcao == '5':
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except requests.ConnectionError:
            print("Erro de conexão: o servidor não está acessível. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    menu()
