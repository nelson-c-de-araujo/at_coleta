import requests

def obter_cotacao_gbp_brl():

    url = "https://economia.awesomeapi.com.br/json/last/GBP-BRL"
    
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        
        dados = resposta.json()
      
        cotacao = float(dados["GBPBRL"]["bid"])
        return cotacao

    except requests.RequestException as e:
        print(f"Erro ao consultar a API: {e}")
        return None

if __name__ == "__main__":
    valor_cotacao = obter_cotacao_gbp_brl()
    if valor_cotacao:
        print("ETAPA 2: Cotação Obtida com Sucesso")
        print(f"1 GBP = R$ {valor_cotacao:.2f}")
    else:
        print("Não foi possível obter a cotação.")
