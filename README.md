# Activity Tracker

**Activity Tracker** é uma aplicação simples baseada em terminal para organizar e monitorar atividades ao longo do tempo. A ferramenta permite adicionar, editar, excluir e exibir atividades, exibindo-as de forma ordenada por data e hora.

## Funcionalidades

- Adicionar atividades com data e hora de início e fim.
- Exibir atividades em ordem cronológica.
- Editar ou excluir atividades registradas.
- Exportar os dados para análise futura (planejado para próximas versões).

## Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/MrJCRJ/activity-tracker.git
   ```

2. Acesse o diretório do projeto:

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

## Estrutura do Projeto

- main.py: Arquivo principal que conecta todas as funcionalidades.
- storage.py: Responsável pelo armazenamento e recuperação de dados.
- actions.py: Contém as funções principais para adicionar, editar, excluir e exibir atividades.
- utils.py: Funções auxiliares, como ordenação e validação de dados.

## Contribuição

Contribuições são bem-vindas! Para colaborar, siga os passos:

1. Faça um fork do repositório.
2. Crie um branch para suas alterações:

```bash
git checkout -b minha-melhoria
```

3. Envie um Pull Request.

## Licença

Este projeto está licenciado sob a MIT License.
