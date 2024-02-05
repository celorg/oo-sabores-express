from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import  Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_pao = Prato('Pão', 2.0, 'O melhor pão da cidade')
bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_praca.exibir_cardapio
    

if __name__ == '__main__':
    main()