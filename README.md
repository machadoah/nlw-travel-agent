# NLW New Journey

## Descrição do Projeto :rocket:

Este projeto é uma aplicação Python desenvolvida para integrar-se com o modelo GPT da OpenAI, utilizando o framework Langchain. A aplicação inclui a criação de um banco vetorial com ChromaDB, e agentes especializados para consumo de dados do DuckDuckGo e Wikipedia, além de um agente supervisor. Toda a aplicação é containerizada em uma imagem Docker e pode ser implantada na AWS usando ECR, EC2 e Lambda function.

## Stack

- **[Langchain :parrot::link:](https://www.langchain.com/)**
- **[Chroma DB](https://www.trychroma.com/)**
- **[Python :snake:](https://www.python.org/)**
- **[OpenAI](https://openai.com/)**

## Agentes de IA :robot:

- **Agente DuckDuckGo**: Coleta dados da web através do DuckDuckGo.
- **Agente Wikipedia**: Coleta dados da Wikipedia.
- **Agente Supervisor**: Supervisiona as operações dos outros agentes para garantir eficiência e precisão.

## ReAct

- Utiliza o framework [ReAct](https://react-lm.github.io/) para interação e tomada de decisão baseada em lógica reativa.

## Estrutura do Projeto :file_folder:

```plaintext
NLW-travel-agent/
│
├── tools/
│   └── prompts.py
├── .env
│
├── .env-sample
│
├── .gitignore
│
├── chat_comp.py
│
├── Dockerfile
│
├── poetry.lock
│
├── pyproject.toml
│
├── README.md
│
└── travel_agent.py
```

## Pré-requisitos :gear:

- Python 3.12
- AWS CLI configurado
- Poetry para gerenciamento de dependências
- Pyenv
- OpenAI Key

## Instalação :computer:

1. **Clone o repositório:**
    ```sh
    gh repo clone machadoah/nlw-travel-agent
    cd nlw-travel-agent
    ```

2. **Instale as dependências:**
    ```sh
    poetry install
    ```
