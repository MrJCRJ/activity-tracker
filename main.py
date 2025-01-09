from InquirerPy import prompt
from actions import registrar_atividade, editar_atividade, deletar_atividade, exibir_atividades, exibir_atividades_por_data, exibir_estatisticas_por_tarefa
from storage import carregar_dados

def menu_principal():
    while True:
        # Menu principal
        menu_options = {
            "Registrar nova atividade": registrar_atividade,
            "Exibir atividades": submenu_exibir_atividades,
            "Editar atividade": editar_atividade,
            "Deletar atividade": deletar_atividade,
            "Exibir estatísticas": exibir_estatisticas_por_tarefa,
            "Sair": None,
        }

        question = [
            {
                "type": "list",
                "name": "menu_choice",
                "message": "Escolha uma opção:",
                "choices": list(menu_options.keys()),
            }
        ]

        answer = prompt(question)["menu_choice"]
        if answer == "Sair":
            print("Saindo do programa. Até logo!")
            break

        # Executa a função correspondente à opção escolhida
        action = menu_options.get(answer)
        if action:
            action()

def submenu_exibir_atividades():
    dados = carregar_dados()
    if not dados:
        print("Nenhuma atividade registrada.")
        return

    # Submenu para exibição de atividades
    question = [
        {
            "type": "list",
            "name": "submenu_choice",
            "message": "Escolha como exibir as atividades:",
            "choices": [
                "Exibir todas as atividades",
                "Filtrar atividades por data",
                "Voltar ao menu principal",
            ],
        }
    ]

    answer = prompt(question)["submenu_choice"]
    if answer == "Exibir todas as atividades":
        exibir_atividades()
    elif answer == "Filtrar atividades por data":
        exibir_atividades_por_data()

if __name__ == "__main__":
    menu_principal()
