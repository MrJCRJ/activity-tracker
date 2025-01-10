from storage import carregar_dados, salvar_dados
from datetime import datetime
from InquirerPy import prompt
from utils import validate_datetime

def registrar_atividade():
    data_atual = datetime.now().strftime('%Y-%m-%d')
    hora_atual = datetime.now().strftime('%H%M')
    descricoes_sugeridas = ["Trabalho Padaria", "Projeto Activity Tracker", "Faxina da Casa", "Treino Iniciante de Calistenia"]

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

    dados = carregar_dados()
    dados.append(atividade)
    salvar_dados(dados)
    print("Atividade registrada com sucesso!")
