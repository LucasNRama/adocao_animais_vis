# 🐶📊 Adoção de Animais no Brasil — Dashboard Interativo

Este projeto apresenta um dashboard interativo, desenvolvido com **Dash (Plotly)**, para **visualizar a evolução, distribuição e desafios da adoção de animais de estimação no Brasil** entre 2015 e 2024.

## 🎯 Objetivo

Fornecer uma narrativa visual clara e interativa que:

- Mostre a tendência histórica de adoções no país;
- Destaque desigualdades regionais;
- Evidencie o gargalo entre resgates e adoções por ONGs.

## 📈 Visualizações

1. **Gráfico de Linha Temporal**  
   - Adoções por ano (2015 a 2024)  
   - Destaque para o crescimento no período da pandemia.

2. **Mapa Interativo por Estado (UF)**  
   - Volume de adoções por estado com detalhamento via clique.  
   - Exposição de desigualdades regionais.

3. **Gráfico de Barras Comparativo**  
   - Resgatados vs. Adotados por ano com slider dinâmico.  
   - Mostra o gap entre capacidade de resgate e adoção.

## 📊 Fontes de Dados

- [Instituto Pet Brasil](https://www.institutopetbrasil.com/)  
- [IBGE - Censo Pet](https://www.ibge.gov.br)  
- ONGs como AMPARA Animal, SUIPA, Gatil da Serra  
- Dados complementares de ANDA, G1, WAP

## 🛠️ Tecnologias Utilizadas

- **Dash (Plotly Dash)** – Visualização interativa
- **Plotly Express** – Gráficos avançados
- **Bootstrap 5** – Estilização
- **Pandas** – Processamento de dados
- **Callbacks Reativos** – Interação entre componentes

## 🚀 Como Executar

```bash
# Instale as dependências
pip install dash pandas plotly

# Rode o aplicativo
python app.py