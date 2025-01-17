from datetime import datetime
from InquirerPy import prompt
from utils import validate_datetime
import requests

def registrar_atividade():
    data_atual = datetime.now().strftime('%Y-%m-%d')
    hora_atual = datetime.now().strftime('%H%M')
    descricoes_sugeridas = ["Trabalho Padaria", "Projeto Activity Tracker", "Faxina da Casa", "Treino Iniciante de Calistenia", "Curso.dev"]

    perguntas = [
        {"type": "input", "name": "data", "message": f"Data (AAAA-MM-DD) [Sugestão: {data_atual}]:", "default": data_atual},
        {"type": "input", "name": "hora_inicio", "message": "Hora de início (HHMM):"},
        {"type": "input", "name": "hora_fim", "message": "Hora de fim (HHMM):"},
        {"type": "list", "name": "descricao", "message": "Descrição:", "choices": descricoes_sugeridas},
    ]

    respostas = prompt(perguntas)

    if not validate_datetime(respostas['data'], 'data') or \
       not validate_datetime(respostas['hora_inicio'], 'hora') or \
       not validate_datetime(respostas['hora_fim'], 'hora'):
        print("Dados inválidos. Tente novamente.")
        return

    atividade = {
        "data": respostas['data'],
        "hora_inicio": respostas['hora_inicio'][:2] + ':' + respostas['hora_inicio'][2:],
        "hora_fim": respostas['hora_fim'][:2] + ':' + respostas['hora_fim'][2:],
        "descricao": respostas['descricao'],
    }

    # Enviar para o backend
    url_backend = 'http://127.0.0.1:5000/api/registrar_atividade'
    try:
        response = requests.post(url_backend, json=atividade)
        if response.status_code == 200:
            print("Atividade registrada com sucesso no servidor!")
        else:
            print("Erro ao registrar atividade no servidor:", response.json())
    except Exception as e:
        print(f"Erro ao se comunicar com o servidor: {e}")

def editar_atividade():
    print("Editar uma atividade existente")
    # Chamar API ou implementar lógica local

def deletar_atividade():
    print("Deletar uma atividade existente")
    # Chamar API ou implementar lógica local

def salvar_em_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
    print(f"Conteúdo salvo em {nome_arquivo}")

def exibir_estatisticas():
    print("Exibir estatísticas")
    try:
        response = requests.get("http://127.0.0.1:5000/api/estatisticas")
        if response.status_code == 200:
            estatisticas = response.json()

            # Exibir e salvar Dias de Procrastinação
            dias_procrastinacao = "\n=== Dias de Procrastinação ou Férias ===\n"
            for dia in estatisticas.get("dias_procrastinacao", []):
                dias_procrastinacao += f"  - {dia['data']}: {dia['total_dia']}\n"
            salvar_em_arquivo("dias_procrastinacao.txt", dias_procrastinacao)

            # Exibir e salvar Resumo Anual
            resumo_anual = "\n=== Resumo Anual ===\n"
            for ano, tarefas in estatisticas.get("resumo_anual", {}).items():
                resumo_anual += f"\nAno {ano}:\n"
                for tarefa, horas in tarefas.items():
                    resumo_anual += f"  - {tarefa}: {horas:.2f} horas\n"
            salvar_em_arquivo("resumo_anual.txt", resumo_anual)

            # Exibir e salvar Resumo Mensal
            resumo_mensal = "\n=== Resumo Mensal ===\n"
            for ano, meses in estatisticas.get("resumo_mensal", {}).items():
                for mes, tarefas in meses.items():
                    resumo_mensal += f"\nMês {mes}/{ano}:\n"
                    for tarefa, horas in tarefas.items():
                        resumo_mensal += f"  - {tarefa}: {horas:.2f} horas\n"
            salvar_em_arquivo("resumo_mensal.txt", resumo_mensal)

            # Exibir e salvar Resumo por Data
            resumo_por_data = "\n=== Resumo por Data ===\n"
            for data, tarefas in estatisticas.get("resumo_por_data", {}).items():
                resumo_por_data += f"\nData {data}:\n"
                for tarefa, horas in tarefas.items():
                    if tarefa != "total_dia":
                        resumo_por_data += f"  - {tarefa}: {horas}\n"
                resumo_por_data += f"  Total do dia: {tarefas['total_dia']}\n"
            salvar_em_arquivo("resumo_por_data.txt", resumo_por_data)

            # Exibir e salvar Resumo Semanal
            resumo_semanal = "\n=== Resumo Semanal ===\n"
            for semana, tarefas in estatisticas.get("resumo_semanal", {}).items():
                resumo_semanal += f"\nSemana {semana}:\n"
                for tarefa, horas in tarefas.items():
                    resumo_semanal += f"  - {tarefa}: {horas:.2f} horas\n"
            salvar_em_arquivo("resumo_semanal.txt", resumo_semanal)

        else:
            print(response.json().get("error", "Erro ao obter estatísticas"))
    except requests.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor.")
