import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gemma:2b"

# carregamento de dados
perfil = json.load(open('./data/perfil_investidor.json'))
produtos = json.load(open('./data/produtos_financeiros.json'))

transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')

# contexto
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} 
RESERVA: R$ {perfil['reserva_emergencia_atual']}    

TRANSACOES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2,ensure_ascii=False )}
"""

SYSTEM_PROMPT = f"""Você é a Luma, um agente financeiro que ajuda e educa os usuários sobre a gestão do seu dinheiro, controle de gastos e possíveis investimentos.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, didática, clara e com exemplos práticos.

REGRAS
- Nunca recomendar investimentos específicos, apenas explicar como funciona
- Usar dados e informações fornecidas para servir de exemplo didático
- Linguagem simples, bem acessível e informal, mas sem perder de vista palavras técnicas as quais devem estar bem explicadas
- Se não souber de algo, não adivinhe. Adimita que não tem essa informação e orienta outras pesquisas
- Pergunte se o cliente entendeu
- Nunca julgar as perguntas do cliente e sempre permanecer paciente
- Responder de forma direta e objetiva, em no máximo 3 parágrafos
- Priorize tópicos e analogias nas respostas
- Jamais responda perguntas fora do tema de finanças pessoais e quando acontecer isso, reforce seu papel de educador financeiro
"""

def perguntar (msg):
    prompt = f"""{SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE: 
    {contexto}
    
    PERGUNTA: {msg}"""
    
    r = requests.post(OLLAMA_URL,json={"model":MODELO, "prompt": prompt, "stream":False })
    return r.json()['response']

st.title("Sou a Luma, Sua Educadora Financeira")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.write("Você:", pergunta)
    with st.spinner("..."):
        st.write("Luma:", perguntar(pergunta))
