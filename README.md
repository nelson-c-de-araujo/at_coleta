# Pipeline de Coleta de Dados - Campanha 'Clássicos & Citações'

Projeto de automação de coleta e enriquecimento de dados desenvolvido para o Assessment (AT) da disciplina de Coleta de Dados.

## Estrutura do Projeto

* `autores_prioritarios.csv`: Arquivo de entrada contendo os autores prioritários da campanha.
* `etapa1.py`: Módulo responsável pela leitura do arquivo CSV local.
* `etapa2.py`: Módulo responsável pela consulta à AwesomeAPI para cotação GBP/BRL.
* `etapa3.py`: Módulo de web scraping estruturado dos livros (Books to Scrape) usando BeautifulSoup.
* `etapa4.py`: Módulo de web scraping dinâmico (Quotes to Scrape JS) usando Selenium.
* `main.py`: Script integrador que executa o pipeline completo e gera as planilhas Excel.

## Arquivos Gerados

* `catalogo_campanha.xlsx`: Planilha com os livros da categoria escolhida, preços em libras e reais, disponibilidade e avaliação.
* `citacoes_campanha.xlsx`: Planilha com as citações coletadas dos autores prioritários.

## Como Executar

1. Ativar o ambiente virtual:
   ```bash
   .\venv\Scripts\activate
   ```
2. Executar o pipeline principal:
   ```bash
   python main.py
   ```

