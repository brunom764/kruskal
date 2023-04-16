from interface import interface
from route import route
# Parte principal

if __name__ == "__main__":
    # Abrir a base de dados
    with open('jazzNew.net') as f:
        lines = f.readlines()

    # guardar numero de vertices
    _, nodes = lines[0].split()

    # receber o valor do menor caminho
    mst = route(nodes,lines)

    # output
    sumKm = 0
    for edge in mst:
        print(f'Pedro se deslocou da loja {edge[0]} até a loja {edge[1]} e percorreu {edge[2]}km.')
        sumKm += int(edge[2])
    print('-------- FIM DO PERCURSO --------')
    print(f'Pedro percorreu {sumKm}km.')
    print()

    # interface
    itf = input("Você deseja ver o percuso graficamente? Se sim, digite 'SIM': ").upper()
    if itf == "SIM":
        interface()