# METAFIT - CRUD de Clientes com Flask

Versão de demonstração do projeto.

Aplicação de CRUD (Create, Read, Update, Delete) para gerenciar clientes, desenvolvida com o framework Flask. 

O código está estruturado em camadas para melhor organização e manutenção, seguindo boas práticas de design de software.

## Estrutura do Projeto

- **`apresentacao/`**: Camada responsável pela interação com o usuário, através de um menu no terminal.
- **`validacao/`**: Camada de lógica de negócios. Contém as regras de validação e implementação de padrões de projeto como Observer.
- **`acesso_dados/`**: Camada responsável pelo modelo de dados e persistência no banco de dados SQLite.
- **`main.py`**: Execução da aplicação.

## Camadas

### Apresentação
Gerencia a interação com o usuário, exibindo menus e coletando informações. Utiliza funções para acessar a camada de validação e realizar operações no banco de dados.

### Validação
Implementa a lógica de negócios e validação dos dados. Utiliza o padrão de projeto **Observer** para logar operações importantes.

### Acesso aos Dados
Gerencia a comunicação com o banco de dados SQLite usando SQLAlchemy, implementando operações CRUD para a tabela de clientes.

## Instalação

### Requisitos
- Python 3.9 ou superior

### Passos para Instalação

1. Clone o repositório ou baixe o código.
2. Navegue até o diretório do projeto.
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o projeto:

   4.1 Para uso convencional (precisa de 2 terminais funcionando)

   ```bash
   python frontend.py # No 1º terminal
   ```

   ```bash
   python backend.py # No 2º terminal
   ```

   4.2 Para testes automatizados(usar somente com um terminal)

   ```bash
   pytest tests.py 
   ```


## Uso

Ao executar o programa, será exibido um menu no terminal com as opções:

1. **Criar cliente**: Permite adicionar um novo cliente.
2. **Listar clientes**: Mostra todos os clientes cadastrados.
3. **Atualizar cliente**: Edita as informações de um cliente existente.
4. **Deletar cliente**: Remove um cliente pelo ID.
5. **Sair**: Encerra o programa.

## Dependências
As dependências do projeto estão listadas no arquivo `requirements.txt`.