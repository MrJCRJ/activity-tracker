# Activity Tracker

**Activity Tracker** é uma aplicação simples baseada em terminal para organizar e monitorar atividades ao longo do tempo. A ferramenta permite adicionar, editar, excluir e exibir atividades, exibindo-as de forma ordenada por data e hora. Além disso, oferece estatísticas sobre o tempo gasto em diferentes tarefas para ajudar no acompanhamento e análise de produtividade.

## Funcionalidades

- **Adicionar atividades**: Registre atividades com data, hora de início e fim e uma descrição.
- **Exibir atividades ordenadas**: Visualize suas atividades organizadas em ordem cronológica.
- **Filtrar por data**: Exiba apenas atividades de uma data específica.
- **Editar e excluir atividades**: Faça alterações ou remova atividades já registradas.
- **Estatísticas por tarefas**: Visualize o tempo total gasto em cada tarefa por data.
- **Exportar dados (futuro)**: Planejado para incluir funcionalidade de exportação para análise externa.

### Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/MrJCRJ/activity-tracker.git
   ```

2. Acesse o Diretório do Projeto:

   ```bash
   cd activity-tracker
   ```

3. Instale as dependências (se necessário):

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o programa:

   ```bash
   python main.py
   ```

### Estrutura do Projeto

A estrutura do código foi projetada para garantir clareza e modularidade, facilitando futuras melhorias e manutenção.

- **`main.py`**: Arquivo principal que gerencia o fluxo do programa e conecta todas as funcionalidades.
- **`storage.py`**: Responsável pelo armazenamento e recuperação de dados no formato JSON.
- **`actions.py`**: Contém as funções principais para adicionar, editar, excluir e exibir atividades.
- **`utils.py`**: Inclui funções auxiliares, como validação de datas/horas, ordenação e cálculos.
- **`requirements.txt`**: Lista de dependências do projeto, se aplicável.

---

### Funcionalidades em Detalhes

#### Registro de Atividades

- Permite registrar atividades com data, hora de início, hora de fim e descrição.

#### Exibição de Atividades

- **Ordenação cronológica**: Todas as atividades são exibidas por ordem de data e hora.
- **Filtro por data**: Exiba apenas as atividades de uma data específica para um acompanhamento mais detalhado.

#### Estatísticas

- **Por tarefas**: Saiba quanto tempo foi gasto em cada tarefa em determinado dia, com totalizações automáticas.
- **Resumo por dia**: Visualize um panorama do seu tempo gasto por data.

---

### Contribuição

Contribuições são sempre bem-vindas! Se você quiser ajudar a melhorar o **Activity Tracker**, siga estas etapas:

1. Faça um fork do repositório.
2. Crie um branch para suas alterações:
   ```bash
   git checkout -b minha-melhoria
   ```
3. Implemente suas alterações e faça commits claros e descritivos.
4. Envie um Pull Request com uma descrição detalhada do que foi alterado.

Para mais informações sobre como contribuir, consulte o Guia de Contribuição do GitHub.

---

### Exemplos de Uso

#### Registro de Atividades

```bash
Data (formato: AAAA-MM-DD): 2025-01-08
Hora de início (formato: HH:MM): 08:00
Hora de fim (formato: HH:MM): 09:00
Descrição da atividade: Estudar Python

```

#### Exibição de Atividades

```bash
=== Atividades Registradas ===
1. 2025-01-08 | 08:00 - 09:00 | Estudar Python
2. 2025-01-08 | 09:30 - 11:00 | Estudar Python
3. 2025-01-09 | 10:00 - 11:30 | Estudar JavaScript

```

#### Estatísticas por Tarefa

```bash
=== Estatísticas por Data ===

Data: 2025-01-08
Total de horas: 3.50
- Estudar Python: 3.50 horas

Data: 2025-01-09
Total de horas: 1.50
- Estudar JavaScript: 1.50 horas

```

---

### Licença

Este projeto está licenciado sob a MIT License. Sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo.
