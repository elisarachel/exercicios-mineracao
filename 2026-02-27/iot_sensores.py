import pandas as pd
import numpy as np
from datetime import datetime, timedelta

df_ambientes = pd.DataFrame({
    'id_ambiente': [1, 2, 3],
    'nome_setor': ['Linha de Produção', 'Armazém Frio', 'Escritório']
})

df_dispositivos = pd.DataFrame({
    'id_dispositivo': [10, 11, 12, 13, 14],
    'modelo': ['RPI', 'Orange Pi', 'ESP32', 'RPI', 'ESP32'],
    'id_ambiente': [1, 1, 2, 2, 3]
})

np.random.seed(42)
n = 20
base = datetime(2026, 4, 1, 8, 0, 0)

df_telemetria = pd.DataFrame({
    'id_leitura':    range(1, n + 1),
    'id_dispositivo': np.random.choice([10, 11, 12, 13, 14], n),
    'data_hora':     [base + timedelta(minutes=i * 30) for i in range(n)],
    'temperatura_c': np.round(np.random.uniform(15.0, 45.0, n), 1),
    'umidade':       np.round(np.random.uniform(40.0, 90.0, n), 1)
})
