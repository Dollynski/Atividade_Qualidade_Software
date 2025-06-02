import pytest
from src.desconto import aplicar_desconto

def test_desconto_10_porcento():
    assert aplicar_desconto(100, 10) == 90

def test_desconto_zero():
    assert aplicar_desconto(100, 0) == 100

def test_erro_porcentagem_maior_que_100():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 120)

def test_erro_porcentagem_negativa():
    with pytest.raises(ValueError):
        aplicar_desconto(100, -5)
