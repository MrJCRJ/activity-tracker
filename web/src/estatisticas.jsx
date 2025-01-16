import React, { useEffect, useState } from "react";
import api from "./services/api";
import "./estatisticas.css";

function Estatisticas() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await api.get("/estatisticas");
        setData(response.data);
      } catch (err) {
        setError("Erro ao buscar dados");
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  if (loading) return <p>Carregando...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div className="container">
      <h2 className="title">Estatísticas</h2>

      {/* Container para as seções lado a lado */}
      <div className="sections">
        <div className="section-container">
          <h3 className="subtitle">Dias de Procrastinação ou Férias</h3>
          <ul className="stat-list">
            {data.dias_procrastinacao.map((dia, index) => (
              <li className="stat-item" key={index}>
                <span>{dia.data}:</span> {dia.total_dia}
              </li>
            ))}
          </ul>
        </div>

        <div className="section-container">
          <h3 className="subtitle">Resumo Anual</h3>
          {Object.entries(data.resumo_anual).map(([ano, tarefas]) => (
            <div key={ano}>
              <h3>{ano}</h3>
              <ul className="stat-list">
                {Object.entries(tarefas).map(([tarefa, horas]) => (
                  <li className="stat-item" key={tarefa}>
                    <span>{tarefa}:</span> {horas.toFixed(2)} horas
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="section-container">
          <h3 className="subtitle">Resumo por Data</h3>
          {Object.entries(data.resumo_por_data).map(([data, tarefas]) => (
            <div key={data}>
              <h3>{data}</h3>
              <ul className="stat-list">
                {Object.entries(tarefas).map(([tarefa, horas]) =>
                  tarefa === "total_dia" ? (
                    <li className="stat-item" key={tarefa}>
                      <span>Total do dia:</span> {horas}
                    </li>
                  ) : (
                    <li className="stat-item" key={tarefa}>
                      <span>{tarefa}:</span> {horas}
                    </li>
                  )
                )}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Estatisticas;
