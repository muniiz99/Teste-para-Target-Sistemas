import json

# carrega os dados do json
with open('dados.json') as f:
    dados = json.load(f)

# inicializa as variáveis
menor = float('inf')
maior = float('-inf')
soma = 0
dias_acima_media = 0
dias_com_faturamento = 0
valores = []

# Salva no meu vetor valores, apenas o valor "valor" do meu json.
for obj in dados:
     valores.append(obj["valor"])

for valor in valores:
    if valor > 0.0:
        # atualiza o menor e o maior valor
        if valor < menor:
            menor = valor
        if valor > maior:
            maior = valor

        # acumula o valor para calcular a média
        soma += valor
        dias_com_faturamento += 1



media = soma / dias_com_faturamento

# percorre novamente os valores de faturamento diário
for valor in valores:
    if valor > 0.0 and valor > media:
        dias_acima_media += 1
print('='*44)
print(f"Menor valor de faturamento: R$ {menor:.2f}")
print(f"Maior valor de faturamento: R$ {maior:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
print('='*44)