# _studing-fastapi

Respositório com API de exemplo usando FastAPI no Python

## Setup

### Gerenciador de dependências
Esse projeto de exemplo usa [Pipenv](https://pipenv.pypa.io/en/latest/) como gerenciador de dependências. Você precisa ter o Pipenv instalado na sua máquina para rodar o projeto.

Para instalar o Pipenv, você pode usar o comando:

```bash
pip install --user pipenv
```

> [!IMPORTANT]
> Para informações detalhadas sobre como instalar e usar o Pipenv, consulte a [documentação oficial](https://pipenv.pypa.io/en/latest/).

### Instalando as dependências

Para instalar as dependências do projeto, você pode usar o comando:

```bash
pipenv sync
```

Esse comando instala todas as dependências do projeto, incluindo as dependências de desenvolvimento, declaradas no arquivo [`Pipfile`](Pipfile).

### Rodando o projeto

Para rodar o projeto no modo desenvolvimento, você pode usar o comando:

```bash
pipenv run dev
```

Esse comando inicia o servidor de desenvolvimento do FastAPI. Você pode acessar a documentação da API em `http://localhost:8000/docs`.

## Links de referência
- **FastAPI**: [_https://fastapi.tiangolo.com/_](https://fastapi.tiangolo.com/)
- **Pipenv**: [_https://pipenv.pypa.io/en/latest/_](https://pipenv.pypa.io/en/latest/)
- **Pydantic**: [_https://docs.pydantic.dev/latest/_](https://docs.pydantic.dev/latest/)