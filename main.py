def main():
    print("Bem-vindo ao Conversor de Moedas!")

    try:
        # Abre o arquivo 'input.txt' e lê o valor
        with open('input.txt', 'r') as file:
            amount_str = file.read().strip()
            amount = float(amount_str)
            print(f"Você digitou: {amount}")
    except FileNotFoundError:
        print("Erro: o arquivo de entrada não foi encontrado.")
    except ValueError:
        print("Erro: o valor no arquivo não é válido.")
    
    # Continue com o código de conversão aqui...

if __name__ == "__main__":
    main()
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    # Usa a variável de ambiente 'PORT' ou a porta 5000 por padrão
    port = int(os.environ.get('PORT', 5000))  # Pegando a variável 'PORT' ou usando 5000 se não existir
    app.run(host='0.0.0.0', port=port)
