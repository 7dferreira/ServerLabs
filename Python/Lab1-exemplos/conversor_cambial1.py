
from decimal import Decimal as dec
import subprocess
def main():

    cambio_eur_usd = dec('1.10')

    while True:

        #Exibir menu
        print("Escolha o sentido da conversão:")
        print("1. Euros -> Dólares")
        print("2. Dólares-> Euros")
        print("T. Terminar")

        #Ler a opçao
        opcao = input("> ")

        #Analisar e executar a opção introduzida

        if opcao == '1':
            montante = dec(input("Montante em euros: "))
            print(f'Dólar -> {montante * cambio_eur_usd: .2f}')

        elif opcao == '2':
            montante = dec(input("Montante em dólares: "))
            print(f'Euros -> {montante / cambio_eur_usd: .2f}')

        elif opcao == 'T':
            break

        else:
            print(f"Opção <{opcao}> inválida!")

    # 4. Continuar ou não

        if not confirma("Deseja repetir? "):
            2
            break

        

def confirma(msg: str) -> bool:
    while True:
        opcao_repetir = input(msg)
        if opcao_repetir.upper() in ('S', 'SIM'):
            return True
        elif opcao_repetir.upper() in ('N', 'NÃO', 'NAO'):
            return False
        else:
            print(f"Opção <{opcao_repetir}> errada!")


if __name__ == '__main__':

    main()