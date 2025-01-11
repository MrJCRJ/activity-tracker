from storage import carregar_dados
from utils import calcular_horas_por_data_e_tarefa
from datetime import datetime, timedelta

def exibir_estatisticas_por_tarefa():
    # Carrega os dados registrados pelo usuário
    dados = carregar_dados()
    if not dados:
        print("Nenhuma atividade registrada para mostrar.")
        return

    # Calcula as estatísticas de horas por data e tarefa
    estatisticas = calcular_horas_por_data_e_tarefa(dados)

    if not estatisticas:
        print("Nenhuma estatística disponível.")
        return

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

    print("\n=== Estatísticas por Data ===")
    for data in sorted(estatisticas.keys()):  # Ordena as datas em ordem crescente
        print(f"\nData: {data}")
        tarefas = estatisticas[data]
        total_dia = 0
        ano, semana, dia_da_semana = datetime.strptime(data, "%Y-%m-%d").isocalendar()

        if semana not in semanal:
            semanal[semana] = {}
        if ano not in mensal:
            mensal[ano] = {}
        if ano not in anual:
            anual[ano] = {}

        for descricao, horas in sorted(tarefas.items(), key=lambda x: x[1], reverse=True):  # Ordena tarefas por maior tempo
            print(f"  - {descricao}: {formatar_horas(horas)}")
            total_dia += horas
            total_por_tarefa[descricao] = total_por_tarefa.get(descricao, 0) + horas

            # Adiciona os valores aos resumos semanais, mensais e anuais
            semanal[semana][descricao] = semanal[semana].get(descricao, 0) + horas
            if semana not in mensal[ano]:
                mensal[ano][semana] = {}
            mensal[ano][semana][descricao] = mensal[ano][semana].get(descricao, 0) + horas

            anual[ano][descricao] = anual[ano].get(descricao, 0) + horas

        print(f"  Total do dia: {formatar_horas(total_dia)}")

    print("\n=== Resumo Semanal ===")
    for semana, tarefas in sorted(semanal.items()):
        print(f"\nSemana {semana}:")
        for descricao, horas in sorted(tarefas.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {descricao}: {formatar_horas(horas)}")

    print("\n=== Resumo Mensal ===")
    for ano, semanas in mensal.items():
        for semana, tarefas in sorted(semanas.items()):
            print(f"\nSemana {semana}/{ano}:")
            for descricao, horas in sorted(tarefas.items(), key=lambda x: x[1], reverse=True):
                print(f"  - {descricao}: {formatar_horas(horas)}")

    print("\n=== Resumo Anual ===")
    for ano, tarefas in sorted(anual.items()):
        print(f"\nAno {ano}:")
        for descricao, horas in sorted(tarefas.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {descricao}: {formatar_horas(horas)}")

    print("\n=== Dias de Procrastinação ou Férias ===")
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
            print(f"  - {data_str}: {formatar_horas(total_dia)}")
        data_inicio += delta

    print("=============================")
    print("Fim das estatísticas.")
    print("=============================")
    return
