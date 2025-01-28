from camadas.acesso_dados.cliente_persistencia import ClientePersistencia
from camadas.acesso_dados.cliente import Cliente
from typing import List
from .observer import Observer, LogObserver


class ClienteNegocio:
    def __init__(self):
        self.observers: List[Observer] = []

    def registrar_observer(self, observer: Observer):
        self.observers.append(observer)

    def notificar_observers(self, mensagem: str):
        for observer in self.observers:
            observer.atualizar(mensagem)

    def validar_cliente(self, nome, cpf, data_nascimento, telefone, email, sexo):
        # Limpar CPF e telefone antes da validação
        if cpf:
            cpf = str(cpf).replace(".", "").replace("-", "").replace(" ", "")
            if len(cpf) != 11 or not cpf.isnumeric():
                raise ValueError("CPF deve ter 11 dígitos numéricos.")
        else:
            raise ValueError("CPF deve ter 11 dígitos numéricos.")

        if not nome:
            raise ValueError("Nome é obrigatório.")

        if not data_nascimento:
            raise ValueError("Data de nascimento é obrigatória.")
        try:
            dia, mes, ano = map(int, data_nascimento.split("/"))
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1900):
                raise ValueError(
                    "Data de nascimento deve estar no formato DD/MM/AAAA.")
        except ValueError:
            raise ValueError(
                "Data de nascimento deve estar no formato DD/MM/AAAA.")

        if data_nascimento.count("/") != 2:
            raise ValueError(
                "Data de nascimento deve estar no formato DD/MM/AAAA.")

        if telefone:
            telefone = str(telefone).replace("(", "").replace(
                ")", "").replace("-", "").replace(" ", "")
            if len(telefone) > 11 or len(telefone) < 8:
                raise ValueError("Telefone deve ter até 11 dígitos (com DDD).")
        else:
            raise ValueError("Telefone é obrigatório.")

        if "@" not in email:
            raise ValueError("Email é inválido.")

        if sexo not in ["M", "F", "Outro"]:
            raise ValueError("Sexo deve ser 'M', 'F' ou 'Outro'.")

    def criar_cliente(self, nome, cpf, data_nascimento, endereco, telefone, email, sexo):

        # Limpar CPF e telefone antes de validar
        cpf = str(cpf).replace(".", "").replace("-", "").replace(" ", "")
        telefone = str(telefone).replace("(", "").replace(")",
                                                          "").replace("-", "").replace(" ", "")

        cliente_existente = Cliente.query.filter_by(cpf=cpf).first()
        if cliente_existente:
            raise ValueError("CPF já está cadastrado.")

        self.validar_cliente(nome, cpf, data_nascimento, telefone, email, sexo)

        cliente = Cliente(nome=nome, cpf=cpf, data_nascimento=data_nascimento,
                          endereco=endereco, telefone=telefone, email=email, sexo=sexo)
        ClientePersistencia.criar_cliente(cliente)
        self.notificar_observers(f"Cliente {nome} criado com sucesso.")

    def atualizar_cliente(self, cliente_id, nome, cpf, data_nascimento, endereco, telefone, email, sexo):
        cliente = ClientePersistencia.buscar_cliente(cliente_id)
        if cliente:
            # Limpar CPF e telefone antes de validar
            cpf = str(cpf).replace(".", "").replace("-", "").replace(" ", "")
            telefone = str(telefone).replace("(", "").replace(
                ")", "").replace("-", "").replace(" ", "")

            self.validar_cliente(
                nome, cpf, data_nascimento, telefone, email, sexo)

            cliente_existente = Cliente.query.filter_by(cpf=cpf).first()
            if cliente_existente:
                raise ValueError("CPF já está cadastrado.")

            cliente.nome = nome
            cliente.cpf = cpf
            cliente.data_nascimento = data_nascimento
            cliente.endereco = endereco
            cliente.telefone = telefone
            cliente.email = email
            cliente.sexo = sexo
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
