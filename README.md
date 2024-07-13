# Py Orders Database Project

`Autor:` [Kaíque Freire dos Santos]<br>
`Data Conclusão:` [13/07/2024]

O Py Orders Database Project é uma aplicação desenvolvida em Python para gerenciar pedidos de uma empresa. A aplicação permite adicionar, visualizar e manipular dados de pedidos em um banco de dados SQLite, utilizando o módulo sqlite3 do Python.

Este projeto foi desenvolvido com o objetivo de demonstrar o uso de operações CRUD (Create, Read, Update, Delete) em um banco de dados SQLite, bem como a separação de responsabilidades através de diferentes camadas: modelos, visualizações e controle.

## Instalação

Para instalar e rodar este projeto, siga os passos abaixo:

1. Clone o repositório:
    ```sh
    git clone https://github.com/kaiquefreire05/py-orders-database-project.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd py-orders-database-project
    ```

3. (Opcional) Crie um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Para Windows use `venv\Scripts\activate`
    ```

4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

Para usar a aplicação, execute o script principal:
```sh
python src/main.py
```
<br>
Você verá as opções disponíveis no menu para gerenciar os pedidos.<br><br>

1 - Menu de Opções<br>
2 - Adicionar novo pedido<br>
3 - Visualizar todos os pedidos<br>
4 - Atualizar um pedido<br>
5 - Remover um pedido<br>
6 - Sair<br>

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

py-orders-database-project/<br>
│<br>
├── database/<br>
│   └── orders.db          # Banco de dados SQLite<br>
│<br>
├── src/<br>
│   ├── controllers/<br>
│   │   └── item_controller.py  # Controladores para manipulação de itens<br>
│   │   └── pedido_controller.py  # Controladores para manipulação de pedidos<br>
│   │<br>
│   ├── models/<br>
│   │   └── pedido.py<br>
│   │   └── item_pedido.py<br>
│   │   └── pedido.py<br>
│   │<br>
│   ├── views/<br>
│   │   └── item    # Todos os scripts de views relacionado a itens do projeto<br>
│   │   └── pedido   # Todos os scripts de views relacionado a pedidos do projeto<br>
│   │   └── main_view.py   # View inicial do projeto<br>
│   │<br>
│   └── main.py             # Script principal da aplicação<br>
│<br>
│<br>
├── README.md               # Documentação do projeto<br>
├── requirements.txt        # Dependências do projeto<br>
└── .gitignore              # Arquivos e diretórios ignorados pelo Git<br>

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão de melhoria, por favor, abra uma issue ou envie um pull request.

1 - Fork o repositório
2 - Crie uma branch para sua feature (git checkout -b feature/nova-feature)
3 - Commit suas mudanças (git commit -m 'Adiciona nova feature')
4 - Faça o push para a branch (git push origin feature/nova-feature)
5 - Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
