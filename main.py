"""
Pipeline principal: Aqui as 4 etapas se conectam.
"""
import pandas as pd
from etapa1 import carregar_autores_prioritarios
from etapa2 import obter_cotacao_gbp_brl
from etapa3 import coletar_livros_categoria
from etapa4 import coletar_citacoes_autores

def executar_pipeline():
    print("PIPELINE DE COLETA DE DADOS: CLÁSSICOS & CITAÇÕES")

    print("\nEtapa 1 - Lendo arquivo local de autores prioritários...")
    autores = carregar_autores_prioritarios("autores_prioritarios.csv")
    print(f">>>>{len(autores)} autores prioritários carregados com sucesso.")

    print("\nEtapa 2 Consultando API pública de câmbio (GBP -> BRL)...")
    cotacao_gbp = obter_cotacao_gbp_brl()
    if cotacao_gbp:
        print(f">>>>Cotação obtida: 1 GBP = R$ {cotacao_gbp:.4f}")
    else:
        print("Falha ao obter cotação. Usando valor padrão aproximado")
        cotacao_gbp = 7.0

    print("\nEtapa 3 Coletando catálogo de livros da categoria Classics...")
    url_classicos = "http://books.toscrape.com/catalogue/category/books/classics_6/index.html"
    livros = coletar_livros_categoria(url_classicos, cotacao_gbp)
    print(f">>>>{len(livros)} livros coletados e convertidos para Reais.")

    print("\nEtapa 4 Coletando citações via Selenium")
    citacoes = coletar_citacoes_autores(autores)
    print(f">>>>{len(citacoes)} citações filtradas para os autores prioritários.")


    print("\n[Exportação] Salvando os resultados em arquivos Excel...")
    
    df_catalogo = pd.DataFrame(livros)
    colunas_catalogo = ["título", "preço em libras", "preço em reais", "disponibilidade", "avaliação"]
    df_catalogo = df_catalogo[colunas_catalogo]  
    df_catalogo.to_excel("catalogo_campanha.xlsx", index=False)
    print(">>>Arquivo 'catalogo_campanha.xlsx' gerado com sucesso.")

    df_citacoes = pd.DataFrame(citacoes)
    colunas_citacoes = ["autor", "texto da citação"]
    df_citacoes = df_citacoes[colunas_citacoes]  # Garante a ordem exata das colunas pedida
    df_citacoes.to_excel("citacoes_campanha.xlsx", index=False)
    print(">>>Arquivo 'citacoes_campanha.xlsx' gerado com sucesso.")

    print("PIPELINE CONCLUÍDO!")

if __name__ == "__main__":
    executar_pipeline()

