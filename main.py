# Arquivo principal que inicia o programa e controla o menu.
from actions import registrar_atividade, exibir_atividades, editar_atividade, deletar_atividade, exibir_atividades_por_data, exibir_estatisticas
from storage import carregar_dados

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Registrar nova atividade")
        print("2. Exibir atividades")
        print("3. Editar atividade")
        print("4. Deletar atividade")
        print("5. Exibir estatísticas")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_atividade()
        elif opcao == "2":
            submenu_exibir_atividades()
        elif opcao == "3":
            editar_atividade()
        elif opcao == "4":
            deletar_atividade()
        elif opcao == "5":
            exibir_estatisticas()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Submenu para exibir atividades
def submenu_exibir_atividades():
    dados = carregar_dados()
    if not dados:
        print("Não há atividades registradas.")
        return

    while True:
        print("\n=== Exibir Atividades ===")
        print("1. Exibir todas as atividades")
        print("2. Filtrar atividades por data")
        print("0. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_atividades()
        elif opcao == "2":
            exibir_atividades_por_data()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
