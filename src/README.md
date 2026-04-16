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
## Exemplo de Execução 
<img width="1127" height="865" alt="image" src="https://github.com/user-attachments/assets/3876e62e-69f4-4ac2-b717-f038e940a943" />

