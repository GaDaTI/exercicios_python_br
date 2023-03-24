"""
18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
 velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
  de download do arquivo usando este link (em minutos).
"""
# Entrada de dados:
import math

tamanho_arquivo = float(input("Tamanho de um arquivo para download: "))
velocidade_Internet = float(input("Velocidade de um link de Internet (em Mbps): "))

# Processamento de dados:
tempo_de_download_min = (tamanho_arquivo / (velocidade_Internet / 8))/ 60
tempo_de_download_min = math.ceil(tempo_de_download_min)

# Saida de dados:
print(f"o tempo aproximado de download do arquivo usando este link é de {tempo_de_download_min} em minutos.")
