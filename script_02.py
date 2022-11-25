"""
Programação OOP

Encapsulamento

"""


class MaquinaDeCafe:

    def __init__(self, cafe=5000, leite=2000, chocolate=2000):
        self._cafe = cafe
        self._leite = leite
        self._chocolate = chocolate

    def _fazer_cafe(self):
        print("PREPARANDO O CAFÉ")

    def _fazer_leite(self):
        print("PREPARANDO O LEITE")

    def _fazer_chocolate(self):
        print("PREPARANDO O CHOCOLATE")

    def _fazer_cappuccino(self):
        print("PREPARANDO O CAPPUCCINO")

    def preparar_bebida(self, opcao):

        # Café
        if opcao == 1:
            self._fazer_cafe()

        # Leite
        elif opcao == 2:
            self._fazer_leite()

        # Chocolate
        elif opcao == 3:
            self._fazer_chocolate()

        # Cappuccino
        elif opcao == 4:
            self._fazer_cappuccino()

        # Mostrar erro
        else:
            print("Opção desconhecida.")


if __name__ == "__main__":

    texto = """
    Escolha a sua bebida:
    
    1) Café (Café + Água)
    2) Leite (Leite)
    3) Chocolate (Chocolate + Leite)
    4) Cappuccino (Café + Leite + Chocolate)
"""

    print(texto)

    opcao = int(input("Informe a opção desejada: "))

    maquina_de_cafe = MaquinaDeCafe()
    maquina_de_cafe.preparar_bebida(opcao)