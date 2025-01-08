#  Contém funções auxiliares (como validação de entradas, por exemplo, caso seja necessário no futuro).
# Funções de validação.
# Formatação de saída.
# Cálculos, como estatísticas das atividades.


from datetime import datetime

# Função para calcular o total de horas por data
def calcular_horas_por_data(dados):
    horas_por_data = {}

    for atividade in dados:
        data = atividade["data"]
        hora_inicio = atividade["hora_inicio"]
        hora_fim = atividade["hora_fim"]

        # Converte as horas para objetos datetime
        inicio = datetime.strptime(hora_inicio, "%H:%M")
        fim = datetime.strptime(hora_fim, "%H:%M")

        # Calcula a diferença em horas
        duracao = (fim - inicio).seconds / 3600

        # Soma a duração ao total da data
        if data in horas_por_data:
            horas_por_data[data] += duracao
        else:
            horas_por_data[data] = duracao

    return horas_por_data
