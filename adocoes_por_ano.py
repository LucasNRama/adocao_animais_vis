import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

# Dados estimados de adoções por ano
df_adocoes = pd.DataFrame({
    'Ano': list(range(2015, 2025)),
    'Adoções': [350000, 360000, 370000, 380000, 390000, 400000, 410000, 420000, 580000, 650000]
})

# Inicialização da aplicação
app = dash.Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'])

app.layout = html.Div(className='container', children=[
    html.H1('Adoções de Animais no Brasil (2015-2024)', className='my-4 text-center'),

    html.Div(className='mb-4', children=[
        dcc.Slider(
            id='ano-slider',
            min=df_adocoes['Ano'].min(),
            max=df_adocoes['Ano'].max(),
            value=df_adocoes['Ano'].max(),
            marks={str(ano): str(ano) for ano in df_adocoes['Ano']},
            step=None
        ),
    ]),

    dcc.Graph(id='grafico-linha', className='shadow p-3 mb-5 bg-body rounded')
])

@app.callback(
    Output('grafico-linha', 'figure'),
    Input('ano-slider', 'value')
)
def update_figure(selected_year):
    filtered_df = df_adocoes[df_adocoes['Ano'] <= selected_year]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=filtered_df['Ano'],
        y=filtered_df['Adoções'],
        mode='lines+markers',
        line=dict(color='royalblue', width=3),
        marker=dict(size=8, color='darkblue'),
        name='Adoções'
    ))

    fig.update_layout(
        title='Evolução das Adoções de Animais por Ano',
        xaxis_title='Ano',
        yaxis_title='Número de Adoções',
        template='plotly_white',
        margin=dict(l=40, r=40, t=60, b=40),
        height=500
    )

    fig.update_xaxes(tickmode='linear', dtick=1)
    fig.update_yaxes(tickformat=',', ticksuffix='')

    return fig

if __name__ == '__main__':
    app.run(debug=True)
