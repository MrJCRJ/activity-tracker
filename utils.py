# utils.py

from datetime import datetime
from collections import defaultdict

def calcular_horas_por_data_e_tarefa(dados):
    """
    Calcula as horas totais por data e agrupa tarefas por descrição.

    Args:
        dados (list): Lista de dicionários contendo as atividades.

    Returns:
        dict: Dicionário estruturado como {data: {descricao: horas}}.
    """
    estatisticas = defaultdict(lambda: defaultdict(float))

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

def validate_datetime(valor, tipo):
    """
    Valida o formato de data ou hora.

    Args:
        valor (str): Valor a ser validado.
        tipo (str): Tipo de validação ('data' ou 'hora').

    Returns:
        bool: True se for válido, False caso contrário.
    """
    try:
        if tipo == 'data':
            datetime.strptime(valor, "%Y-%m-%d")  # Valida a data no formato AAAA-MM-DD
            return True
        elif tipo == 'hora':
            if len(valor) == 4 and valor.isdigit():
                hora = int(valor[:2])
                minuto = int(valor[2:])
                return 0 <= hora <= 23 and 0 <= minuto <= 59
    except ValueError:
        pass
    return False

def filtrar_por_data(dados, data):
    """
    Filtra as atividades por uma data específica.

    Args:
        dados (list): Lista de dicionários contendo as atividades.
        data (str): Data no formato AAAA-MM-DD.

    Returns:
        list: Lista de atividades filtradas pela data.
    """
    return [atividade for atividade in dados if atividade['data'] == data]
