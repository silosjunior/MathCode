from math import floor


def calcular_modulo(dividendo, divisor):
    """
    Calcula o módulo utilizando a definição de piso da divisão.
    """
    funcao_piso = floor(dividendo / divisor)
    resultado = dividendo - divisor * funcao_piso
    return resultado


if __name__ == "__main__":

    dividendo = -10
    divisor = 9

    modulo_calculado = calcular_modulo(dividendo, divisor)

    print(
        f"O cálculo do módulo para {dividendo} e {divisor} é {modulo_calculado}"
    )
    print(
        f"O mesmo resultado obtém-se com o uso da expressão 'dividendo' % 'divisor' = {dividendo % divisor}"
    )
