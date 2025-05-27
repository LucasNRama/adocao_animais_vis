import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Inicializa o app com Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Dados estimados
df_resgate_adocao = pd.DataFrame({
    'Ano': list(range(2015, 2025)),
    'Resgatados': [200000, 210000, 220000, 230000, 240000, 250000, 260000, 270000, 280000, 290000],
    'Adotados': [180000, 190000, 200000, 210000, 220000, 230000, 240000, 250000, 260000, 270000]
})

# Layout com estilo Bootstrap
app.layout = dbc.Container([
    html.H1('Resgates e Adoções de Animais por ONGs', className='my-4 text-center text-primary'),

    html.P('Use o seletor de ano para visualizar os dados acumulados até o ano escolhido:',
           className='text-muted text-center'),

    dcc.Slider(
        id='ano-slider',
        min=df_resgate_adocao['Ano'].min(),
        max=df_resgate_adocao['Ano'].max(),
        value=df_resgate_adocao['Ano'].max(),
        marks={str(ano): str(ano) for ano in df_resgate_adocao['Ano']},
        step=None,
        tooltip={"placement": "bottom", "always_visible": True}
    ),

    dcc.Graph(id='grafico-barras', className='mt-4')
], fluid=True)


# Callback interativo
@app.callback(
    Output('grafico-barras', 'figure'),
    Input('ano-slider', 'value')
)
def update_figure(selected_year):
    filtered_df = df_resgate_adocao[df_resgate_adocao['Ano'] <= selected_year]
    fig = px.bar(filtered_df, x='Ano', y=['Resgatados', 'Adotados'],
                 barmode='group',
                 title=f'Resgates vs. Adoções acumuladas até {selected_year}',
                 labels={'value': 'Quantidade de Animais', 'variable': 'Situação'},
                 color_discrete_map={
                     'Resgatados': '#E74C3C',
                     'Adotados': '#2ECC71'
                 })

    fig.update_layout(
        template='plotly_white',
        title_x=0.5,
        legend_title_text='Situação',
        hovermode='x unified',
        transition_duration=500
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
