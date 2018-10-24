from os import listdir
from os.path import isfile, join
import os as osfnc

#%% Descobrir o nome de todas as imagens da base

# Para isso é necessário descobrir o diretório atual
# Em seguida apontar a pasta da base de imagens
# Descobrir o nome de todos os arquivos da pasta
# Filtrar apenas aqueles que são imagens e adicionar
# Na lista de imagens

# Descobrir o diretório atual
mypath = osfnc.getcwd()
# apontar a pasta que as minhas imagens estão
dirEntrada = mypath + '\\Entrada'
dirSaida = mypath + '\\Saida'
# Criar uma lista de imagens
soimagens = []
# Iterar cada um dos arquivos dentro de mypath
for f in listdir(dirEntrada):
    #Calcular o diretório completo do arquivo
    aa = join(dirEntrada, f)
    # verificar se é um arquivo ou não
    if isfile(aa):
        # Se for arquivo verificar se é .png
        if f.endswith(".png") or f.endswith(".jpg"):
            # Se for .png ou .jpg então adiciona na lista de imagens
            soimagens.append(f)

#%%

import cv2

for u, nome_das_imagens in enumerate(soimagens):

    img = cv2.imread(join(dirEntrada, nome_das_imagens),1)

    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] = clahe.apply(hsv[:, :, 2])
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imwrite(join(dirSaida, nome_das_imagens), img)



