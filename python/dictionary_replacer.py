import unittest


def substitui(template, dicionario):
    dentro    = False
    resultado = ''
    termo     = ''
    for l in template:
        if l != '$':
            if dentro:
                termo += l
            else:
                resultado += l
        else:
            if not dentro :
                dentro = True
                continue
            else:
                dentro = False
                resultado += dicionario[termo]
                termo  = ''
                        

    return resultado


class StringReplacerTest(unittest.TestCase):

    def test_substituicao_01(self):
        entrada = "$temp$ aqui vai o nome $name$"
        dicionario = {
            "temp": "bruno",
            "name": "gustavo"
        }
        resultado = substitui(entrada, dicionario)
        self.assertEqual("bruno aqui vai o nome gustavo", resultado)

    def test_substituicao_02(self):
        entrada = "Oi $fulano$ meu nome eh $nome$"
        dicionario = {
            "fulano": "layro",
            "nome": "clayton"
        }
        resultado = substitui(entrada, dicionario)
        self.assertEqual("Oi layro meu nome eh clayton", resultado)
     
    def test_substituicao_03(self):
        entrada = "Oi $fulano$ meu nome eh $nome$"
        dicionario = {
            "fulano": "renan",
            "nome": "gustavo"
        }
        resultado = substitui(entrada, dicionario)
        self.assertEqual("Oi renan meu nome eh gustavo", resultado)
     




if __name__ == "__main__":
    unittest.main()
