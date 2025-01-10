# actions.py: Contém as funções para registrar, editar, deletar e exibir atividades.
# Contém as funções para registrar, editar, deletar e exibir atividades.
from storage import carregar_dados, salvar_dados
from datetime import datetime
from utils import calcular_horas_por_data_e_tarefa
from InquirerPy import prompt

# Função para validar data e hora
def validate_datetime(valor, tipo):
    try:
        if tipo == 'data':
            datetime.strptime(valor, "%Y-%m-%d")  # Valida a data no formato AAAA-MM-DD
        elif tipo == 'hora':
            if len(valor) == 4 and valor.isdigit():  # Verifica se a hora está no formato HHMM
                hora = int(valor[:2])
                minuto = int(valor[2:])
                if 0 <= hora <= 23 and 0 <= minuto <= 59:
                    return True
            return False
    except ValueError:
        return False
    return True

# Função para registrar uma nova atividade
def registrar_atividade():
    # Sugestão de data e hora atual para facilitar o preenchimento
    data_atual = datetime.now().strftime('%Y-%m-%d')
    hora_atual = datetime.now().strftime('%H%M')  # Hora no formato HHMM, sem ":".

    # Lista de descrições sugeridas
    descricoes_sugeridas = [
        "Trabalho Padaria",
        "Projeto Activity Tracker",
        "Faxina da Casa",
        "Treino Iniciante de Calistenia",
    ]

    # Usando o InquirerPy para solicitar os dados
    perguntas = [
        {
            'type': 'input',
            'name': 'data',
            'message': f"Data (formato: AAAA-MM-DD) [Sugestão: {data_atual}]:",
            'default': data_atual
        },
        {
            'type': 'input',
            'name': 'hora_inicio',
            'message': f"Hora de início (formato: HHMM):",
        },
        {
            'type': 'input',
            'name': 'hora_fim',
            'message': "Hora de fim (formato: HHMM):"
        },
        {
            'type': 'list',
            'name': 'descricao',
            'message': "Escolha uma descrição ou digite uma nova:",
            'choices': descricoes_sugeridas
        }
    ]

    respostas = prompt(perguntas)

    # Validar data e horas
    data_validada = validate_datetime(respostas['data'], 'data')
    if not data_validada:
        print("Data inválida. Tente novamente.")
        return

    hora_inicio_validada = validate_datetime(respostas['hora_inicio'], 'hora')  # Não precisa de ':' aqui
    if not hora_inicio_validada:
        print("Hora de início inválida. Tente novamente.")
        return

    hora_fim_validada = validate_datetime(respostas['hora_fim'], 'hora')  # Não precisa de ':' aqui
    if not hora_fim_validada:
        print("Hora de fim inválida. Tente novamente.")
        return

    # Cria o dicionário da atividade com os dados validados
    atividade = {
        "data": respostas['data'],
        "hora_inicio": respostas['hora_inicio'][:2] + ':' + respostas['hora_inicio'][2:],  # Converte para HH:MM
        "hora_fim": respostas['hora_fim'][:2] + ':' + respostas['hora_fim'][2:],  # Converte para HH:MM
        "descricao": respostas['descricao'],
    }

    # Carrega e salva os dados
    dados = carregar_dados()
    dados.append(atividade)
    salvar_dados(dados)
    print("Atividade registrada com sucesso!")

# Filtro por data
def filtrar_por_data(dados, data):
    atividades_filtradas = [atividade for atividade in dados if atividade['data'] == data]
    return atividades_filtradas

# Exibir atividades filtradas por data
def exibir_atividades_por_data():
    dados = carregar_dados()
    if not dados:
        print("Não há atividades registradas.")
        return
    
    # Ordena as atividades pela data e hora de início
    dados.sort(key=lambda x: (x["data"], x["hora_inicio"]))

    data = input("Digite a data desejada (formato: AAAA-MM-DD): ")

    atividades_filtradas = filtrar_por_data(dados, data)

    if atividades_filtradas:
        print(f"Atividades na data {data}:")
        for atividade in atividades_filtradas:
            print(f"{atividade['hora_inicio']} - {atividade['hora_fim']} | {atividade['descricao']}")
    else:
        print(f"Não foram encontradas atividades para a data {data}.")


