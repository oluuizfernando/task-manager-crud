# Lista de Tarefas com Python, Django e Bootstrap

Este é um projeto de lista de tarefas desenvolvido utilizando Python, Django e Bootstrap. O objetivo é permitir que usuários gerenciem suas tarefas de forma eficiente, oferecendo funcionalidades como adicionar, editar, concluir e deletar tarefas.

## Funcionalidades

- Adicionar uma nova tarefa especificando o nome e a data de entrega.
- Editar uma tarefa existente para modificar seu nome ou data de entrega.
- Marcar uma tarefa como concluída.
- Excluir tarefas que não são mais necessárias.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para a lógica do sistema.
- **Django**: Framework web utilizado para desenvolver a aplicação.
- **Bootstrap**: Framework de CSS utilizado para o design responsivo e interface do usuário.

## Como Usar

1. **Instalação**
   - Clone o repositório:

     ```
     git clone https://github.com/oluuizfernando/task-manager-crud.git
     
     ```

   - Instale as dependências:

     ```
     pip install -r requirements.txt
     ```

2. **Configuração**
   - Configure as variáveis de ambiente necessárias, como chaves secretas e configurações de banco de dados, conforme definido no arquivo `.env.example`.

3. **Execução**
   - Execute as migrações do banco de dados:

     ```
     python manage.py migrate
     ```

   - Inicie o servidor de desenvolvimento:

     ```
     python manage.py runserver
     ```

4. **Acesso**
   - Acesse a aplicação no navegador utilizando o endereço local fornecido pelo Django.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues relatando problemas ou sugestões.
