import random


with open('jazz.net') as f:
    lines = f.readlines()

# guardar numero de vertices
_, nodes = lines[0].split()

# Criar grafo
graph = {}
for line in lines:
    if line.startswith('*') or not line.strip(): # verifica se a linha está vazia ou começa com *
        continue

    values = line.rstrip().split()
    if len(values) < 3: # verifica se a linha contém pelo menos 3 valores
        continue

    src, desc, weight = values
    weight = random.randint(1,184)
    graph.setdefault(src, {})[desc] = weight


with open('jazz.net', 'w') as f:
    f.write(f"*{len(graph)} {nodes}\n")  # escreve o cabeçalho do arquivo
    for line in lines:
        if line.startswith('*'):
            continue
        src, desc, weight = line.rstrip().split()
        weight = random.randint(1,184)
        temp = [src, desc, str(weight)]
        f.write(" ".join(temp) + "\n")
