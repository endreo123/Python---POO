from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')

restaurante_praca.receber_avalicao('Gui', 10)

restaurante_praca.receber_avalicao('Endreo', 8)

restaurante_praca.receber_avalicao('ddddd', 1)

def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()
