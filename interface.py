import networkx as nx
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from route import route


def criarGrafo(grafo):
    df = {'origem': [], 'destino': [], 'peso': []}

    # transforma a lista de tuplas mst em dicionário com chaves from (vértice de partida), to(vértice de destino) e peso
    for i in range(len(grafo)):
        df['origem'].append(grafo[i][0])
        df['destino'].append(grafo[i][1])
        df['peso'].append(grafo[i][2])

    # constroi o grafo
    Grafo = nx.from_pandas_edgelist(df, 'origem', 'destino')
    nx.draw(Grafo, with_labels=True, node_size=0.6, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=10)
    plt.grid(True)
    return plt.gcf()


def drawFigure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def interface():
    layout = [[sg.Titlebar('Algoritmo de Kruskal')],
              [sg.Button('Adicionar base de dados percurso de Pedro', key='ADDROUTE', enable_events=True)],
              [sg.Text('Escolha um outro arquivo com a base de dados ou escreva manualmente')],
              [sg.Text('Choose a file: ', enable_events=True), sg.FileBrowse(key='browse', ),
              sg.Button('Adicionar base de dados', key='ADDBASE', enable_events=True)],
              [sg.Text('Digite o número de vértices'), sg.Input(key='-VER-'),
               sg.Button('Adicionar número de vértices', key='add', enable_events=True)],
              [sg.Text('Digite a primeira vértice, a segunda vértice e o peso da aresta'), sg.Input(key='-ARE-'),
               sg.Button('Adicionar aresta', key='OK', enable_events=True)],
              [sg.Button('Gerar caminho de menor custo', key='-OK-', enable_events=True)],
              [sg.Canvas(size=(1000, 1000), key='-CANVAS-')],
              ]
    sg.theme('DarkTeal')
    print = sg.Print
    window = sg.Window('Kruskal Algoritmo - Visualização', layout, location=(0, 0), size=(800, 600), keep_on_top=True,
                       resizable=True).Finalize()

    lines = []
    fim = False
    while True:
        event, values = window.read()
        if event == 'ADDBASE':
            # Abrir a base de dados
            path = values['browse']
            with open(path) as f:
                lines = f.readlines()

            # guardar numero de vertices
            _, nodes = lines[0].split()

        elif event == 'ADDROUTE':
            # Abrir a base de dados
            path = 'jazzNew.net'
            with open(path) as f:
                lines = f.readlines()

            # guardar numero de vertices
            _, nodes = lines[0].split()

        elif event == 'OK':

            lines.append(str(values['-ARE-']))

        elif event == '-OK-':

            mst = route(nodes, lines)

            drawFigure(window['-CANVAS-'].TKCanvas, criarGrafo(mst))

        elif event == 'add':

            nodes = values['-VER-']

        elif event == sg.WIN_CLOSED:
            break

    window.close()