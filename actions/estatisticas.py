from storage import carregar_dados
from utils import calcular_horas_por_data_e_tarefa

def exibir_estatisticas_por_tarefa():
    dados = carregar_dados()
    if not dados:
        print("Nenhuma atividade registrada para mostrar.")
        return
    
    estatisticas = calcular_horas_por_data_e_tarefa(dados)
    
    if not estatisticas:
        print("Nenhuma estatística disponível.")
        return
    
    print("\n=== Estatísticas por Data ===")
    for data in sorted(estatisticas.keys()):  # Ordena as datas em ordem crescente
        print(f"\nData: {data}")
        tarefas = estatisticas[data]
        for descricao, horas in sorted(tarefas.items()):  # Ordena as tarefas alfabeticamente
            print(f"  - {descricao}: {horas:.2f} horas")
    print("=============================")
