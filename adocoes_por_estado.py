import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Base de dados com região e sigla dos estados
df_estados = pd.DataFrame({
    'Estado': ['SP', 'RJ', 'MG', 'ES', 'BA', 'PE', 'CE', 'RN', 'PB', 'SE', 'AL', 'PI', 'MA', 'RS', 'SC', 'PR', 'GO', 'MT', 'MS', 'DF', 'TO', 'PA', 'AM', 'RO', 'AC', 'RR', 'AP'],
    'UF': ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo', 'Bahia', 'Pernambuco', 'Ceará', 'Rio Grande do Norte', 'Paraíba', 'Sergipe', 'Alagoas', 'Piauí', 'Maranhão',
           'Rio Grande do Sul', 'Santa Catarina', 'Paraná', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul', 'Distrito Federal', 'Tocantins', 'Pará', 'Amazonas', 'Rondônia', 'Acre', 'Roraima', 'Amapá'],
    'Região': ['Sudeste', 'Sudeste', 'Sudeste', 'Sudeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste',
               'Sul', 'Sul', 'Sul', 'Centro-Oeste', 'Centro-Oeste', 'Centro-Oeste', 'Centro-Oeste', 'Norte', 'Norte', 'Norte', 'Norte', 'Norte', 'Norte', 'Norte'],
    'Adoções': [120000, 80000, 90000, 40000, 70000, 60000, 65000, 30000, 25000, 20000, 22000, 18000, 17000,
                50000, 45000, 47000, 40000, 35000, 30000, 25000, 15000, 20000, 18000, 12000, 8000, 5000, 4000]
})

# Inicialização do app com Bootstrap
app = dash.Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'])

app.layout = html.Div(className="container", children=[
    html.H1('Adoções de Animais por Estado', className='my-4'),

    html.Div([
        html.Label('Filtrar por Região:', className='form-label'),
        dcc.Dropdown(
            id='filtro-regiao',
            options=[{'label': regiao, 'value': regiao} for regiao in sorted(df_estados['Região'].unique())] +
                    [{'label': 'Todas as regiões', 'value': 'Todas'}],
            value='Todas',
            className='form-select'
        )
    ], className='mb-4'),

    dcc.Graph(id='grafico-mapa')
])

@app.callback(
    Output('grafico-mapa', 'figure'),
    Input('filtro-regiao', 'value')
)
def atualizar_mapa(regiao):
    if regiao == 'Todas':
        df_filtrado = df_estados
    else:
        df_filtrado = df_estados[df_estados['Região'] == regiao]

    fig = px.choropleth(
        df_filtrado,
        locations='Estado',
        locationmode='geojson-id',
        geojson="https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson",
        featureidkey="properties.sigla",
        color='Adoções',
        hover_name='UF',
        color_continuous_scale='YlGn',
        title=f"Adoções por Estado - {regiao if regiao != 'Todas' else 'Brasil'}"
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
    return fig

if __name__ == '__main__':
    app.run(debug=True)
