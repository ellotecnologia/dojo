import unittest
from pdv import calcula_troco

class TestaPdv(unittest.TestCase):

    def testa_troco_com_compra_de_10_reais(self):
        valor_compra = 5.00
        valor_pago = 10.00
        self.assertEqual("5 moedas de $1.00", calcula_troco(valor_compra, valor_pago))

    def testa_troco_com_compra_de_25_reais_50_centavos(self):
        valor_compra = 25.50
        valor_pago = 30.00
        self.assertEqual("4 moedas de $1.00 e 2 moedas de $0.25 centavos", calcula_troco(valor_compra, valor_pago))
    
unittest.main()
