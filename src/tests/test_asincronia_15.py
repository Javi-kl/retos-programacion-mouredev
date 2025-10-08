from src.asincronia_15 import (
    funcion_asincrona,
    a_function,
    b_function,
    c_function,
    d_function,
    principal_extra,
)
import pytest
import asyncio
import time


# Test 1: Verifica que la función se ejecuta correctamente
@pytest.mark.asyncio
async def test_funcion_asincrona_completa():
    """Verifica que la función termine sin errores"""

    await funcion_asincrona(1, "test")
    assert True


# test 2: Mide el tiempo de ejecución
@pytest.mark.asyncio
async def test_tiempo_ejecucion():
    inicio = time.perf_counter()
    await funcion_asincrona(2, "timer test")
    duracion = time.perf_counter() - inicio

    assert 1.9 <= duracion <= 2.5


# Test 3: verifica ejecución concurrente
@pytest.mark.asyncio
async def test_concurrencia():
    inicio = time.perf_counter()

    # Ejecuta A, B, C en paralelo
    await asyncio.gather(a_function(), b_function(), c_function())

    duracion = time.perf_counter() - inicio

    # Si fueran secuenciales: 1+2+3=6 segundos
    # En paralelo: máximo 3 segundos (la más lenta)
    assert duracion < 4  # Debe ser menos de 4 segundos


# Test 4: Verifica el orden de ejecución
@pytest.mark.asyncio
async def test_orden_ejecucion(capsys):
    """
    ¿Qué hace? Captura los prints para verificar el orden
    ¿Qué aprendes? Con gather() todas empiezan casi simultáneamente
    """
    await asyncio.gather(a_function(), b_function())

    captured = capsys.readouterr()

    # Verifica que ambas iniciaron antes de terminar
    assert "Iniciando 'A'" in captured.out
    assert "Iniciando 'B'" in captured.out


# Test 5: Test de la función principal completa
@pytest.mark.asyncio
async def test_principal_extra():
    """
    ¿Qué hace? Verifica que principal_extra se ejecute correctamente
    ¿Qué aprendes? El patrón completo de gather + await secuencial
    """
    inicio = time.perf_counter()
    await principal_extra()
    duracion = time.perf_counter() - inicio

    # gather(A,B,C) = 3s + d_function = 1s = aprox 4s total
    assert 3.5 <= duracion <= 5


# Test 6: Verifica parámetros de entrada
@pytest.mark.asyncio
async def test_parametros_funcion_asincrona():
    """
    ¿Qué hace? Prueba diferentes parámetros
    ¿Qué aprendes? Las funciones async aceptan parámetros normalmente
    """
    # Test con diferentes valores
    await funcion_asincrona(0, "Rápido")  # Sin espera
    await funcion_asincrona(1, "Normal")  # Con espera corta

    assert True  # Si no hay excepciones, el test pasa
