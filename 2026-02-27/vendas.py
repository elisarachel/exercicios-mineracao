import pandas as pd

dados_clientes = {
    'id_cliente': [1, 2, 3, 4, 5],
    'nome_cliente': ['Ana', 'Bruno', 'Carlos', 'Maria', 'Paula'],
    'endereco_cliente': ['Rua A, 123', 'Rua B, 45', 'Rua C, 89', 'Rua D, 900', 'Rua E, 12']
}
df_clientes = pd.DataFrame(dados_clientes)

dados_produtos = {
    'id_produto': [101, 102, 103, 104],
    'nome_produto': ['Placa ESP32', 'Raspberry Pi 4', 'Orange Pi 4 LTS', 'Arduino'],
    'valor_produto': [45.90, 450.00, 380.00, 85.50],
    'quantidade_produto': [150, 50, 30, 200]
}
df_produtos = pd.DataFrame(dados_produtos)

dados_vendas = [
    [1, 1, 101], 
    [2, 1, 104], 
    [3, 2, 103], 
    [4, 2, 104], 
    [5, 3, 101], 
    [6, 4, 102], 
    [7, 5, 103], 
    [8, 5, 104]  
]

df_vendas = pd.DataFrame(dados_vendas, columns=['id_venda', 'id_cliente', 'id_produto'])

