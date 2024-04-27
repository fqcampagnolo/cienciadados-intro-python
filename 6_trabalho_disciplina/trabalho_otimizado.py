# A partir da base de dados de glicemia 'suja', ou sem tratamento, construir um programa em Python que:
# 1) leia linha por linha do arquivo
# 2) extraia as colunas das linhas separadas por ;
# 3) armazene os dados em um objeto chamado glicemia (destacando os atributos até os dados dos esportes)
# 4) armazene os objetos numa lista de glicemia
# 5) realize a média de glicemia, kcal, carb.
# 6) realize a mediana de glicemia, kcal, carb. (Dica. Ordenar a lista)
# 7) realize a moda de glicemida, kcal, carb (Moda é o valor que mais repete)


from glicemia import Glicemia
from collections import Counter
import numpy as np


def calcular_moda_all(data):
    if not data:  # Verifica se a lista está vazia
        return []
    
    # Conta a frequência de cada elemento no conjunto de dados
    counter = Counter(data)
    # Encontra a maior frequência
    max_freq = max(counter.values())
    # Encontra todos os elementos que têm essa frequência máxima
    modes = [key for key, count in counter.items() if count == max_freq]
    
    return modes, max_freq


nome_arquivo = "glicose_data_suja.csv"
lista_glicemias = []
with open(nome_arquivo,"r",encoding="utf8") as leitor:

    # 1) leia linha por linha do arquivo
    for i, linha in enumerate(leitor):
    # 2) extraia as colunas das linhas separadas por ;
        vetor_linha = linha.replace('\n', '').split(";")
        vetor_linha.pop(2)
        vetor_linha = vetor_linha[:7]

    # 3) armazene os dados em um objeto chamado glicemia (destacando os atributos até os dados dos esportes)
        obj = Glicemia(*vetor_linha)
    # 4) armazene os objetos numa lista de glicemia
        lista_glicemias.append(obj)

    # transforma lista dos objetos em lista de valores
    glicemia_values = [glic.valor_glicemia for glic in lista_glicemias]
    kcal_values = [glic.kcal for glic in lista_glicemias]
    carb_values = [glic.carb for glic in lista_glicemias]

    # 5) realize a média de glicemia, kcal, carb.
    print(f"Média Glicemia: {np.mean(glicemia_values)}")
    print(f"Média Kcal: {np.mean(kcal_values)}")
    print(f"Média Carboidrato: {np.mean(carb_values)}\n")

    # 6) realize a mediana de glicemia, kcal, carb. (Dica. Ordenar a lista)
    print(f"Mediana Glicemia: {np.median(glicemia_values)}")
    print(f"Mediana Kcal: {np.median(kcal_values)}")
    print(f"Mediana Carboidrato: {np.median(carb_values)}\n")
    
    # 7) realize a moda de glicemida, kcal, carb (Moda é o valor que mais repete)
    print(f"Moda Glicemia: {calcular_moda_all(glicemia_values)}")
    print(f"Moda Kcal: {calcular_moda_all(kcal_values)}")
    print(f"Moda Carboidrato: {calcular_moda_all(carb_values)}\n")


