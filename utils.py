#  Contém funções auxiliares (como validação de entradas, por exemplo, caso seja necessário no futuro).
# Funções de validação.
# Formatação de saída.
# Cálculos, como estatísticas das atividades.


from datetime import datetime
from collections import defaultdict

# Função para calcular horas totais por data e agrupar tarefas por descrição
def calcular_horas_por_data_e_tarefa(dados):
    estatisticas = defaultdict(lambda: defaultdict(float))  # Estrutura: {data: {descricao: horas}}

    for atividade in dados:
        data = atividade["data"]
        descricao = atividade["descricao"]
        hora_inicio = atividade["hora_inicio"]
        hora_fim = atividade["hora_fim"]

        # Converte as horas para objetos datetime
        inicio = datetime.strptime(hora_inicio, "%H:%M")
        fim = datetime.strptime(hora_fim, "%H:%M")

        # Calcula a duração em horas
        duracao = (fim - inicio).seconds / 3600

        # Adiciona a duração à descrição dentro da data
        estatisticas[data][descricao] += duracao

    return estatisticas
