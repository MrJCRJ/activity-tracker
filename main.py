# Arquivo principal que inicia o programa e controla o menu.
from actions import registrar_atividade, exibir_atividades, editar_atividade, deletar_atividade

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Registrar nova atividade")
        print("2. Exibir atividades")
        print("3. Editar atividade")
        print("4. Deletar atividade")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_atividade()
        elif opcao == "2":
            exibir_atividades()
        elif opcao == "3":
            editar_atividade()
        elif opcao == "4":
            deletar_atividade()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
