# Função para modificar os pesos da base de dados,
# pois todos estão com peso 1, agora será gerado
# um peso de numero aleatório entre 1 e 184 e será
# armazenado essa alteração no arquivo jazzNew.net

import random

with open('jazz.net') as f:   # abrir arquivo original
    lines = f.readlines()

_, nodes = lines[0].split()  # guardar numero de vertices

with open('jazzNew.net', 'w') as f:
    f.write(f"*5484 {nodes}\n")  # escreve o cabeçalho do arquivo
    for line in lines:
        if line.startswith('*'):
            continue
        src, desc, _ = line.rstrip().split()   # Guarda as variaveis
        weight = random.randint(1,184)
        temp = [src, desc, str(weight)]
        f.write(" ".join(temp) + "\n")

