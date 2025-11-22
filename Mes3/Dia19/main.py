"""
=== Desafio do Dia 79 — Estatísticas Avançadas com Pandas (sem CSV) ===

Descrição:
Este desafio envolve criar uma pequena base simulada de alunos em cursos
online, sem utilização de arquivos externos. O objetivo é praticar
agrupamentos, estatísticas agregadas,filtros condicionais e ordenações, 
produzindo um relatório útil.

Tarefas:
 - Criar manualmente um DataFrame simulando alunos e cursos
 - Calcular médias por categoria e por curso
 - Identificar categoria com maior dedicação (horas estudadas)
 - Encontrar curso com melhor avaliação média
 - Filtrar alunos com baixo progresso (< 30%)
 - Gerar tabelas ordenadas para análise
"""




import pandas as pd





def criar_base():
    data = {
        "user_id":   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "course": [
            "Python Básico", "SQL Essencial", "UI Design", "Python Básico",
            "Data Science", "Python Básico", "SQL Essencial", "UI Design",
            "Data Science", "SQL Essencial"
        ],
        "category": [
            "Programação", "Dados", "Design", "Programação",
            "Dados", "Programação", "Dados", "Design",
            "Dados", "Dados"
        ],
        "hours_studied": [10, 6, 4, 15, 12, 18, 7, 5, 20, 8],
        "progress":      [40, 55, 30, 80, 60, 95, 25, 20, 85, 50],
        "rating":        [5, 4, 3, 5, 4, 5, 2, 3, 5, 4]
    }
    df = pd.DataFrame(data)
    return df





def analisar(df):
    print("\n=-= 1) Média de progresso por categoria =-=")
    print(df.groupby("category")["progress"].mean().round(1))

    print("\n=-= 2) Média de horas estudadas por curso =-=")
    print(df.groupby("course")["hours_studied"].mean().round(1))

    print("\n=-= 3) Categoria com mais dedicação (horas estudadas) =-=")
    dedicacao = df.groupby("category")["hours_studied"].mean().sort_values(ascending=False)
    print(dedicacao)

    print("\n=-= 4) Curso com melhor avaliação média =-=")
    avaliacao = df.groupby("course")["rating"].mean().sort_values(ascending=False)
    print(avaliacao.head(1))

    print("\n=-= 5) Alunos com progresso abaixo de 30% (grupo de risco) =-=")
    risco = df[df["progress"] < 30]
    print(risco)

    print("\n=-= 6) Tabela geral de cursos ordenada por progresso médio =-=")
    progresso_ordenado = df.groupby("course")["progress"].mean().sort_values(ascending=False)
    print(progresso_ordenado)






def main():
    df = criar_base()
    print("\n=-=- Base Criada =-=-")
    print(df)
    analisar(df)





if __name__ == "__main__":
    main()
