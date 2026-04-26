import pandas as pd

df_motoristas = pd.DataFrame({
    'id_motorista':   [1, 2, 3, 4],
    'nome_motorista': ['Carlos', 'Ana', 'Roberto', 'Mariana'],
    'cnh':            ['AB', 'B', 'A', 'AB']
})

df_veiculos = pd.DataFrame({
    'id_veiculo':    [10, 11, 12, 13, 14],
    'placa':         ['ABC1234', 'DEF5678', 'GHI9012', 'JKL3456', 'MNO7890'],
    'tipo_veiculo':  ['Van', 'Caminhão', 'Van', 'Moto', 'Caminhão'],
    'capacidade_kg': [800, 5000, 800, 30, 5000]
})

df_entregas = pd.DataFrame({
    'id_entrega':   list(range(1, 13)),
    'id_motorista': [1, 2, 1, 3, 4, 2, 1, 4, 3, 2, 1, 4],
    'id_veiculo':   [10, 11, 12, 13, 14, 10, 11, 12, 13, 14, 10, 11],
    'distancia_km': [120, 350, 85, 15, 500, 280, 150, 95, 20, 410, 75, 320],
    'status':       ['Entregue', 'Entregue', 'Entregue', 'Em trânsito', 'Entregue',
                     'Entregue', 'Entregue', 'Em trânsito', 'Entregue', 'Entregue',
                     'Entregue', 'Entregue']
})
