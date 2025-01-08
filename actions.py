# Contém as funções para registrar, editar, deletar e exibir atividades.
from storage import carregar_dados, salvar_dados
from datetime import datetime

# Função para validar data e hora
def validate_datetime(input_str, date_time_type):
    try:
        if date_time_type == 'data':
            # Tenta converter a data (AAAA-MM-DD)
            return datetime.strptime(input_str, "%Y-%m-%d").date()
        elif date_time_type == 'hora':
            # Tenta converter a hora (HH:MM)
            return datetime.strptime(input_str, "%H:%M").time()
    except ValueError:
        print(f"{input_str} é inválido! Use o formato correto para {date_time_type}.")
        return None

# Função para registrar uma nova atividade
def registrar_atividade():
    data = input("Data (formato: AAAA-MM-DD): ")
    # Valida a data
    data_validada = validate_datetime(data, 'data')
    if not data_validada:
        return
    
    hora_inicio = input("Hora de início (formato: HH:MM): ")
    # Valida a hora de início
    hora_inicio_validada = validate_datetime(hora_inicio, 'hora')
    if not hora_inicio_validada:
        return
    
    hora_fim = input("Hora de fim (formato: HH:MM): ")
    # Valida a hora de fim
    hora_fim_validada = validate_datetime(hora_fim, 'hora')
    if not hora_fim_validada:
        return
    
    descricao = input("Descrição da atividade: ")

    # Cria o dicionário da atividade com os dados validados
    atividade = {
        "data": data,
        "hora_inicio": hora_inicio,
        "hora_fim": hora_fim,
        "descricao": descricao,
    }

    # Carrega e salva os dados
    dados = carregar_dados()
    dados.append(atividade)
    salvar_dados(dados)
    print("Atividade registrada com sucesso!")

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
