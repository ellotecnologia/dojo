def calcula_troco(total_compra, valor_pago):
    troco = valor_pago - total_compra 
    inteiro = int(troco) # 4
    fracao  = troco - int(troco) # 0.50
    resultado = ""

    if inteiro > 0:
       resultado = f"{inteiro} moedas de $1.00"

    if fracao > 0:
        if fracao == 0.50:
            fracao = 0.25 
            resultado += f" e 2 moedas de ${fracao} centavos"

    return resultado
