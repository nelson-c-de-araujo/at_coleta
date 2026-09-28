
import requests
from bs4 import BeautifulSoup

def converter_avaliacao_para_numero(classe_estrela):

    mapa_estrelas = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    for palavra, valor in mapa_estrelas.items():
        if palavra in classe_estrela:
            return valor
    return 0

def coletar_livros_categoria(url_categoria, cotacao_gbp):

    livros = []
    url_atual = url_categoria

    while url_atual:
        resposta = requests.get(url_atual, timeout=10)
        resposta.encoding = 'utf-8'
        
        if resposta.status_code != 200:
            print(f"Erro ao acessar a página: {url_atual}")
            break

        soup = BeautifulSoup(resposta.text, 'html.parser')
        artigos = soup.find_all('article', class_='product_pod')

        for artigo in artigos:

            tag_link = artigo.h3.find('a')
            titulo = tag_link.get('title') if tag_link.get('title') else tag_link.text.strip()


            texto_preco = artigo.find('p', class_='price_color').text
            preco_libras = float(texto_preco.replace('£', '').replace('Â', '').strip())

            preco_reais = round(preco_libras * cotacao_gbp, 2) if cotacao_gbp else 0.0

            disponibilidade = artigo.find('p', class_='instock availability').text.strip()

            tag_rating = artigo.find('p', class_='star-rating')
            classes_rating = tag_rating.get('class', []) if tag_rating else []
            avaliacao = converter_avaliacao_para_numero(" ".join(classes_rating))

            livros.append({
                "título": titulo,
                "preço em libras": preco_libras,
                "preço em reais": preco_reais,
                "disponibilidade": disponibilidade,
                "avaliação": avaliacao
            })

        tag_next = soup.find('li', class_='next')
        if tag_next and tag_next.find('a'):
            link_proximo = tag_next.find('a')['href']

            base_url = url_atual.rsplit('/', 1)[0]
            url_atual = f"{base_url}/{link_proximo}"
        else:
            url_atual = None

    return livros

if __name__ == "__main__":
    from etapa2 import obter_cotacao_gbp_brl

    cotacao = obter_cotacao_gbp_brl() or 7.0
    url_classicos = "http://books.toscrape.com/catalogue/category/books/classics_6/index.html"
    
    lista_livros = coletar_livros_categoria(url_classicos, cotacao)
    
    print(f"ETAPA 3: {len(lista_livros)} Livros Coletados")
    for livro in lista_livros[:3]:
        print(livro)
