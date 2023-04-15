from route import route
from interface import interface
# Parte principal

if __name__ == "__main__":
    # Abrir a base de dados
    with open('jazzNew.net') as f:
        lines = f.readlines()

    # guardar numero de vertices
    _, nodes = lines[0].split()

    route(nodes,lines)
    itf = input("Você deseja ver o percuso graficamente? Se sim, digite 'SIM': ").upper()
    if itf == "SIM":
        interface()