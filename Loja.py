import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker

# Gerar 832 nomes fictícios (permitindo repetições)
fake = Faker("pt_BR")
nomes_clientes = [fake.name() for _ in range(832)]

# Lista de vendedores
vendedores = ["Bruna Almeida", "Jaqueline Silva", "Daniela Alves", "Bruna Rodrigues", "Helena Maria", "Rosa Silveira", "Maria Luiza", "Edna Teixeira"]

# Função para gerar uma data aleatória com menor probabilidade de ser segunda ou terça
def generate_random_date():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 7, 31)
    while True:
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        weekday = random_date.weekday()
        month = random_date.month
        if month == 1 and random.random() < 0.40:  # 50% de chance de evitar janeiro
            continue
        if month == 2 and random.random() < 0.52:
            continue
        if month == 3 and random.random() < 0.21:
            continue
        if month == 4 and random.random() < 0.35:
            continue
        if month == 5 and random.random() < 0.02:
            continue
        if month == 6 and random.random() < 0.25:
            continue
        if month == 7 and random.random() < 0.12:
            continue
        if weekday != 6:  # 6 representa domingo
            if weekday == 5:  # 5 representa sábado
                if random.random() < 0.99:  # 50% de chance de ser sábado
                    return random_date.strftime("%d/%m/%Y")
            elif weekday in [0, 1]:  # 0 representa segunda e 1 representa terça
                if random.random() < 0.27:  # 20% de chance de ser segunda ou terça
                    return random_date.strftime("%d/%m/%Y")
            elif weekday == 2:  
                if random.random() < 0.55:  
                    return random_date.strftime("%d/%m/%Y")
            elif weekday == 3:  
                if random.random() < 0.65:  
                    return random_date.strftime("%d/%m/%Y")
            elif weekday == 4:  
                if random.random() < 0.70:  
                    return random_date.strftime("%d/%m/%Y")
            else:
                return random_date.strftime("%d/%m/%Y")

# Gerar dados de vendas
vendas = []
for i in range(1, 3801):
    id_compra = i
    nome_cliente = random.choice(nomes_clientes)
    vendedor = random.choices(vendedores, weights=[0.24, 0.11, 0.03, 0.18, 0.04, 0.10, 0.10, 0.19])[0]
    categoria = random.choices(["Calçados", "Roupas", "Acessórios", "Roupas infantis"], weights=[0.20, 0.60, 0.08, 0.12])[0]
    total_vendido = round(random.uniform(9.9, 300), 2)
    data_venda = generate_random_date()
    forma_pagamento = random.choices(["Cartão de crédito", "Cartão Débito", "Dinheiro", "PIX"], weights=[0.29, 0.30, 0.28, 0.13])[0]
    vendas.append((id_compra, nome_cliente, vendedor, categoria, total_vendido, data_venda, forma_pagamento))

# Criar um DataFrame com os dados gerados
df = pd.DataFrame(vendas, columns=["ID Compra", "Cliente", "Vendedor", "Categoria", "Total Vendido", "Data da Venda", "Forma de Pagamento"])

# Salvar em um arquivo .xlsx
nome_arquivo = "roupas.xlsx"
df.to_excel(nome_arquivo, index=False, engine="openpyxl")

print(f"Os dados foram salvos no arquivo '{nome_arquivo}' com as vendas restritas aos períodos de trabalho das vendedoras.")
