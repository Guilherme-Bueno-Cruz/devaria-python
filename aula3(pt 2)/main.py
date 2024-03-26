from Quadrado import Quadrado
from Circulo import Circulo

if __name__ == '__main__':

    formas = [
        Quadrado(),
        Circulo()
        ]

    for forma in formas:
        forma.desenhar()


