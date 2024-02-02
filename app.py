from models.restaurante import Restaurante


restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Marcelo', 7)
restaurante_praca.receber_avaliacao('Marcelo', 4)

def main():
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()