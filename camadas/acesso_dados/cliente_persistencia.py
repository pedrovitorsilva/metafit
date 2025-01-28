from .cliente import db, Cliente


class ClientePersistencia:
    @staticmethod
    def criar_cliente(cliente):
        db.session.add(cliente)
        db.session.commit()

    @staticmethod
    def listar_clientes():
        return Cliente.query.all()

    @staticmethod
    def buscar_cliente(cliente_id):
        return Cliente.query.get(cliente_id)

    @staticmethod
    def atualizar_cliente(cliente):
        db.session.commit()

    @staticmethod
    def deletar_cliente(cliente):
        db.session.delete(cliente)
        db.session.commit()