# Função para exibir todas as atividades registradas
def exibir_atividades():
    
    dados = carregar_dados()
    if not dados:
        print("Nenhuma atividade registrada.")
        return
    
    # Ordena as atividades pela data e hora de início
    dados.sort(key=lambda x: (x["data"], x["hora_inicio"]))

    print("\n=== Atividades Registradas ===")
    for i, atividade in enumerate(dados, 1):
        print(f"{i}. {atividade['data']} | {atividade['hora_inicio']} - {atividade['hora_fim']} | {atividade['descricao']}")
    print("==============================\n")

# Função para editar uma atividade
def editar_atividade():
    exibir_atividades()
    dados = carregar_dados()
    if not dados:
        print("Não há atividades registradas.")
        return

    try:
        indice = int(input("Digite o número da atividade que deseja editar: ")) - 1
        if 0 <= indice < len(dados):
            print("Deixe o campo vazio para manter o valor atual.")

            # Edita a data com validação
            nova_data = input(f"Nova data (atual: {dados[indice]['data']}): ") or dados[indice]['data']
            nova_data_validada = validate_datetime(nova_data, 'data') if nova_data else dados[indice]['data']
            if nova_data and not nova_data_validada:
                return
            
            # Edita a hora de início com validação
            nova_hora_inicio = input(f"Nova hora de início (atual: {dados[indice]['hora_inicio']}): ") or dados[indice]['hora_inicio']
            nova_hora_inicio_validada = validate_datetime(nova_hora_inicio, 'hora') if nova_hora_inicio else dados[indice]['hora_inicio']
            if nova_hora_inicio and not nova_hora_inicio_validada:
                return

            # Edita a hora de fim com validação
            nova_hora_fim = input(f"Nova hora de fim (atual: {dados[indice]['hora_fim']}): ") or dados[indice]['hora_fim']
            nova_hora_fim_validada = validate_datetime(nova_hora_fim, 'hora') if nova_hora_fim else dados[indice]['hora_fim']
            if nova_hora_fim and not nova_hora_fim_validada:
                return

            # Edita a descrição
            nova_descricao = input(f"Nova descrição (atual: {dados[indice]['descricao']}): ") or dados[indice]['descricao']

            # Atualiza os dados da atividade
            dados[indice] = {
                "data": nova_data_validada,
                "hora_inicio": nova_hora_inicio_validada,
                "hora_fim": nova_hora_fim_validada,
                "descricao": nova_descricao,
            }
            
            salvar_dados(dados)
            print("Atividade editada com sucesso!")
        else:
            print("Número de atividade inválido.")

    except ValueError:
        print("Entrada inválida! Certifique-se de digitar um número válido para o índice da atividade.")

# Função para deletar uma atividade
def deletar_atividade():
    exibir_atividades()
    dados = carregar_dados()
    if not dados:
        print("Não há atividades registradas.")
        return

    try:
        indice = int(input("Digite o número da atividade que deseja deletar: ")) - 1
        if 0 <= indice < len(dados):
            print(f"Você está prestes a deletar a seguinte atividade:")
            print(f"Data: {dados[indice]['data']}, Início: {dados[indice]['hora_inicio']}, Fim: {dados[indice]['hora_fim']}")
            confirmacao = input("Tem certeza que deseja deletar? (s/n): ").lower()
            if confirmacao == 's':
                dados.pop(indice)
                salvar_dados(dados)
                print("Atividade deletada com sucesso!")
            else:
                print("Deleção cancelada.")
        else:
            print("Número de atividade inválido.")
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar um número válido para o índice da atividade.")

# Função para calcular o total de horas por data
def exibir_estatisticas_por_tarefa():
    dados = carregar_dados()
    if not dados:
        print("Nenhuma atividade registrada para exibir estatísticas.")
        return

    estatisticas = calcular_horas_por_data_e_tarefa(dados)

    print("\n=== Estatísticas por Data ===")
    for data, tarefas in sorted(estatisticas.items()):
        print(f"\nData: {data}")
        total_horas = sum(tarefas.values())
        print(f"Total de horas: {total_horas:.2f}")
        for descricao, horas in sorted(tarefas.items()):
            print(f"  - {descricao}: {horas:.2f} horas")
    print("=============================\n")

