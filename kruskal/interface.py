import networkx as nx
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from kruskal import kruskal


# Parte principal

def test(nodes, lines):
    # Criar grafo
    grafo = {}
    for line in lines:
        if line.startswith('*'):
            continue
        orig, dest, peso = line.split()
        if orig not in grafo:
            grafo[orig] = {}
        if dest not in grafo:
            grafo[dest] = {}
        grafo[orig][dest] = peso
        grafo[dest][orig] = peso

    # Converter grafo em uma uma lista de vertices
    # (u, v, w) triples representam: vértice de partida `u` -> vértice de chegada `v` com peso `w`
    arestas = []
    for orig, neighbors in grafo.items():
        for dest, peso in neighbors.items():
            arestas.append((int(orig), int(dest), int(peso)))
    # Kruskal
    mst = kruskal(arestas, int(nodes))

    # Output
    sumKm = 0
    for edge in mst:
        print(f'Pedro se deslocou da loja {edge[0]} até a loja {edge[1]} e percorreu {edge[2]}km.')
        sumKm += int(edge[2])
    print('-------- FIM DO PERCURSO --------')
    print(f'Pedro percorreu {sumKm}km.')
    return mst


def CriarGrafo(grafo):
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


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


l0 = sg.Text('Escolha um arquivo com a base de dados ou escreva manualmente')
b5 = sg.Button('Adicionar base de dados', key='ADDBASE', enable_events=True)
l1 = sg.Text('Digite o número de vértices')
t2 = sg.Input(key='-VER-')
l2 = sg.Text('Digite a primeira vértice, a outra vértice que está ligada a primeira e o peso')
t1 = sg.Input(key='-ARE-')
b1 = sg.Button('Mostrar grafo', key='-OK-', enable_events=True)
b3 = sg.Button('Adicionar aresta', key='OK', enable_events=True)
b4 = sg.Button('Adicionar número de vértices', key='add', enable_events=True)
layout = [[l0], [sg.Text('Choose a file: ', enable_events=True), sg.FileBrowse(key='browse', )], [b5], [l1], [t2], [b4],
          [l2], [t1], [b3], [b1],
          [sg.Canvas(size=(1000, 1000), key='-CANVAS-')],
          ]
sg.theme("DarkTeal2")
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

    elif event == 'OK':

        lines.append(str(values['-ARE-']))

    elif event == '-OK-':

        mst = test(nodes, lines)

        draw_figure(window['-CANVAS-'].TKCanvas, CriarGrafo(mst))

    elif event == 'add':

        nodes = values['-VER-']

    elif event == sg.WIN_CLOSED:
        break

window.close()