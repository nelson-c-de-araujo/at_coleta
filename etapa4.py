

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def coletar_citacoes_autores(lista_autores_prioritarios):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=chrome_options)
    url_base = "https://quotes.toscrape.com/js/"
    citacoes_coletadas = []

    autores_alvo = [autor.strip().lower() for autor in lista_autores_prioritarios]

    try:
        driver.get(url_base)

        while True:
            # Aguarda 10 sec pra entender se o JS foi renderizado
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "quote"))
            )

            # Encontra todos os blocos de citação renderizados
            blocos_quote = driver.find_elements(By.CLASS_NAME, "quote")

            for bloco in blocos_quote:
                nome_autor = bloco.find_element(By.CLASS_NAME, "author").text.strip()
                texto_citacao = bloco.find_element(By.CLASS_NAME, "text").text.strip()

                # Verifica se o autor da citação está na nossa lista
                if nome_autor.lower() in autores_alvo:
                    citacoes_coletadas.append({
                        "autor": nome_autor,
                        "texto da citação": texto_citacao
                    })

            # Tenta encontrar o botão "Next" para ir para a próxima página
            botoes_next = driver.find_elements(By.CSS_SELECTOR, "li.next > a")
            if botoes_next and botoes_next[0].is_displayed():
                botoes_next[0].click()
            else:
                
                break

    except Exception as e:
        print(f"Erro durante a execução do Selenium: {e}")

    finally:
        driver.quit()

    return citacoes_coletadas

if __name__ == "__main__":
    from etapa1 import carregar_autores_prioritarios

    autores = carregar_autores_prioritarios()
    resultado_citacoes = coletar_citacoes_autores(autores)

    print(f"ETAPA 4: {len(resultado_citacoes)} Citações Coletadas")
    for item in resultado_citacoes[:3]:  # Mostra as 3 primeiras
        print(f"Autor: {item['autor']} | Citação: {item['texto da citação']}")

