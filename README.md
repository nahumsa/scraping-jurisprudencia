<h1 align="center">Scraping de Jurisprudência do TJPR</h1>
<p align="center">
<a href="https://github.com/nahumsa/scraping-jurisprudencia/actions"><img alt="Actions Status" src="https://github.com/nahumsa/scraping-jurisprudencia/workflows/scraping-jurisprudencia/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://pycqa.github.io/isort/"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
<a href="https://github.com/PyCQA/pylint"><img alt="pylint" src="https://img.shields.io/badge/linting-pylint-yellowgreen"></a>
</p>


# Tabela de conteúdo <!-- omit in toc -->

- [Introdução](#introdução)
- [Requisitos](#requisitos)
- [Rodando o projeto](#rodando-o-projeto)
  - [Utilizando Makefile](#utilizando-makefile)
  - [Utilizando comandos](#utilizando-comandos)
- [TODO](#todo)


# Introdução

Esse repositório consiste em criar um script em python para coletar dados de jurisprudência e decisões do Tribunal Jurídico do estado do Paraná (TJPR).

Esses cálculos são muito importantes para fazer jurimetria, que consiste em aplicar conceitos de estatística para o Direito.

# Requisitos

- Python 3.10
- instalar pipenv (`pip install pipenv`)


# Rodando o projeto

Para instalar as bibliotecas é necessário instalar o [`pipenv`](https://pipenv.pypa.io/en/latest/), se tiver python 3.10 no seu computador, basta rodar `pip install pipenv`.

Após a instalação do pipenv, tem duas opções para rodar o projeto: [utilizando Makefile](#utilizando-makefile) e [utilizando os comandos](#utilizando-comandos).

## Utilizando Makefile

Para instalar os pacotes basta rodar:

```bash
make setup
```

Isso vai adicionar todos os pacotes necessários para desenvolvimento.

Após isso basta rodar o comando:

```bash
make run_scraper
```

Se o scrape da página for sucedido vai gerar um csv na pasta `data` com os dados obtidos através do scrape. Caso não seja sucedido (pode ocorrer de que encontre um erro 502), ele gera um `execution_error.json`.

## Utilizando comandos
Para instalar os pacotes basta rodar:

```bash
pipenv install --dev
```

Isso vai adicionar todos os pacotes necessários para desenvolvimento.

Após isso basta rodar o comando:

```bash
pipenv run python src/scrape.py
```

Se o scrape da página for sucedido vai gerar um csv na pasta `data` com os dados obtidos através do scrape. Caso não seja sucedido (pode ocorrer de que encontre um erro 502), ele gera um `execution_error.json`.

# TODO

Tipos de decisões cobertos:

- [X] Decisão monocrática
- [ ] Acórdão
- [ ] Dúvida/exame de competência