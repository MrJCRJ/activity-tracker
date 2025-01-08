# Contém as funções para registrar, editar, deletar e exibir atividades.
from storage import carregar_dados, salvar_dados

# Função para registrar uma nova atividade
def registrar_atividade():
    data = input("Data (formato: AAAA-MM-DD): ")
    hora_inicio = input("Hora de início (formato: HH:MM): ")
    hora_fim = input("Hora de fim (formato: HH:MM): ")
    descricao = input("Descrição da atividade: ")

    atividade = {
        "data": data,
        "hora_inicio": hora_inicio,
        "hora_fim": hora_fim,
        "descricao": descricao,
    }

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
        return

    indice = int(input("Digite o número da atividade que deseja editar: ")) - 1
    if 0 <= indice < len(dados):
        print("Deixe o campo vazio para manter o valor atual.")
        data = input(f"Nova data (atual: {dados[indice]['data']}): ") or dados[indice]['data']
        hora_inicio = input(f"Nova hora de início (atual: {dados[indice]['hora_inicio']}): ") or dados[indice]['hora_inicio']
        hora_fim = input(f"Nova hora de fim (atual: {dados[indice]['hora_fim']}): ") or dados[indice]['hora_fim']
        descricao = input(f"Nova descrição (atual: {dados[indice]['descricao']}): ") or dados[indice]['descricao']

        dados[indice] = {
            "data": data,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim,
            "descricao": descricao,
        }
        salvar_dados(dados)
        print("Atividade editada com sucesso!")
    else:
        print("Número de atividade inválido.")

# Função para deletar uma atividade
def deletar_atividade():
    exibir_atividades()
    dados = carregar_dados()
    if not dados:
        return

    indice = int(input("Digite o número da atividade que deseja deletar: ")) - 1
    if 0 <= indice < len(dados):
        confirmacao = input(f"Tem certeza que deseja deletar a atividade '{dados[indice]['descricao']}'? (s/n): ")
        if confirmacao.lower() == 's':
            del dados[indice]
            salvar_dados(dados)
            print("Atividade deletada com sucesso!")
    else:
        print("Número de atividade inválido.")
