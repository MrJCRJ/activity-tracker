# main.py: Arquivo principal do programa
from actions.registro import registrar_atividade
from actions.exibicao import exibir_atividades, exibir_atividades_por_data
from actions.edicao import editar_atividade
from actions.delecao import deletar_atividade
from actions.estatisticas import exibir_estatisticas_por_tarefa
from InquirerPy import prompt
from storage import carregar_dados

def menu_principal():
    """
    Exibe o menu principal e gerencia a execução das opções.
    """
    while True:
        # Mapeamento de opções do menu para funções
        menu_options = {
            "Registrar nova atividade": registrar_atividade,
            "Exibir atividades": submenu_exibir_atividades,
            "Editar atividade": editar_atividade,
            "Deletar atividade": deletar_atividade,
            "Exibir estatísticas": exibir_estatisticas_por_tarefa,
            "Sair": None,
        }

        # Pergunta do menu principal
        question = [
            {
                "type": "list",
                "name": "menu_choice",
                "message": "Escolha uma opção:",
                "choices": list(menu_options.keys()),
            }
        ]

        # Captura a escolha do usuário
        answer = prompt(question)["menu_choice"]
        
        if answer == "Sair":
            print("Saindo do programa. Até logo!")
            break

        # Executa a função correspondente à escolha do menu
        action = menu_options.get(answer)
        if action:
            action()

def submenu_exibir_atividades():
    """
    Exibe um submenu para escolher como visualizar as atividades.
    Caso não existam dados, retorna uma mensagem.
    """
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

    # Captura a escolha do submenu
    answer = prompt(question)["submenu_choice"]
    if answer == "Exibir todas as atividades":
        exibir_atividades()
    elif answer == "Filtrar atividades por data":
        exibir_atividades_por_data()

if __name__ == "__main__":
    # Inicializa o programa chamando o menu principal
    menu_principal()
