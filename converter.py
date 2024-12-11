import requests
from config import API_KEY

class CurrencyConverter:
    API_URL = "https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}"

    def convert(self, amount, from_currency, to_currency):
        url = self.API_URL.format(api_key=API_KEY, currency=from_currency)
        response = requests.get(url)
        
        if response.status_code != 200:
            raise ValueError("Erro ao acessar a API. Verifique sua conexão ou chave.")
        
        data = response.json()
        if "conversion_rates" not in data:
            raise ValueError("Dados de conversão indisponíveis.")
        
        rates = data["conversion_rates"]
        if to_currency not in rates:
            raise ValueError(f"Moeda de destino {to_currency} não suportada.")
        
        return amount * rates[to_currency]
