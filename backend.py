from flask import Flask, jsonify, request
from camadas.validacao.cliente_negocio import ClienteNegocio
from camadas.acesso_dados.cliente import db

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Inicializa ClienteNegocio
cliente_negocio = ClienteNegocio()

# Garantir que as tabelas sejam criadas antes de iniciar o servidor
with app.app_context():
    db.create_all()


@app.route('/clientes', methods=['GET'])
def listar_clientes():
    try:
        clientes = cliente_negocio.listar_clientes()
        return jsonify([{
            "id": cliente.id,
            "nome": cliente.nome,
            "cpf": cliente.cpf,
            "data_nascimento": cliente.data_nascimento,
            "endereco": cliente.endereco,
            "telefone": cliente.telefone,
            "email": cliente.email,
            "sexo": cliente.sexo
        } for cliente in clientes]), 200
    except Exception as e:
        print(e)
        return jsonify({"erro": str(e)}), 500


@app.route('/clientes', methods=['POST'])
def adicionar_cliente():
    dados = request.json
    try:
        cliente_negocio.criar_cliente(
            nome=dados['nome'],
            cpf=dados['cpf'],
            data_nascimento=dados['data_nascimento'],
            endereco=dados['endereco'],
            telefone=dados['telefone'],
            email=dados['email'],
            sexo=dados['sexo']
        )
        return jsonify({'status': 'cliente adicionado'}), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@app.route('/clientes/<int:id>', methods=['PUT'])
def editar_cliente(id):
    dados = request.json
    try:
        cliente_negocio.atualizar_cliente(
            cliente_id=id,
            nome=dados['nome'],
            cpf=dados['cpf'],
            data_nascimento=dados['data_nascimento'],
            endereco=dados['endereco'],
            telefone=dados['telefone'],
            email=dados['email'],
            sexo=dados['sexo']
        )
        return jsonify({'status': f'cliente {id} editado'}), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    try:
        cliente_negocio.deletar_cliente(cliente_id=id)
        return jsonify({'status': f'cliente {id} excluído'}), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
