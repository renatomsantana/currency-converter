from converter import CurrencyConverter

def main():
    print("Bem-vindo ao Conversor de Moedas!")
    amount = float(input("Digite o valor a ser convertido: "))
    from_currency = input("Digite a moeda de origem (ex: USD): ").upper()
    to_currency = input("Digite a moeda de destino (ex: BRL): ").upper()

    converter = CurrencyConverter()
    try:
        result = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
