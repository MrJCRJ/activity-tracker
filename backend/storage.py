import json
from pathlib import Path

# Caminho padrão do arquivo de dados
DATA_FILE = Path("data/atividades.json")

def carregar_dados():
    """
    Carrega os dados do arquivo JSON.
    Retorna uma lista vazia caso o arquivo não exista ou esteja vazio.
    """
    try:
        if not DATA_FILE.exists():
            print("Arquivo não encontrado, retornando lista vazia.")
            return []  # Se o arquivo não existe, retornamos uma lista vazia
        with DATA_FILE.open("r") as file:
            dados = json.load(file)
            return dados
    except (json.JSONDecodeError, IOError) as e:
        print(f"Erro ao carregar dados: {e}")
        return []

def salvar_dados(dados):
    """
    Salva os dados no arquivo JSON.
    Cria o diretório do arquivo, se necessário.
    """
    try:
        # Verifica se o diretório existe e cria se necessário
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with DATA_FILE.open("w") as file:
            json.dump(dados, file, indent=4)
    except IOError as e:
        print(f"Erro ao salvar dados: {e}")
