from storage import carregar_dados, salvar_dados
from actions.exibicao import exibir_atividades

def deletar_atividade():
    try:
        exibir_atividades()
        dados = carregar_dados()
        if not dados:
            print("Não há atividades registradas.")
            return
        
        while True:
            try:
                indice = int(input("Digite o número da atividade para deletar: ")) - 1
                if 0 <= indice < len(dados):
                    atividade = dados[indice]
                    print("\nVocê está prestes a deletar a seguinte atividade:")
                    print(f"Data: {atividade['data']}")
                    print(f"Hora: {atividade['hora_inicio']} - {atividade['hora_fim']}")
                    print(f"Descrição: {atividade['descricao']}")
                    
                    confirmar = input("Confirmar exclusão? (s/n): ").lower()
                    if confirmar == 's':
                        dados.pop(indice)
                        salvar_dados(dados)
                        print("Atividade deletada com sucesso!")
                    else:
                        print("Operação cancelada.")
                    break
                else:
                    print("Número inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    except Exception as e:
        print(f"Erro ao deletar atividade: {e}")
