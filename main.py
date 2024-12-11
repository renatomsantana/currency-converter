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
