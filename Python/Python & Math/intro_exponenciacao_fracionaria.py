def calcular_raiz(radicando, indice_raiz, expoente_radicando=1):
    """
    Calcula a raiz de um número usando a propriedade dos expoentes fracionários.
    """
    # Transforma a raiz em uma potência de expoente fracionário.
    resultado = radicando ** (expoente_radicando / indice_raiz)
    return resultado


if __name__ == "__main__":
    # Definindo as variáveis baseadas no nosso estudo matemático:
    numero_base = 2
    indice_raiz = 3

    # Executando a função:
    valor_calculado = calcular_raiz(numero_base, indice_raiz)

    # Exibindo o resultado formatado
    print(f"O cálculo matemático para a raiz cúbica de {numero_base} é:")
    print(f"Resultado completo da máquina: {valor_calculado}")
    print(f"Resultado arredondado (2 casas decimais): {valor_calculado:.2f}")
