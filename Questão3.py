import json

def carregar_dados(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def calcular_faturamento(dados):
    valores = [item['valor'] for item in dados['faturamento']]
    
    dias_com_faturamento = [valor for valor in valores if valor > 0]
    
    if not dias_com_faturamento:
        return None, None, 0  
    
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    
    
    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media


dados = carregar_dados('faturamento.json')

menor, maior, dias_acima_media = calcular_faturamento(dados)

if menor is not None:
    print(f"Menor valor de faturamento: R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias acima da média mensal: {dias_acima_media}")
else:
    print("Não há dados de faturamento para calcular.")