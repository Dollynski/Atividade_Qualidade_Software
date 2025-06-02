def aplicar_desconto(valor, porcentagem):
    if not 0 <= porcentagem <= 100:
        raise ValueError("Porcentagem inválida")
    return valor - (valor * porcentagem / 100)
