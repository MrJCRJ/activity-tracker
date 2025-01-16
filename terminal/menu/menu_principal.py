from InquirerPy import prompt
from menu.submenu_exibir_atividades import submenu_exibir_atividades
from actions import registrar_atividade, editar_atividade, deletar_atividade, exibir_estatisticas

def menu_principal():
    """
    Exibe o menu principal e gerencia a execução das opções.
    """
    while True:
        menu_options = {
            "Registrar nova atividade": registrar_atividade,
            "Exibir atividades": submenu_exibir_atividades,
            "Editar atividade": editar_atividade,
            "Deletar atividade": deletar_atividade,
            "Exibir estatísticas": exibir_estatisticas,
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

        action = menu_options.get(answer)
        if action:
            action()
