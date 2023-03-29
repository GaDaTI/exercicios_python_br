"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
primeiro_vetor = list(range(0, 20, 2))
segundo_vetor = list(range(1, 20, 2))
terceiro_vetor = primeiro_vetor + segundo_vetor
terceiro_vetor.sort()
print(primeiro_vetor)
print(segundo_vetor)
print(terceiro_vetor)