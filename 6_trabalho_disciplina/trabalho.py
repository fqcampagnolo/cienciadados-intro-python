# A partir da base de dados de glicemia 'suja', ou sem tratamento, construir um programa em Python que:
# 1) leia linha por linha do arquivo
# 2) extraia as colunas das linhas separadas por ;
# 3) armazene os dados em um objeto chamado glicemia (destacando os atributos até os dados dos esportes)
# 4) armazene os objetos numa lista de glicemia
# 5) realize a média de glicemia, kcal, carb.
# 6) realize a mediana de glicemia, kcal, carb. (Dica. Ordenar a lista)
# 7) realize a moda de glicemida, kcal, carb (Moda é o valor que mais repete)


from glicemia import Glicemia


def calcular_media(lista_glicemias, atributo):
    media = 0
    tamanho_lista_glicemias = len(lista_glicemias)

    if tamanho_lista_glicemias == 0:
        return 0  
    
    for obj in lista_glicemias:
        media += getattr(obj, atributo, 0)  

    return media / tamanho_lista_glicemias


def calcular_mediana(lista_glicemias, atributo):
    tamanho_lista_glicemias = len(lista_glicemias)

    lista_glicemias_ordenada = sorted(lista_glicemias, key=lambda glicemia: getattr(glicemia, atributo, None))

    mediana = 0
    if tamanho_lista_glicemias % 2 == 1:
        mediana_obj = lista_glicemias_ordenada[int(tamanho_lista_glicemias/2)]
        mediana = getattr(mediana_obj, atributo, None)
    else:
        mediana_obj_1 = lista_glicemias_ordenada[int(tamanho_lista_glicemias/2)]
        mediana_obj_2 = lista_glicemias_ordenada[int(tamanho_lista_glicemias/2) + 1]
        mediana = (getattr(mediana_obj_1, atributo, None) + getattr(mediana_obj_2, atributo, None)) / 2

    return mediana


def calcular_moda(lista_glicemias, atributo):
    lista_moda = []
    qtd_moda = 0
    
    for item in lista_glicemias:
        ocorrencias = 0
        for outro_item in lista_glicemias:
            if (getattr(item, atributo, None) == getattr(outro_item, atributo, None)):
                ocorrencias += 1

        if ocorrencias == qtd_moda:
            if getattr(item, atributo, None) not in lista_moda:
                lista_moda.append(getattr(item, atributo, None))
        elif ocorrencias > qtd_moda:
            lista_moda = [getattr(item, atributo, None)]
            qtd_moda = ocorrencias

    return qtd_moda, lista_moda



nome_arquivo = "glicose_data_suja.csv"
lista_glicemias = []
with open(nome_arquivo,"r",encoding="utf8") as leitor:
    # i = 0
    # 1) leia linha por linha do arquivo
    for linha in leitor:
    # 2) extraia as colunas das linhas separadas por ;
        vetor_linha = linha.split(";")
        #[Quinta,2012,ac,90,6,2037,246,4]
        # print(f">>> {i}")
        # i += 1
        
    # 3) armazene os dados em um objeto chamado glicemia (destacando os atributos até os dados dos esportes)
        obj = Glicemia(vetor_linha[0],vetor_linha[1],vetor_linha[3],vetor_linha[4],vetor_linha[5],vetor_linha[6],vetor_linha[7])
    # 4) armazene os objetos numa lista de glicemia
        lista_glicemias.append(obj)


    # 5) realize a média de glicemia, kcal, carb.
    print(f"Média Glicemia: {calcular_media(lista_glicemias, 'valor_glicemia')}")
    print(f"Média Kcal: {calcular_media(lista_glicemias, 'kcal')}")
    print(f"Média Carboidrato: {calcular_media(lista_glicemias, 'carb')}\n")

    # 6) realize a mediana de glicemia, kcal, carb. (Dica. Ordenar a lista)
    print(f"Mediana Glicemia: {calcular_mediana(lista_glicemias, 'valor_glicemia')}")
    print(f"Mediana Kcal: {calcular_mediana(lista_glicemias, 'kcal')}")
    print(f"Mediana Carboidrato: {calcular_mediana(lista_glicemias, 'carb')}\n")
    
    # 7) realize a moda de glicemida, kcal, carb (Moda é o valor que mais repete)
    qtd, moda = calcular_moda(lista_glicemias, 'valor_glicemia')
    print(f"Moda Glicemia, o valor {moda} apareceu {qtd} vezes.")
    
    qtd, moda = calcular_moda(lista_glicemias, 'kcal')
    print(f"Moda Kcal, o valor {moda} apareceu {qtd} vezes.")

    qtd, moda = calcular_moda(lista_glicemias, 'carb')
    print(f"Moda Carboidrato, o valor {moda} apareceu {qtd} vezes.")
    


