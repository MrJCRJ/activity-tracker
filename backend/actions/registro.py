from storage import carregar_dados, salvar_dados
from flask import jsonify
from utils import validate_datetime

def registrar(data, hora_inicio, hora_fim, descricao):
    
    # Montando a atividade a ser salva
    atividade = {
        "data": data,
        "hora_inicio": hora_inicio,
        "hora_fim": hora_fim,
        "descricao": descricao,
    }
    try:
        dados = carregar_dados()
        dados.append(atividade)
        salvar_dados(dados)
        return jsonify({"message": "Atividade registrada com sucesso!"}), 200
    except Exception as e:
        print(f"Erro ao salvar a atividade: {e}")  # Log do erro
        return jsonify({"error": f"Erro ao salvar a atividade: {str(e)}"}), 500
