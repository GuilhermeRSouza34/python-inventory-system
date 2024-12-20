# Sistema de Gerenciamento de Estoque em Python

Este projeto é um sistema de gerenciamento de estoque para produtos como mouses, teclados e monitores. Ele permite a adição de novos produtos, o registro de solicitações e a consulta do estoque atual, utilizando um arquivo Excel para armazenar os dados.

## Estrutura do Projeto

```
python-inventory-system
├── src
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── inventory_manager.py   # Gerencia operações de estoque
│   ├── request_handler.py     # Lida com solicitações de produtos
│   └── excel_utils.py        # Funções utilitárias para manipulação de Excel
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação do projeto
└── setup.py                   # Configuração do projeto
```

## Instalação

1. Clone o repositório ou faça o download do projeto.
2. Navegue até o diretório do projeto.
3. Instale as dependências com o comando:

   ```
   pip install -r requirements.txt
   ```

## Uso

1. Execute o arquivo `main.py` para iniciar o sistema:

   ```
   python src/main.py
   ```

2. Siga as instruções exibidas no menu para gerenciar o estoque e registrar solicitações.

## Instruções para Gerar um Executável com PyInstaller

1. Instale o PyInstaller com o comando:

   ```
   pip install pyinstaller
   ```

2. Navegue até o diretório do projeto.

3. Execute o comando para gerar um executável único:

   ```
   pyinstaller --onefile src/main.py
   ```

4. O executável será criado na pasta `dist`. Você pode mover este arquivo para a tela de início ou para a pasta de rede da empresa.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.