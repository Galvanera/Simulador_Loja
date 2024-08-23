Gerador de Dados de Compras Fictícias
Este repositório contém um script Python que gera dados fictícios de compras, incluindo nomes de clientes, valores de compras, formas de pagamento, datas e horários. Os dados são salvos em um arquivo Excel para fácil manipulação e análise.

Funcionalidades
Geração de Nomes Fictícios: Utiliza a biblioteca Faker para gerar nomes em português do Brasil.
Datas Aleatórias: Gera datas aleatórias dentro de um intervalo especificado, com menor probabilidade de serem segundas ou terças-feiras.
Valores de Compras: Gera valores de compras aleatórios entre 10 e 1000.
Formas de Pagamento: Inclui várias formas de pagamento como cartão de crédito, débito, vale alimentação, vale refeição e dinheiro.
Vendedores: Atribui um vendedor aleatório a cada compra.
Exportação para Excel: Salva os dados gerados em um arquivo Excel (dados_compras_vendedores.xlsx).
Como Usar
Instale as bibliotecas necessárias:
pip install pandas faker openpyxl

Clone este repositório:
git clone https://github.com/seu-usuario/gerador-dados-compras.git
cd gerador-dados-compras

Execute o script:
python gerar_dados_compras.py

Veja os dados gerados:
O script salvará os dados gerados em um arquivo Excel chamado dados_compras_vendedores.xlsx.
