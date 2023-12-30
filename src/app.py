import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from flask import request

from main import main_

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Text Similarity Calculator"),
    html.Div([
        html.Label("Text 1 "),
        dcc.Input(id='text1-input', type='text', value=''),
    ], style={'margin-bottom': '10px'}),
    
    html.Div([
        html.Label("Text 2 "),
        dcc.Input(id='text2-input', type='text', value=''),
    ], style={'margin-bottom': '10px'}), 
    
    html.Div([
        html.Button('Calculate Similarity', id='calculate-button'),
        html.Div(id='store-clicks', style={'display': 'none'}), 
    ], style={'margin-bottom': '10px'}),  
    
    html.Div(id='output-similarity')
])

@app.callback(
    Output('store-clicks', 'children'),
    [Input('calculate-button', 'n_clicks')]
)
def store_click_count(n_clicks):
    return n_clicks

@app.callback(
    Output('output-similarity', 'children'),
    [Input('store-clicks', 'children')],
    [State('text1-input', 'value'),
     State('text2-input', 'value')]
)
def calculate_similarity(n_clicks, text1, text2):
    if n_clicks is not None and n_clicks > 0:
        score = main_(text1, text2)
        return f"Similarity Score: {score}"
    else:
        return ''
    
@app.server.route('/api', methods=['POST', 'GET'])
def handle_api():
    if request.method == 'POST':
        data = request.json 
        text1 = data.get('text1', '')
        text2 = data.get('text2', '')
        score = main_(text1, text2)
        return {'similarity_score': score}
    
    elif request.method == 'GET':
        text1 = request.args.get('text1', '')
        text2 = request.args.get('text2', '')
        score = main_(text1, text2)
        return {'similarity_score': score}

if __name__ == '__main__':
    server.run(debug=False)
