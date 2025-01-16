from storage import carregar_dados
from utils import calcular_horas_por_data_e_tarefa
from datetime import datetime, timedelta

def gerar_estatisticas_por_tarefa():
    # Carrega os dados registrados pelo usuário
    dados = carregar_dados()
    if not dados:
        return {"mensagem": "Nenhuma atividade registrada para mostrar."}

    # Calcula as estatísticas de horas por data e tarefa
    estatisticas = calcular_horas_por_data_e_tarefa(dados)

    if not estatisticas:
        return {"mensagem": "Nenhuma estatística disponível."}

    total_por_tarefa = {}

    # Função para formatar horas no estilo "Xh Ym"
    def formatar_horas(horas):
        horas_int = int(horas)
        minutos = int((horas - horas_int) * 60)
        return f"{horas_int}h {minutos}m"

    # Organiza dados por semanas, meses e anos
    semanal = {}
    mensal = {}
    anual = {}

    resumo_por_data = {}

    for data in sorted(estatisticas.keys()):  # Ordena as datas em ordem crescente
        tarefas = estatisticas[data]
        total_dia = 0
        ano, semana, dia_da_semana = datetime.strptime(data, "%Y-%m-%d").isocalendar()

        if semana not in semanal:
            semanal[semana] = {}
        if ano not in mensal:
            mensal[ano] = {}
        if ano not in anual:
            anual[ano] = {}

        resumo_por_data[data] = {}

        for descricao, horas in sorted(tarefas.items(), key=lambda x: x[1], reverse=True):  # Ordena tarefas por maior tempo
            resumo_por_data[data][descricao] = formatar_horas(horas)
            total_dia += horas
            total_por_tarefa[descricao] = total_por_tarefa.get(descricao, 0) + horas

            # Adiciona os valores aos resumos semanais, mensais e anuais
            semanal[semana][descricao] = semanal[semana].get(descricao, 0) + horas
            if semana not in mensal[ano]:
                mensal[ano][semana] = {}
            mensal[ano][semana][descricao] = mensal[ano][semana].get(descricao, 0) + horas

            anual[ano][descricao] = anual[ano].get(descricao, 0) + horas

        resumo_por_data[data]["total_dia"] = formatar_horas(total_dia)

    dias_procrastinacao = []
    ano_atual = datetime.now().year
    dias_registrados = set(estatisticas.keys())

    # Verifica todos os dias do ano até a data atual
    data_inicio = datetime(ano_atual, 1, 1)
    data_fim = datetime.now()
    delta = timedelta(days=1)

    while data_inicio <= data_fim:
        data_str = data_inicio.strftime("%Y-%m-%d")
        if data_str not in dias_registrados or sum(estatisticas.get(data_str, {}).values()) < 6:
            total_dia = sum(estatisticas.get(data_str, {}).values())
            dias_procrastinacao.append({"data": data_str, "total_dia": formatar_horas(total_dia)})
        data_inicio += delta

    return {
        "resumo_por_data": resumo_por_data,
        "resumo_semanal": semanal,
        "resumo_mensal": mensal,
        "resumo_anual": anual,
        "dias_procrastinacao": dias_procrastinacao
    }