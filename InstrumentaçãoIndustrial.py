import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import dash
from dash import dcc
from dash import html

# carrega os dados
dados = {'Vazão (m³/h)': [1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],
         'Pressão TQ2 (psi)': [9, 9, 13, 18, 23, 27, 31, 37, 39, 43, 45, 47, 49, 51, 52],
         'Pressão Bomba (psi)': [38, 38, 39, 40, 42, 42, 45, 46, 48, 50, 51, 51, 51, 53, 53],
         'Variação tempo (Segundos)': [50, 23, 15, 11, 6, 7, 9, 5, 4, 4, 5, 4, 4, 13, 12]}

df = pd.DataFrame(dados)

# cria o gráfico de vazão x tempo
fig1 = px.line(df, x='Variação tempo (Segundos)', y='Vazão (m³/h)', title='Vazão x Tempo')

# cria o gráfico de pressão da bomba x tempo
fig2 = px.line(df, x='Variação tempo (Segundos)', y='Pressão Bomba (psi)', title='Pressão Bomba x Tempo')

# cria o gráfico de pressão do tanque x tempo
fig3 = px.line(df, x='Variação tempo (Segundos)', y='Pressão TQ2 (psi)', title='Pressão TQ x Tempo')

# cria o gráfico de pressão da bomba x pressão do tanque x vazão
fig4 = go.Figure()

fig4.add_trace(go.Scatter3d(x=df['Pressão Bomba (psi)'], 
                             y=df['Pressão TQ2 (psi)'], 
                             z=df['Vazão (m³/h)'],
                             mode='markers',
                             marker=dict(
                                 size=5,
                                 color=df['Variação tempo (Segundos)'],
                                 colorscale='Viridis',
                                 opacity=0.8
                             )
                            ))

fig4.update_layout(scene=dict(
    xaxis_title='Pressão Bomba (psi)',
    yaxis_title='Pressão TQ (psi)',
    zaxis_title='Vazão (m³/h)'),
    margin=dict(l=0, r=0, t=0, b=0)
)

# cria a página HTML
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Dashboard de Instrumentação Industrial'),

    html.Div(children='''
        Análise de dados de vazão e pressão
    '''),

    dcc.Graph(
        id='grafico-vazao-tempo',
        figure=fig1
    ),

    dcc.Graph(
        id='grafico-pressao-bomba-tempo',
        figure=fig2
    ),

    dcc.Graph(
        id='grafico-pressao-tanque-tempo',
        figure=fig3
    ),

    dcc.Graph(
        id='grafico-pressao-tanque-bomba-vazao',
        figure=fig4
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
