import pytest
from gym_system import calculate_total

# REQUISITO 11: Unit Testing - Verificar cálculos para diferentes casos

def test_basic_plan_calculation():
    # Plan de 100, sin extras, 1 persona
    # Costo esperado: 100
    assert calculate_total(100, 0, 1, False) == 100

def test_premium_surcharge_req6():
    # Plan de 150 (Premium), sin extras, 1 persona
    # Subtotal 150. Recargo Premium 15% -> 150 * 1.15 = 172.5
    # Total < 200, no aplica descuento especial.
    # Resultado int: 172
    assert calculate_total(150, 0, 1, True) == 172
    
def test_group_discount_req4():
    # Plan 100, 2 personas. Base = 200.
    # Descuento grupo 10% -> 200 * 0.9 = 180.
    # Total < 200, sin descuento especial.
    assert calculate_total(100, 0, 2, False) == 180

def test_special_offer_200_req5():
    # Plan 200, 1 persona, Feature 30. Total base 230.
    # No es premium. No es grupo.
    # > 200, aplica descuento -$20 -> 210.
    assert calculate_total(200, 30, 1, False) == 210

def test_validation_req7_logic():
    # Si la cantidad de personas es 0, debe retornar -1 (Error)
    assert calculate_total(100, 0, 0, False) == -1
