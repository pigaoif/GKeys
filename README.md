# GKeys

Sistema de Empréstimo de Chaves IFNMG Campus Arinos - GUARDIAN KEYS

# Descrição

O Sistema de Empréstimo de Chaves é uma aplicação desenvolvida em Python com o framework Django, projetada para automatizar o processo de empréstimo e devolução de chaves no IFNMG Campus Arinos.
O banco de dados utiliza SQLite e é composto por cinco tabelas principais:
  - servidor;
  - chave;
  - emprestimo;
  - devolucao;
  - usuario.

A principal característica do sistema é a integração de tecnologias de leitura para proporcionar uma experiência eficiente e segura.
Utiliza-se um leitor de código de barras para identificação das chaves e a leitura biométrica para autenticação dos servidores.

# Requisitos do Sistema

  - Python 3.10.12
  - Django 3.12.12
  - SQLite
  - Leitor de código de barras
  - Leitor de leitura biométrica

# Instalação

Clone este repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


# Instale as dependências:

pip install -r requirements.txt

# Execute as migrações do banco de dados:

python manage.py migrate

# Inicie o servidor local:

python manage.py runserver

# Acesse o sistema

http://localhost:8000/

# Uso do Sistema

Faça login utilizando usuario: reprografia e senha:reprografia para autenticação.

Utilize o leitor de código de barras para identificar as chaves desejadas.
Utilize o leitor biometrico para identificar o servidor que pegará a chave emprestada.

# Estrutura do Banco de Dados

1. Tabela servidor
Descrição: Armazena informações sobre os servidores do campus.
Campos: id, nome, cargo, email, biometria

2. Tabela chave
Descrição: Contém dados das chaves disponíveis.
Campos: id, descricao, status, codbarra

3. Tabela empréstimo
Descrição: Registra os empréstimos de chaves.
Campos: id, chave_id, servidor_id, data_emprestimo, status

4. Tabela devolução
Descrição: Registra as devoluções de chaves.
Campos: id, id_chave, data_devolucao,

5. Tabela usuário
Descrição: Armazena informações sobre os usuários do sistema.
Campos: id, nome, user, password

# Integração de Dispositivos

1. Leitor de Código de Barras
Descrição: Utilizado para identificação das chaves.
Conexão: USB.

2. Leitor Biométrico
Descrição: Utilizado para identificar os servidores/funcionários.
Dispositivo: Sensor biométrico compatível.
Métodos de autenticação: Impressão digital.

# Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar pull requests.



