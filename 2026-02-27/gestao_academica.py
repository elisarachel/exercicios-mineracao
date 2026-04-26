import pandas as pd

df_cursos = pd.DataFrame({
    'id_curso': [1, 2, 3],
    'nome_curso': ['DSM', 'ADS', 'GPI'],
    'duracao_semestres': [6, 6, 4]
})

df_disciplinas = pd.DataFrame({
    'id_disciplina': [101, 102, 103, 104, 105],
    'nome_disciplina': ['Mineração de Dados', 'Banco de Dados', 'Programação Web', 'Redes', 'Eng. de Software'],
    'id_curso': [1, 1, 2, 2, 3]
})

df_professores = pd.DataFrame({
    'id_professor': [201, 202, 203],
    'nome_professor': ['Prof. Silva', 'Prof. Santos', 'Prof. Oliveira'],
    'id_disciplina': [101, 102, 103]
})

df_alunos = pd.DataFrame({
    'id_aluno': [301, 302, 303, 304, 305, 306, 307, 308, 309, 310],
    'nome_aluno': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo',
                   'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Julia'],
    'id_curso': [1, 1, 2, 2, 3, 1, 2, 3, 1, 2]
})

df_matriculas = pd.DataFrame({
    'id_matricula': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'id_aluno':     [301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 301, 302],
    'id_disciplina':[101, 101, 103, 104, 105, 102, 103, 105, 101, 103, 102, 103],
    'id_professor': [201, 201, 203, None, None, 202, 203, None, 201, 203, 202, 203],
    'nota':         [8.5, 7.0, 9.0, 6.5, 8.0, 7.5, 8.5, 7.0, 9.5, 8.0, 7.5, 6.0]
})
