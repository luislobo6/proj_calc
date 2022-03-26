import pytest
#import funciones as tf
import sys
sys.path.append("c:/Tutoriales/proj_calc/src/")
import cacl as tf

def obtener_datos_suma():
  """ 
  Función que genera un arreglo de tuplas con los 
  datos que se usarán para probar la función suma 
  """
  return [(1,1,2),("1/4",2,2.25), (0.5,"1/4", 0.75)]

@pytest.mark.parametrize("numero1,numero2,resultado",obtener_datos_suma())
def test_suma(numero1, numero2, resultado):
  """
  Función que prueba la función suma
  Args:
    numero1: primer sumando
    numero2: segundo sumando
    resultado: resultado esperado 

  Returns: True si es correcta la evaluación y False si no lo es

  """
  assert tf.suma(numero1,numero2) == resultado


def obtener_datos_multiplicacion():
  """ """
  return [("1/2",2,1.0),(2,4,8),(-1,2,-2)]

@pytest.mark.parametrize("numero1,numero2,resultado", obtener_datos_multiplicacion())
def test_multiplicacion(numero1,numero2,resultado):
  """

  Args:
    numero1: 
    numero2: 
    resultado: 

  Returns: True si es correcta la evaluación y False si no lo es

  """
  assert tf.multiplicacion(numero1,numero2) == resultado
