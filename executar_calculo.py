 
from app_cartorio import CalculadoraCustosRegistro

valor_do_imovel = 350000
valor_do_financiamento = 280000

calculadora = CalculadoraCustosRegistro(valor_imovel=valor_do_imovel, valor_financiamento=valor_do_financiamento)

custos_totais = calculadora.calcular_custo_total_operacao()

print("--- Simulação de Custos de Registro de Imóvel ---")
print(f"Valor do Imóvel: R$ {valor_do_imovel:,.2f}")
print(f"Valor do Financiamento: R$ {valor_do_financiamento:,.2f}\n")

print(f"Custos Detalhados da Venda: {custos_totais['custos_venda']}")
print(f"Custos Detalhados do Financiamento: {custos_totais['custos_financiamento']}\n")
print(f"==================================================")
print(f"  TOTAL GERAL DA OPERAÇÃO: R$ {custos_totais['total_geral']:.2f}")
print(f"==================================================")