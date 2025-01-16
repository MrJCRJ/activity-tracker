from backend.storage import carregar_dados
from backend.utils import filtrar_por_data, validate_datetime

def exibir_atividades():
    try:
        dados = carregar_dados()
        if not dados:
            print("Nenhuma atividade registrada.")
            return

        dados.sort(key=lambda x: (x["data"], x["hora_inicio"]))
        print("\n=== Atividades Registradas ===")
        for i, atividade in enumerate(dados, 1):
            print(f"{i:<3} {atividade['data']:<10} {atividade['hora_inicio']} - {atividade['hora_fim']:<11} {atividade['descricao']}")
        print("==============================\n")
    except Exception as e:
        print(f"Erro ao exibir atividades: {e}")

def exibir_atividades_por_data():
    try:
        dados = carregar_dados()
        if not dados:
            print("Não há atividades registradas.")
            return

        data = input("Digite a data desejada (AAAA-MM-DD): ")
        if not validate_datetime(data, 'data'):
            print("Data inválida! Use o formato AAAA-MM-DD.")
            return

        atividades = filtrar_por_data(dados, data)
        if atividades:
            print(f"\nAtividades na data {data}:")
            for atividade in atividades:
                print(f"{atividade['hora_inicio']} - {atividade['hora_fim']} | {atividade['descricao']}")
        else:
            print(f"Nenhuma atividade encontrada para {data}.")
    except Exception as e:
        print(f"Erro ao filtrar atividades por data: {e}")
