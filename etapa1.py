
def carregar_autores_prioritarios(caminho_arquivo="autores_prioritarios.csv"):

    autores = []
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome_autor = linha.strip()
            if nome_autor:
                autores.append(nome_autor)
    return autores

if __name__ == "__main__":
    lista_autores = carregar_autores_prioritarios()
    print("Autores Prioritários Carregados")
    for i, autor in enumerate(lista_autores, 1):
        print(f"{i}. {autor}")
