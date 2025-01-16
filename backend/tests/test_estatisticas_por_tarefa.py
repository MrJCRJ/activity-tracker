import pytest
from unittest.mock import patch
from actions.estatisticas import exibir_estatisticas_por_tarefa


# Teste da função de exibição de estatísticas
@patch("storage.carregar_dados")
@patch("utils.calcular_horas_por_data_e_tarefa")
def test_exibir_estatisticas_por_tarefa(mock_calcular_horas, mock_carregar_dados):
    # Mockando os dados retornados por carregar_dados
    mock_carregar_dados.return_value = [
        {"data": "2025-01-09", "hora_inicio": "05:30", "hora_fim": "07:30", "descricao": "Trabalho Padaria"},
        {"data": "2025-01-09", "hora_inicio": "08:00", "hora_fim": "09:00", "descricao": "Treino"},
    ]

    # Mockando o retorno de calcular_horas_por_data_e_tarefa
    mock_calcular_horas.return_value = {
        "2025-01-09": {
            "Trabalho Padaria": 2.0,
            "Treino": 1.0,
        }
    }

    # Criando o que esperamos que seja impresso no console
    expected_output = (
        "\n=== Estatísticas por Data ===\n\nData: 2025-01-09\n"
        "  - Trabalho Padaria: 2h 0m\n  - Treino: 1h 0m\n"
        "  Total do dia: 3h 0m\n"
        "\n=== Resumo Semanal ===\n\nSemana 1:\n  - Trabalho Padaria: 2h 0m\n  - Treino: 1h 0m\n"
        "\n=== Resumo Mensal ===\n\nSemana 1/2025:\n  - Trabalho Padaria: 2h 0m\n  - Treino: 1h 0m\n"
        "\n=== Resumo Anual ===\n\nAno 2025:\n  - Trabalho Padaria: 2h 0m\n  - Treino: 1h 0m\n"
        "\n=== Dias de Procrastinação ou Férias ===\n"
        "  - 2025-01-01: 0h 0m\n  - 2025-01-02: 0h 0m\n"
        "  - 2025-01-03: 0h 0m\n  - 2025-01-04: 0h 0m\n"
        "  - 2025-01-05: 0h 0m\n  - 2025-01-06: 0h 0m\n"
        "  - 2025-01-07: 0h 0m\n  - 2025-01-08: 0h 0m\n"
        "=============================\nFim das estatísticas.\n=============================\n"
    )

    # Usamos pytest capsys para capturar a saída do print
    with patch("builtins.print") as mock_print:
        exibir_estatisticas_por_tarefa()

        # Verificamos se o que foi impresso é o que esperamos
        mock_print.assert_any_call(expected_output)

