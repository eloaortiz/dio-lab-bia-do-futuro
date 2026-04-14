# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Funcionalidade para a Luma |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, atendendo de forma mais eficiente |
| `perfil_investidor.json` | JSON | Personalizar explicações sobre dúvidas e necessidades de aprendizado do cliente |
| `produtos_financeiros.json` | JSON | Conhecer produtos disponíveis para ser explicados ao cliente de forma adequada ao perfil|
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente para servir de exemplo e usar de forma didática |



---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O produto "Fundo Imobiliário" substituiu o "Fundo Multimercado" em razão da minha maior familiaridade com FIIs. Assim, poderei estar mais consciente das repostas da Luma, garantido maior confiança na validação das respostas. 

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

```python

import pandas
import json

# para arquivos CSVs
historico = pandas.read_csv('data/historico_atendimento.csv')
transacoes = pandas.read_csv('data/transacoes.csv')

# para arquivos JSON
with open('data/perfil_investidor.json','r', encoding ='utf-8') as f:
  perfil = json.load(f)

with open('data/produtos_financeiros.json','r', encoding ='utf-8') as f:
  produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
