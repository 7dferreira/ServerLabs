import sys

import subprocess

from decimal import Decimal as dec




def main():

    cambio_eur_usd = dec('1.10')



    while True:

        # 1. Exibimos menu (ie, as opções)

        cls()

        print("Escolha o sentido da conversão:")

        print("1. Euros -> Dólares")

        print("2. Dólares-> Euros")

        print("T. Terminar")



        # 2. Ler a opcao

        opcao = input("> ")



        # 3. Analisar e executar a opção

        if opcao == '1':

            montante = dec(input("Montante em euros: "))

            print(f'Dólares -> {montante * cambio_eur_usd:.2f}')

        elif opcao == '2':

            montante = dec(input("Montante em dólares: "))

            print(f'Euros -> {montante / cambio_eur_usd:.2f}')

        elif opcao == 'T':

            break

        else:

            print(f"Opção <{opcao}> inválida!")



        # 4. Continuar ou não

        if not confirma("Deseja repetir? "):

            break

    #:

#:



def confirma(msg: str) -> bool:

    while True:

        opcao_repetir = input(msg)

        if opcao_repetir.upper() in ('S', 'SIM'):

            return True

        elif opcao_repetir.upper() in ('N', 'NÃO', 'NAO'):

            return False

        else:

            print(f"Opção <{opcao_repetir}> errada!")

    #:

#:



def cls():

    if sys.platform in ('unix', 'linux', 'bsd', 'darwin'):

        subprocess.run(['clear'])

    elif sys.platform in ('win32'):

        subprocess.run(['cls'], shell=True)

#:



# public static boolean confirma(String msg) {

#     var in = new Scanner(System.in);

#     while (true) {

#         out.print(msg);

#         var opcaoRepetir = in.nextLine();

#         if (opcaoRepetir.equalsIgnoreCase("N")

#             || opcaoRepetir.equalsIgnoreCase("NAO")

#             || opcaoRepetir.equalsIgnoreCase("NÃO")) {

#             return false;

#         }

#         else if (opcaoRepetir.equalsIgnoreCase("S")

#                     || opcaoRepetir.equalsIgnoreCase("SIM")) {

#             return true;

#         }

#         else {

#             out.printf("Opção %s errada!\n", opcaoRepetir);

#         }

#     }

# }



if __name__ == '__main__':

    main()




# JS : import {Decimal} from 'decimal'



# tipos primitivos / built-in: int, float, str, bool,



# str(23)