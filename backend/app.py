from flask import Flask, jsonify, request
from actions.estatisticas import gerar_estatisticas_por_tarefa
from actions.registro import registrar
from flask_cors import CORS

# Cria a aplicação Flask
app = Flask(__name__)
CORS(app)  # Habilita o CORS para permitir acesso de diferentes origens

# Rotas para gerenciar as atividades
atividades = []  # Simulando um banco de dados com uma lista em memória

@app.route('/api/estatisticas', methods=['GET'])
def api_estatisticas():
    """
    Endpoint para gerar estatísticas de atividades.
    Retorna um JSON com as estatísticas calculadas.
    """
    estatisticas = gerar_estatisticas_por_tarefa()
    return jsonify(estatisticas)

@app.route('/api/registrar_atividade', methods=['POST'])
def registrar_atividade():
    """
    Endpoint para registrar uma nova atividade.
    Espera um JSON com 'data', 'hora_inicio', 'hora_fim' e 'descricao'.
    """
    print("Registrar nova atividade")
    try:
        # Obtém os dados do corpo da requisição
        dados_recebidos = request.json
        registrar(dados_recebidos['data'], dados_recebidos['hora_inicio'], dados_recebidos['hora_fim'], dados_recebidos['descricao'])
        # Armazena a atividade na lista (simulando um banco de dados)
        atividades.append(dados_recebidos)
        return jsonify({"message": "Atividade registrada com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/atividades', methods=['GET'])
def listar_atividades():
    """
    Endpoint para listar todas as atividades registradas.
    Retorna uma lista de atividades em JSON.
    """
    return jsonify(atividades)

@app.route('/api/atividades/<int:index>', methods=['PUT'])
def editar_atividade(index):
    """
    Endpoint para editar uma atividade existente.
    Espera um JSON com os novos dados.
    """
    try:
        dados_atualizados = request.json
        if index < 0 or index >= len(atividades):
            return jsonify({"error": "Atividade não encontrada."}), 404
        atividades[index] = dados_atualizados
        return jsonify({"message": "Atividade atualizada com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/atividades/<int:index>', methods=['DELETE'])
def deletar_atividade(index):
    """
    Endpoint para deletar uma atividade pelo índice.
    """
    try:
        if index < 0 or index >= len(atividades):
            return jsonify({"error": "Atividade não encontrada."}), 404
        atividades.pop(index)
        return jsonify({"message": "Atividade removida com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000)
