import pytest
import json
from backend import app

# Simula ambiente da aplicação funcionando
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_listar_clientes(client):
    response = client.get('http://127.0.0.1:5000/clientes')
    assert response.status_code == 200

def test_adicionar_cliente(client):
    dados = {
        "nome": "Teste",
        "cpf": "12345678901",
        "data_nascimento": "01/01/1990",
        "endereco": "Rua Teste",
        "telefone": "123456789",
        "email": "teste@teste.com",
        "sexo": "M"
    }
    response = client.post('http://127.0.0.1:5000/clientes',
                           data=json.dumps(dados), content_type='application/json')
    assert response.status_code == 201

def test_adicionar_cliente_cpf_invalido(client):
    dados = {
        "nome": "Teste",
        "cpf": "1234567890",  # CPF inválido
        "data_nascimento": "01/01/1990",
        "endereco": "Rua Teste",
        "telefone": "123456789",
        "email": "teste@teste.com",
        "sexo": "M"
    }
    response = client.post('http://127.0.0.1:5000/clientes',
                           data=json.dumps(dados), content_type='application/json')
    assert response.status_code == 400
    assert "CPF deve ter 11 dígitos numéricos." in response.json['erro']

def test_adicionar_cliente_nome_vazio(client):
    dados = {
        "nome": "",  # Nome vazio
        "cpf": "12312312312",
        "data_nascimento": "01/01/1990",
        "endereco": "Rua Teste",
        "telefone": "123456789",
        "email": "teste@teste.com",
        "sexo": "M"
    }
    response = client.post('http://127.0.0.1:5000/clientes',
                           data=json.dumps(dados), content_type='application/json')
    assert response.status_code == 400
    assert "Nome é obrigatório." in response.json['erro']

def test_adicionar_cliente_data_nascimento_invalida(client):
    dados = {
        "nome": "Teste",
        "cpf": "444.444.444-44",
        "data_nascimento": "01/011999",  # Data de nascimento inválida
        "endereco": "Rua Teste",
        "telefone": "123456789",
        "email": "teste@teste.com",
        "sexo": "M"
    }
    response = client.post('http://127.0.0.1:5000/clientes',
                           data=json.dumps(dados), content_type='application/json')
    assert response.status_code == 400
    assert "Data de nascimento deve estar no formato DD/MM/AAAA." in response.json['erro']

def test_adicionar_cliente_telefone_invalido(client):
    dados = {
        "nome": "Teste",
        "cpf": "87698756444",
        "data_nascimento": "01/01/1990",
        "endereco": "Rua Teste",
        "telefone": "1234567",  # Telefone inválido
        "email": "teste@teste.com",
        "sexo": "M"
    }
    response = client.post('http://127.0.0.1:5000/clientes',
                           data=json.dumps(dados), content_type='application/json')
    assert response.status_code == 400
    assert "Telefone deve ter até 11 dígitos (com DDD)." in response.json['erro']

def test_excluir_cliente(client):
    # Excluir o cliente
    response = client.delete('http://127.0.0.1:5000/clientes/1')
    assert response.status_code == 200

def test_excluir_cliente_inexistente(client):
    response = client.delete('http://127.0.0.1:5000/clientes/1')
    assert response.status_code == 404
    assert "Cliente não encontrado." in response.json['erro']