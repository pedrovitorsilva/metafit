from typing import List
from camadas.acesso_dados.cliente import Cliente
from camadas.acesso_dados.cliente_persistencia import ClientePersistencia
from camadas.validacao.observer import Observer
from camadas.validacao.validacao import Validacao, ValidatorFactory


class ClienteNegocio(Validacao):
    def __init__(self):
        self.observers: List[Observer] = []

    def registrar_observer(self, observer: Observer):
        self.observers.append(observer)

    def notificar_observers(self, mensagem: str):
        for observer in self.observers:
            observer.atualizar(mensagem)


    def validar_cliente(self, cliente: Cliente):
        for campo, valor in cliente.__dict__.items():
            # Ignorar campos internos do SQLAlchemy (começam com "_")
            if campo.startswith("_"):
                continue
            validator = ValidatorFactory.get_validator(campo)
            validator.validar(campo, valor)

    def criar_cliente(self, nome, cpf, data_nascimento, endereco, telefone, email, sexo):
        # Limpar CPF e telefone antes de validar
        cpf = str(cpf).replace(".", "").replace("-", "").replace(" ", "")
        telefone = str(telefone).replace("(", "").replace(")",
                                                          "").replace("-", "").replace(" ", "")

        cliente_existente = Cliente.query.filter_by(cpf=cpf).first()
        if cliente_existente:
            raise ValueError("CPF já está cadastrado.")

        cliente = Cliente(nome=nome, cpf=cpf, data_nascimento=data_nascimento,
                          endereco=endereco, telefone=telefone, email=email, sexo=sexo)
        self.validar_cliente(cliente)
        ClientePersistencia.criar_cliente(cliente)
        self.notificar_observers(f"Cliente {nome} criado com sucesso.")

    def atualizar_cliente(self, cliente_id, nome, cpf, data_nascimento, endereco, telefone, email, sexo):
        cliente = ClientePersistencia.buscar_cliente(cliente_id)
        if cliente:
            # Limpar CPF e telefone antes de validar
            cpf = str(cpf).replace(".", "").replace("-", "").replace(" ", "")
            telefone = str(telefone).replace("(", "").replace(
                ")", "").replace("-", "").replace(" ", "")

            cliente_existente = Cliente.query.filter_by(cpf=cpf).first()
            if cliente_existente and cliente_existente.id != cliente_id:
                raise ValueError("CPF já está cadastrado.")

            cliente.nome = nome
            cliente.cpf = cpf
            cliente.data_nascimento = data_nascimento
            cliente.endereco = endereco
            cliente.telefone = telefone
            cliente.email = email
            cliente.sexo = sexo

            self.validar_cliente(cliente)
            ClientePersistencia.atualizar_cliente(cliente)
            self.notificar_observers(f"Cliente {nome} atualizado com sucesso.")
        else:
            raise ValueError("Cliente não encontrado.")

    def listar_clientes(self):
        return ClientePersistencia.listar_clientes()

    def deletar_cliente(self, cliente_id):
        cliente = ClientePersistencia.buscar_cliente(cliente_id)
        if cliente:
            ClientePersistencia.deletar_cliente(cliente)
            self.notificar_observers(
                f"Cliente {cliente.nome} removido com sucesso.")
        else:
            raise ValueError("Cliente não encontrado.")
