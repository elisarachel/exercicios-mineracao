import pandas as pd

df_usuarios = pd.DataFrame({
    'id_usuario':   [1, 2, 3, 4, 5],
    'nome_usuario': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'departamento': ['TI', 'Financeiro', 'RH', 'TI', 'Marketing']
})

df_equipamentos = pd.DataFrame({
    'id_equipamento':      [101, 102, 103, 104, 105, 106],
    'modelo':              ['Dell XPS', 'ThinkPad', 'MacBook', 'HP Pavilion', 'Dell Inspiron', 'Acer Aspire'],
    'sistema_operacional': ['Windows 11', 'Ubuntu', 'macOS', 'Windows 10', 'Ubuntu', 'Windows 11'],
    'id_usuario':          [1, 2, 3, 4, 5, 1]
})

df_chamados = pd.DataFrame({
    'id_ticket':       [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'id_usuario':      [1, 2, 3, 4, 5, 1, 2, 3],
    'id_equipamento':  [101, 102, 103, 104, 105, 106, 101, 102],
    'categoria':       ['Hardware', 'Software', 'Rede', 'Hardware', 'Software',
                        'Impressora', 'Hardware', 'Rede'],
    'horas_resolucao': [2.5, 1.0, 3.0, 4.0, 0.5, 1.5, 2.0, 2.5],
    'status':          ['Resolvido', 'Resolvido', 'Aberto', 'Resolvido', 'Resolvido',
                        'Aberto', 'Resolvido', 'Resolvido']
})
