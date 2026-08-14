def f(x: int) -> int:
    """
    Função matemática elementar.
    Mapeia um número inteiro (Domínio X) para o seu quadrado (Contradomínio Y).

    Args:
    - x (int): número inteiro que representa o domínio da função.

    Returns:
    - y (int): número inteiro que representa o contradomínio da função.
    """
    y = x ** 2
    return y

def verifica_simetria_matematica(s: str) -> bool:
    """
    Motor matemático puro para verificação de palíndromos.
    Não inclui sanitização de dados.

    Args:
    - s (str): a string a ser testada se é um palíndromo.

    Returns:
    - bool: `True` se `s` for um palíndromo, `False`, caso contrário.
    """
    n = len(s)

    # range(k) cria o conjunto {0, 1, ..., k - 1}
    # range(n // 2) traduz o conjunto matemático {0, 1, ..., floor(n/2) - 1}
    conjunto_indices = range(n // 2)

    for i in conjunto_indices:
        # A condicional inverte a lógica do $\forall$ (*Fail-Fast*).
        # Se achar uma única falha, quebra a prova e retorna Falso
        # imediatamente.
        if s[i] != s[n - 1 - i]:
            return False

    return True

def multiplicacao_primitiva(a: int, b: int) -> int:
    """
    Emula a multiplicação através do somatório discreto.
    """
    acumulador = 0
    # O laço for simula o índice k variando de 1 até b
    for _ in range(b):
        acumulador += a
    return acumulador

def divisao_inteira_primitiva(a: int, b: int) -> tuple[int, int]:
    """
    Emula a divisão buscando o máximo de subtrações sucessivas.

    Returns:
    - tuple: quociente, resto
    """
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não pertence aos reais.")

    n = 0
    resto = a

    # Simula a condição (a - n*b >= 0)
    while resto - b >= 0:
        resto -= b
        n += 1

    return n, resto

def simula_impacto_exponencial(
        custo_inicial: float,
        taxa_degradacao: float,
        tempo: int,
        ) -> float:
    """
    Calcula o impacto financeiro ou estrutural cumulativo de um incidente de segurança.

    Args:
    - custo inicial (float): valor do prejuízo causado pelo incidente no marco 0.
    - taxa_degradacao (float): taxa de degradação expressa em formato decimal.
    - tempo (int): tempo usado para cálculo do montante do prejuízo.

    Returns:
    - float: montante do prejuízo no intervalo de tempo indicado.
    """
    impacto_total = custo_inicial * ((1 + taxa_degradacao) ** tempo)
    return impacto_total

def analisa_payload_ofuscado(payload: str) -> bool:
    """
    Verifica se uma string é ou não um palíndromo. A string é sanitizada.

    Args:
    - payload (str): a string a ser analisada.

    Returns:
    - bool: True, se a string for palíndromo, False caso contrário.
    """
    payload = payload.lower()

    tamanho = len(payload)

    for i in range(tamanho // 2):
        if payload[i] != payload[tamanho - 1 - i]:
            return False

    return True

def verifica_primalidade(n: int) -> bool:
    """
    Verifica se um número é primo.

    Args:
    - n (int): o número inteiro a ser testado.

    Returns:
    - bool: `True` se for primo, `False`, caso contrário.
    """
    if n <= 1:
        return False

    elif n == 2:
        return True

    elif n % 2 == 0:
        return False

    limite = int(n ** 0.5)
    divisor = 3

    while divisor <= limite:
        if n % divisor == 0:
            return False
        divisor += 2

    return True
    
def gera_proximo_primo(n: int) -> int:
    """
    Gera o próximo número primo, após fornecido um número inteiro.

    Args:
    - n (int): o inteiro que precede o próximo número primo.

    Returns:
    - int: o número primo seguinte ao encontrado no domínio.
    """
    candidato = n + 1

    while True:
        if verifica_primalidade(candidato):
            return candidato

        candidato += 1

def calcula_mdc(a: int, b: int) -> int:
    """
    Calcula o máximo divisor comum de dois inteiros usando o
    algoritmo de Euclides.

    Args:
    - a (int): o primeiro inteiro do domínio.
    - b (int): o segundo inteiro do domínio.

    Returns:
    - int: o máximo divisor comum de `a` e `b`.
    """
    while b != 0:
        a, b = b, a % b

    return a

def gera_expoente_publico(phi: int) -> int:
    """
    Gera uma chave pública RSA a partir da coprimalidade de um
    expoente e phi.

    Args:
    - phi (int): número que servirá como determinação da coprimalidade
    em relação ao expoente público.

    Returns:
    - int: o expoente público quando encontrada a coprimalidade.
    """
    e = 2
    while calcula_mdc(e, phi) != 1:
        e += 1

    return e

def calcula_inverso_modular(e: int, phi: int) -> int:
    """
    Calcula o inverso multiplicativo modular do expoente público
    em relação ao módulo de phi.

    Args:
    - e (int): o expoente público.
    - phi (int): função totiente de Euler.

    Returns:
    - int: o inverso multiplicativo positivo.
    """
    t, novo_t = 0, 1
    r, novo_r = phi, e

    while novo_r != 0:
        quociente = r // novo_r
        t, novo_t = novo_t, t - quociente * novo_t
        r, novo_r = novo_r, r - quociente * novo_r

    return t % phi

def exponenciacao_modular(base: int, expoente: int, modulo: int) -> int:
    """
    Calcula a exponenciação modular utilizando a representação binária
    do expoente e a propriedade distributiva da aritmética módular.

    Args:
    - base (int): mensagem base.
    - expoente (int): expoente colossal.
    - modulo (int): o módulo numérico aplicado.

    Returns:
    - int: a chave de decriptação.
    """
    resultado = 1
    base = base % modulo

    while expoente > 0:
        if expoente % 2 == 1:
            resultado = (resultado * base) % modulo

        base = (base ** 2) % modulo
        expoente = expoente // 2

    return resultado

def gera_par_chaves_rsa(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Gera um par de chaves RSA.

    Args:
    - p (int): entrada para geração do par de chaves.
    - q (int): entrada para geração do par de chaves.

    Returns:
    - tuple[int, int], [int. int]
    """
    if not verifica_primalidade(p) or not verifica_primalidade(q):
        raise ValueError("Os parâmetros 'p' e 'q' devem ser números primos.")

    n, phi = p * q, (p - 1) * (q - 1)

    e = gera_expoente_publico(phi)

    d = calcula_inverso_modular(e, phi)

    return (e, n), (d, n)



if __name__ == "__main__":

    while True:
        print("")
        print("CipherCore - SecOps Toolkit Triage")
        print("")
        print("* Análise de payload: Opção -> 1")
        print("* Simulador de impactos financeiros por incidente -> Opção 2")
        print("* Análise de Emulação de Shellcode (divisão primitiva) -> Opção 3")
        print("* Produto calculado pela emulação primitiva da ALU -> Opção 4")
        print("* Verificador de números primos -> Opção 5")
        print("* Gerador do próximo número primo -> Opção 6")
        print("* Cálculo do coprimo (MDC) -> Opção 7")
        print("* Gerador de chave pública (e) RSA -> Opção 8")
        print("* Gerador de chave privada RSA (d) -> Opção 9")
        print("* Exponenciação Modular Rápida -> Opção 10")
        print("* Gerador de par de chaves RSA -> Opção 11")
        print("* Encerra a operação -> Opção 0 (zero)")
        print("")
        tool = (input("Digite a opção desejada: "))

        if tool == "0":
            print("Programa encerrado.")
            break

        elif tool == "1":
            payload = input("Digite o payload para análise: ")
            if analisa_payload_ofuscado(payload):
                print(" >>> O payload apresenta comportamento anômalo.")
            else:
                print(" >>> O payload não representa uma ameaça ao sistema.")

        elif tool == "2":
            custo_ini_incidente = float(input("Digite o custo inicial do incidente (R$): "))
            taxa_degradacao = float(input("Digite a taxa de degradação em formato decimal (ex: 3.31): "))
            tempo_simulacao = int(input("Digite o tempo em que deseja simular o prejuízo total (dias):"))
            prejuizo_total = simula_impacto_exponencial(custo_ini_incidente, taxa_degradacao, tempo_simulacao)
            print(f"O impacto total para o período simulado é de R$ {prejuizo_total:.2f}.")

        elif tool == "3":
            try:
                dividendo = int(input("Digite um valor para o dividendo (int): "))
                divisor = int(input("Digite um valor para o divisor (int): "))
                quociente, resto = divisao_inteira_primitiva(dividendo, divisor)
                print(f"Foram obtidos os seguintes resultados: ")
                print(f"Quociente = {quociente} / Resto = {resto}")
            except ValueError:
                print("Digite apenas valores inteiros.")
            except ZeroDivisionError:
                print("Foi inserido 0 (zero) no campo do divisor.")

        elif tool == "4":
            try:
                fator_base = int(input("Digite o valor base para o cálculo (int): "))
                multiplicador = int(input("Digite o multiplicador (int): "))
                produto = multiplicacao_primitiva(fator_base, multiplicador)
                print(f"O produto calculado pela emulação primitiva da ALU é {produto}")
            except ValueError:
                print("Entrada inválida.")

        elif tool == "5":
            try:
                numero = int(input("Digite um número para verificar sua primalidade (int): "))
                if verifica_primalidade(numero):
                    print(f"{numero} é primo.")
                else:
                    print(f"{numero} é composto.")
            except ValueError:
                print("Entrada inválida.")

        elif tool == "6":
            try:
                candidato = int(input("Digite um número para verificar qual o seu próximo primo: "))
                proximo_primo = gera_proximo_primo(candidato)
                print(f"O próximo número primo após {candidato} é {proximo_primo}.")
            except ValueError:
                print("Entrada inválida.")

        elif tool == "7":
            try:
                int_1 = int(input("Digite o primeiro número inteiro: "))
                int_2 = int(input("Digite o segundo número inteiro: "))
                coprimo = calcula_mdc(int_1, int_2)
                print(f"O MDC de {int_1} e {int_2} é {coprimo}.")
            except ValueError:
                print("Entrada inválida.")

        elif tool == "8":
            try:
                valor_inteiro = int(input("Insira um valor inteiro para a função totiente (phi): "))
                expoente = gera_expoente_publico(valor_inteiro)
                print(f"Expoente público {expoente} gerado para a função phi {valor_inteiro}")
            except ValueError:
                print("Entrada inválida.")

        elif tool == "9":
            try:
                expoente_publico = int(input("Digite o expoente público (e): "))
                totiente = int(input("Digite o totiente (phi): "))
                chave_privada = calcula_inverso_modular(expoente_publico, totiente)
                print(f"A chave privada gerada é {chave_privada}")
            except ValueError:
                print("Entrada inválida.")

        elif tool == "10":
            try:
                mensagem = int(input("Digite a base: "))
                chave = int(input("Digite o expoente: "))
                modulo = int(input("Digite o módulo numérico: "))
                resultado = exponenciacao_modular(mensagem, chave, modulo)
                print(f"O resultado cifrado/decifrado é {resultado}.")
            except ValueError:
                print("Entrada inválida.")

        elif tool == "11":
            try:
                candidato_1 = int(input("Informe o primeiro número primo: "))
                candidato_2 = int(input("I:nforme o segundo número primo: "))
                chave_e, chave_d = gera_par_chaves_rsa(candidato_1, candidato_2)
                print(f"Chave Pública: {chave_e} | Chave privada: {chave_d}")
            except ValueError as e:
                print(e)
            except ValueError:
                print("Entrada inválida.")
        else:
            print("Entrada inválida.")



    

    # dominio_x = [1, 2, 3]

    # for elemento in dominio_x:
    #     resultado = f(elemento)
    #     print(f"f({elemento}) = {resultado}")

    # palindromo_nao_sanitizado = verifica_simetria_matematica("RadAR")
    # print(palindromo_nao_sanitizado)

    # produto_primitivo = multiplicacao_primitiva(4, 3)
    # print(produto_primitivo)

    # quociente_resto = divisao_inteira_primitiva(9, 0)
    # print(quociente_resto)

    # prejuizo_acumulado = simula_impacto_exponencial(8.989, 3.31, 11)
    # print(f"Prejuízo acumulado em R$ {prejuizo_acumulado:.2f}")

    # while True:
    #     comando = input("Digite o payload (ou 'SAIR' para encerrar:) ")
    #     if comando.lower() == "sair":
    #         break
    #     else:
    #         if analisa_payload_ofuscado(comando):
    #             print(f"{comando} representa um comportamento anômalo.")
    #         else:
    #             print(f"{comando} é um artefato benigno.")