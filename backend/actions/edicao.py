from backend.storage import carregar_dados, salvar_dados
from backend.utils import validate_datetime
from actions.exibicao import exibir_atividades

def editar_atividade():
    exibir_atividades()
    dados = carregar_dados()
    if not dados:
        print("Não há atividades registradas.")
        return

    try:
        indice = int(input("Digite o número da atividade para editar: ")) - 1
        if 0 <= indice < len(dados):
            atividade_atual = dados[indice]
            print("Deixe o campo vazio para manter o valor atual.")

            nova_data = input(f"Nova data (atual: {atividade_atual['data']}): ") or atividade_atual['data']
            nova_hora_inicio = input(f"Nova hora de início (atual: {atividade_atual['hora_inicio']}): ") or atividade_atual['hora_inicio']
            nova_hora_fim = input(f"Nova hora de fim (atual: {atividade_atual['hora_fim']}): ") or atividade_atual['hora_fim']
            nova_descricao = input(f"Nova descrição (atual: {atividade_atual['descricao']}): ") or atividade_atual['descricao']

            if validate_datetime(nova_data, 'data') and validate_datetime(nova_hora_inicio, 'hora') and validate_datetime(nova_hora_fim, 'hora'):
                dados[indice] = {
                    "data": nova_data,
                    "hora_inicio": nova_hora_inicio,
                    "hora_fim": nova_hora_fim,
                    "descricao": nova_descricao,
                }
                salvar_dados(dados)
                print("Atividade editada com sucesso!")
            else:
                if not validate_datetime(nova_data, 'data'):
                    print("Data inválida! Use o formato AAAA-MM-DD.")
                elif not (validate_datetime(nova_hora_inicio, 'hora') and validate_datetime(nova_hora_fim, 'hora')):
                    print("Hora inválida! Use o formato HHMM (ex.: 0930 para 9h30).")
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}.")
