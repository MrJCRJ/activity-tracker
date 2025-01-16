from flask import Flask, jsonify, request
from actions.estatisticas import gerar_estatisticas_por_tarefa
from actions.registro import registrar
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Isso habilita o CORS para todas as rotas

@app.route('/api/estatisticas', methods=['GET'])
def api_estatisticas():
    estatisticas = gerar_estatisticas_por_tarefa()
    return jsonify(estatisticas)

@app.route('/api/registrar_atividade', methods=['POST'])
def registrar_atividade():
    print("Registrar nova atividade")
    
    try:
        # Chama a função registrar() com os dados recebidos do request
        dados_recebidos = request.json
        registrar(dados_recebidos['data'], dados_recebidos['hora_inicio'], dados_recebidos['hora_fim'], dados_recebidos['descricao'])
        return jsonify({"message": "Atividade registrada com sucesso!"}), 200  # Resposta válida
    except Exception as e:
        # Caso ocorra um erro, retorne uma resposta de erro
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(port=5000)
