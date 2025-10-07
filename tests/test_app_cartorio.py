import pytest
from app_cartorio import CalculadoraCustosRegistro

def test_calculo_venda_faixa_1():
   
    calc = CalculadoraCustosRegistro(valor_imovel=45000)
    custos = calc.calcular_custos_registro_venda()
    assert custos["emolumentos"] == 450.0
    assert custos["fepj"] == 90.0      # 20% de 450
    assert custos["farpen"] == 150.0
    assert custos["issqn"] == 22.5     # 5% de 450
    assert custos["total"] == 712.5

def test_calculo_venda_faixa_3():
    
    calc = CalculadoraCustosRegistro(valor_imovel=180000)
    custos = calc.calcular_custos_registro_venda()
    assert custos["emolumentos"] == 1600.0
    assert custos["fepj"] == 320.0
    assert custos["farpen"] == 150.0
    assert custos["issqn"] == 80.0
    assert custos["total"] == 2150.0

def test_calculo_financiamento():
    
    calc = CalculadoraCustosRegistro(valor_imovel=250000, valor_financiamento=150000)
    custos = calc.calcular_custos_registro_financiamento()
    assert custos["emolumentos"] == 1600.0  
    assert custos["total"] == 2150.0

def test_calculo_total_operacao():
    
    calc = CalculadoraCustosRegistro(valor_imovel=300000, valor_financiamento=180000)
    resultado_total = calc.calcular_custo_total_operacao()
    # Custo da venda (base 300k): emol=2200, fepj=440, farpen=150, issqn=110 -> total = 2900
    # Custo do financ. (base 180k): emol=1600, fepj=320, farpen=150, issqn=80 -> total = 2150
    assert resultado_total["custos_venda"]["total"] == 2900.0
    assert resultado_total["custos_financiamento"]["total"] == 2150.0
    assert resultado_total["total_geral"] == 5050.0

def test_financiamento_zero_gera_custo_zero():
    calc = CalculadoraCustosRegistro(valor_imovel=100000, valor_financiamento=0)
    custos_financiamento = calc.calcular_custos_registro_financiamento()
    assert custos_financiamento["total"] == 0

def test_valor_imovel_invalido():
    with pytest.raises(ValueError, match="O valor do imóvel deve ser um número positivo."):
        CalculadoraCustosRegistro(valor_imovel=-50000)

def test_valor_financiamento_invalido():
    with pytest.raises(ValueError, match="O valor do financiamento deve ser um número positivo ou zero."):
        CalculadoraCustosRegistro(valor_imovel=100000, valor_financiamento="abc")