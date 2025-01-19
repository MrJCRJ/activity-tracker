from storage import carregar_dados
from utils import calcular_horas_por_data_e_tarefa
from datetime import datetime, timedelta

def carregar_dados_e_estatisticas():
    dados = carregar_dados()
    if not dados:
        return None, {"mensagem": "Nenhuma atividade registrada para mostrar."}

    estatisticas = calcular_horas_por_data_e_tarefa(dados)
    if not estatisticas:
        return None, {"mensagem": "Nenhuma estatística disponível."}

    return estatisticas, None

def formatar_horas(horas):
    horas_int = int(horas)
    minutos = int((horas - horas_int) * 60)
    return f"{horas_int}h {minutos}m"

def organizar_resumo_por_periodo(estatisticas):
    semanal = {}
    mensal = {}
    anual = {}

    for data, tarefas in estatisticas.items():
        ano, semana, _ = datetime.strptime(data, "%Y-%m-%d").isocalendar()

        if semana not in semanal:
            semanal[semana] = {}
        if ano not in mensal:
            mensal[ano] = {}
        if ano not in anual:
            anual[ano] = {}

        for descricao, horas in tarefas.items():
            semanal[semana][descricao] = semanal[semana].get(descricao, 0) + horas
            if semana not in mensal[ano]:
                mensal[ano][semana] = {}
            mensal[ano][semana][descricao] = mensal[ano][semana].get(descricao, 0) + horas

            anual[ano][descricao] = anual[ano].get(descricao, 0) + horas

    return semanal, mensal, anual

def calcular_dias_procrastinacao(estatisticas):
    dias_procrastinacao = []
    ano_atual = datetime.now().year
    dias_registrados = set(estatisticas.keys())

    data_inicio = datetime(ano_atual, 1, 1)
    data_fim = datetime.now()
    delta = timedelta(days=1)

    while data_inicio <= data_fim:
        data_str = data_inicio.strftime("%Y-%m-%d")
        if data_str not in dias_registrados or sum(estatisticas.get(data_str, {}).values()) < 6:
            total_dia = sum(estatisticas.get(data_str, {}).values())
            dias_procrastinacao.append({"data": data_str, "total_dia": formatar_horas(total_dia)})
        data_inicio += delta

    return dias_procrastinacao

def gerar_resumo_por_data(estatisticas):
    resumo_por_data = {}
    total_por_tarefa = {}

    for data in sorted(estatisticas.keys()):
        tarefas = estatisticas[data]
        total_dia = 0
        resumo_por_data[data] = {}

        for descricao, horas in sorted(tarefas.items(), key=lambda x: x[1], reverse=True):
            resumo_por_data[data][descricao] = formatar_horas(horas)
            total_dia += horas
            total_por_tarefa[descricao] = total_por_tarefa.get(descricao, 0) + horas

        resumo_por_data[data]["total_dia"] = formatar_horas(total_dia)

    return resumo_por_data, total_por_tarefa

def gerar_estatisticas_por_tarefa():
    estatisticas, erro = carregar_dados_e_estatisticas()
    if erro:
        return erro

    resumo_por_data, total_por_tarefa = gerar_resumo_por_data(estatisticas)
    semanal, mensal, anual = organizar_resumo_por_periodo(estatisticas)
    dias_procrastinacao = calcular_dias_procrastinacao(estatisticas)

    resumo_semanal = {semana: {descricao: formatar_horas(horas) for descricao, horas in tarefas.items()} for semana, tarefas in semanal.items()}
    resumo_mensal = {ano: {semana: {descricao: formatar_horas(horas) for descricao, horas in tarefas.items()} for semana, tarefas in semanas.items()} for ano, semanas in mensal.items()}
    resumo_anual = {ano: {descricao: formatar_horas(horas) for descricao, horas in tarefas.items()} for ano, tarefas in anual.items()}

    resumo_por_data_recente = dict(sorted(resumo_por_data.items(), key=lambda x: x[0], reverse=True)[:10])

    return {
        "total_por_tarefa": {descricao: formatar_horas(horas) for descricao, horas in total_por_tarefa.items()},
        "resumo_por_data": resumo_por_data_recente,
        "resumo_semanal": resumo_semanal,
        "resumo_mensal": resumo_mensal,
        "resumo_anual": resumo_anual,
        "dias_procrastinacao": dias_procrastinacao
    }
