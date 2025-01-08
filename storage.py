# Responsável por carregar e salvar os dados no arquivo JSON.
import json

DATA_FILE = "atividades.json"

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não existir

# Função para salvar os dados no arquivo JSON
def salvar_dados(dados):
    with open(DATA_FILE, "w") as file:
        json.dump(dados, file, indent=4)
