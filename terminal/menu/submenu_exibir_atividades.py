from InquirerPy import prompt

def submenu_exibir_atividades():
    """
    Exibe um submenu para escolher como visualizar as atividades.
    Caso não existam dados, retorna uma mensagem.
    """
    dados = 'carregar_dados()'
    if not dados:
        print("Nenhuma atividade registrada.")
        return

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
        print('exibir_atividade')
    elif answer == "Filtrar atividades por data":
        print('exibir_atividades_por_data')
