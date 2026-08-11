def converte_para_segundos(d, h, m, s) -> int :
    """
    Padroniza a quantidade de dias, horas e minutos no total em segundos.

    Args:
    - d (int): dias a serem convertidos em segundos.
    - h (int): horas a serem convertidas em segundos.
    - m (int): minutos a serem convertidos em segundos.
    - s (int): segundos somados ao tempo total.

    Returns:
    - S (int): o total do tempo em segundos.
    """
    S = d * 86400 + h * 3600 + m * 60 + s
    return S

def converte_celsius_para_fahrenheit(t):
    """
    Converte temperatura Celsius em escala Farenheit.

    Args:
    - t (float): temperatura em Celsius a ser convertida em graus Fahrenheit.

    Returns:
    - F (float): temperatura em graus Fahrenheit.
    """
    F = (9 * t) / 5 + 32
    return F

def calcula_custo_servidor(
        d: int,
        taxa_diaria: float,
        gb: int,
        taxa_consumo: float
        ) -> float:
    """
    Calcula o Custo Total para o uso de um servidor em nuvem baseando-se na
    quantidade de dias utilizados e volume de dados trafegados.

    Args:
    - d (int): quantidade de dias que o servidor esteve ligado.
    - taxa_diaria (float): valor fixo cobrado por dia de uso.
    - gb (int): volume de Gigabytes (GB) trafegado.
    - taxa_consumo (float): taxa variável de acordo com o volume de dados
                            trafegados.

    Returns:
    - float: Custo Total a partir dos valores coletados pelo sistema.
    """
    custo_total = (d * taxa_diaria) + (gb * taxa_consumo)
    return custo_total

def calcula_tempo_transferencia(
        tamanho_do_arquivo: int,
        velocidade_rede: float,
    ) -> float:
    """
    Calcula o tempo em segundos para a transferência de um determinado volume de dados.

    Args:
    - tamanho_do_arquivo (int): volume de dados a serem transferidos Gigabytes (GB).
    - velocidade_rede (float): velocidade da rede Megabytes por segundo (MB/s).

    Returns:
    - t (float): tempo em segundos para a conclusão da transferência de dados.
    """
    t = (tamanho_do_arquivo * 1024) / velocidade_rede
    return t


if __name__ == "__main__":

    d = int(input("Informe a quantidade de dias:"))
    h = int(input("Informe a quantidade de horas:"))
    m = int(input("Informe a quantidade de minutos:"))
    s = int(input("Informe a quantidade de segundos:"))
    total_segundos = converte_para_segundos(d, h, m, s)
    print(total_segundos)

    temperatura_celsius = float(input("Informe a temperatura (graus Celsius):"))
    temperatura_fahrenheit = converte_celsius_para_fahrenheit(temperatura_celsius)
    print(f"{temperatura_fahrenheit:.2f} graus Farenheit.")

    dias = int(input("Número de dias utilizados: "))
    custo_diario = 5.00
    volume_dados = int(input("Volume de dados em Gigabytes (GB):"))
    valor_gb = 0.20
    extrato_cloud_server = calcula_custo_servidor(dias, custo_diario, volume_dados, valor_gb)
    print(f"Extrato mensal consolidado Silos Cloud Server: R$ {extrato_cloud_server:.2f}")

    volume_dados = int(input("Tamanho do arquivo em Gigabytes (GB): "))
    taxa_mbs = float(input("Velocidade da rede (MB/s): "))
    tempo_transferencia = calcula_tempo_transferencia(volume_dados, taxa_mbs)
    print(f"A transferência de arquivos levou {tempo_transferencia:.0f} segundos")