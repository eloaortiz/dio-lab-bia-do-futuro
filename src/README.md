# Passo a passo da Execução

Esta pasta contém o código do seu agente financeiro.

## Setup do Ollama

> 1. Instalar o Ollama
> 2. Baixar um modelo leve (utilizei gemma:2b)
> 3. Testar se funciona

## Código Fonte

Todo o código fonte está no arquivo `app.py`

## Como Rodar

```bash
# Instalar dependências
pip install streamlit pandas requests

# Garantir que o Ollama está funcionando e onde está no computador
ollama serve

# Rodar a aplicação
python -m streamlit run .\src\app.py
```
