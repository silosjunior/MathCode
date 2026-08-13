def calcula_prestacao_mensal(
        p: float,
        i_a: float,
        n: int,
    ) -> float:
    """
    Calcula a prestação mensal para o financiamento de um imóvel
    obedecendo ao Sistema Francês de Amortização (Tabela Price).

    Args:
    - p (float): valor total do imóvel a ser financiado.
    - i_a (float): taxa de juros anual em formato decimal.
    - n (int): prazo total de pagamento em meses.

    Returns:
    - prestacao (float): valor da prestação mensal.
    """
    i_m = (1 + i_a) ** (1/12) - 1

    numerador = i_m * (1 + i_m) ** n
    denominador = (1 + i_m) ** n - 1
    prestacao = p * (numerador / denominador)

    return prestacao


def valida_risco_etario(idade: int) -> float:
    """
    Avalia o risco etário e determina o valor do seguro obrigatório.

    Args:
    - idade (int): idade informada pelo solicitante.

    Returns:
    - float: o valor do seguro obrigatório caso o solicitante informe
             idade entre 65 e 120 anos.

    Raises:
    - ValueError: nos casos em que o solicitante é menor de 18 anos ou
                  ultrapassa a idade limite de 120 anos.
    """
    if idade < 18 or idade > 120:
        raise ValueError("Critérios inválidos para dar prosseguimento.")

    if idade < 65:
        return 0.0
    
    return 850.00

def calcula_risco_credito(
        prestacao: float,
        renda: float,
        ) ->  bool:
    """
    Aprova um financiamento desde que a prestação mensal não exceda 30% da
    renda bruta mensal comprovada.

    Args:
    - prestacao (float): valor da prestação mensal calculada (inlcuindo taxas
    e seguros).
    - renda (float): renda bruta mensal comprovada do solicitante.

    Returns:
    - bool: o crédito é aprovado se a função retorna `True`. `False`, caso contrário.
    """
    return prestacao <= renda * 0.30

def obter_taxa_por_score(score: int) -> float:
    """
    Determina a taxa anual de juros para os casos em que o score do solicitante
    trafega entre os índices 3 e 5. Nega o crédito para scores entre 1 e 2.

    Args:
    - score (int): valores inteiros indicadores do histórico financeiro do
    solicitante (1 a 5).

    Returns:
    - float: as taxas de juros anual de 13.5% (para score igual a 3) e 0.95% para os
    scores 4  5.

    Raises:
    - ValueError: quando o score informado está fora do intervalo (1 a 5) ou quando o
    score está entre 1 e 2.
    """
    if score < 1 or score > 5:
        raise ValueError("Critérios inválidos para cálculo da taxa.")

    if score in (4, 5):
        return 0.095
    elif score == 3:
        return 0.135
    else:
        raise ValueError("Score insuficiente. Crédito negado.")

def executar_motor_credito() -> None:
    """
    Função orquestradora do sistema de financiamento de um imóvel.
    Coleta dados do solicitante, faz os devidos cálculos do financiamento,
    os valida e determina sua aprovação ou negação.
    """
    try:
        valor_imovel = float(input("Valor do imóvel (R$): "))
        idade_solicitante = int(input("Idade do solicitante: "))
        renda_solicitante = float(input("Renda mensal bruta (R$): "))
        prazo_pagamento = int(input("Prazo para pagamento (anos): "))
        score_solicitante = int(input("Score de crédito: "))

        prazo_meses = prazo_pagamento * 12

        valor_seguro = valida_risco_etario(idade_solicitante)
        taxa_anual = obter_taxa_por_score(score_solicitante)

        prestacao_base = calcula_prestacao_mensal(valor_imovel, taxa_anual, prazo_meses)
        prestacao_total = prestacao_base + valor_seguro

        credito_aprovado = calcula_risco_credito(prestacao_total, renda_solicitante)

        if credito_aprovado:
            print(f"Simulação aprovada. {prazo_meses} parcelas de R$ {prestacao_total:.2f} ")
        else:
            print("Crédito negado. Insuficiência de renda.")

    except ValueError as e:
        print(e)


if __name__ == "__main__":

    executar_motor_credito()







