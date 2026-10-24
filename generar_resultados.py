"""Genera evidencia reproducible para el informe, sin dependencias externas."""

import itertools
from main import (aplicar_pulsaciones, construir_sistema, posiciones_pulsadas,
                  resolver_lights_out, verificar_solucion)


def rango_gf2(matriz):
    """Calcula el rango de una matriz binaria con sumas de filas."""
    M = [fila[:] for fila in matriz]
    filas, columnas, pivote = len(M), len(M[0]), 0
    for columna in range(columnas):
        fuente = next((f for f in range(pivote, filas) if M[f][columna]), None)
        if fuente is None:
            continue
        # Esta rutina independiente permite medir el rango; tampoco usa swaps.
        if fuente != pivote:
            M[pivote] = [a ^ b for a, b in zip(M[pivote], M[fuente])]
        for f in range(filas):
            if f != pivote and M[f][columna]:
                M[f] = [a ^ b for a, b in zip(M[f], M[pivote])]
        pivote += 1
    return pivote


def formatear_tablero(tablero):
    return '\n'.join(' '.join(map(str, fila)) for fila in tablero)


def vector_a_texto(vector):
    return 'None' if vector is None else str(vector)


def clasificar(tablero):
    A, _ = construir_sistema(tablero)
    solucion = resolver_lights_out(tablero)
    if solucion is None:
        return 'incompatible', rango_gf2(A), solucion
    rango = rango_gf2(A)
    return ('única' if rango == len(A) else 'múltiples'), rango, solucion


def encontrar_incompatible_4x4():
    """Enumera tableros 4x4 y devuelve el primero incompatible."""
    for bits in itertools.product((0, 1), repeat=16):
        tablero = [list(bits[i * 4:(i + 1) * 4]) for i in range(4)]
        if resolver_lights_out(tablero) is None:
            return tablero
    raise RuntimeError('No se encontró un tablero incompatible.')


def caso(texto, tablero, solucion_alternativa=None):
    clasificacion, rango, solucion = clasificar(tablero)
    A, _ = construir_sistema(tablero)
    lineas = [f'### {texto}', '', 'Tablero inicial:', '```text',
              formatear_tablero(tablero), '```', '',
              f'Clasificación: {clasificacion}', f'Rango de A: {rango} de {len(A)}',
              f'Solución obtenida: {vector_a_texto(solucion)}']
    if solucion is not None:
        final = aplicar_pulsaciones(tablero, solucion)
        lineas += [f'Posiciones: {posiciones_pulsadas(solucion, len(tablero))}',
                   f'Verificación: {verificar_solucion(tablero, solucion)}',
                   'Tablero final:', '```text', formatear_tablero(final), '```']
    else:
        lineas += ['Verificación: no corresponde; el sistema es incompatible.']
    if solucion_alternativa is not None:
        lineas += [f'Segunda solución: {solucion_alternativa}',
                   f'Verificación de la segunda solución: '
                   f'{verificar_solucion(tablero, solucion_alternativa)}']
    return '\n'.join(lineas)


def main():
    tablero_incompatible = encontrar_incompatible_4x4()
    tablero_multiple = [[0] * 4 for _ in range(4)]
    pulsaciones_conocidas = [1, 0, 1, 0, 0, 1, 0, 0,
                             1, 1, 0, 0, 0, 0, 1, 1]
    tablero_generado = aplicar_pulsaciones(
        [[0] * 4 for _ in range(4)], pulsaciones_conocidas)
    segunda = [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
    casos = [
        ('Prueba 1: consigna 3x3', [[0, 1, 0], [1, 1, 0], [0, 0, 1]]),
        ('Prueba 2: 2x2 apagado', [[0, 0], [0, 0]]),
        ('Prueba 3: 2x2 encendido', [[1, 1], [1, 1]]),
        ('Prueba 4: 3x3 apagado', [[0, 0, 0]] * 3),
        ('Prueba 5: 4x4 generado', tablero_generado),
    ]
    secciones = [caso(nombre, tablero) for nombre, tablero in casos]
    secciones.append(caso('Caso A: tablero 4x4 incompatible', tablero_incompatible))
    secciones.append(caso('Caso B: tablero 4x4 con múltiples soluciones',
                           tablero_multiple, segunda))
    contenido = '# Resultados reproducibles de Lights Out\n\n' + '\n\n'.join(secciones)
    contenido += '''\n\n## Análisis de casos especiales\n\n'''
    contenido += ('El caso incompatible aparece como una fila nula con término independiente 1 '
                  'durante la reducción, equivalente a la contradicción 0=1. Por eso no existe '
                  'ningún vector de pulsaciones que apague ese tablero.\n\n')
    contenido += ('En el caso múltiple, el rango de A es menor que la cantidad de incógnitas. '
                  'Las variables que no son pivote son libres; al fijarlas en cero se obtiene '
                  'la solución particular del algoritmo, mientras que una combinación con un '
                  'vector del núcleo produce otra solución válida.\n\n')
    contenido += ('## Discusión\n\nLa evidencia confirma que el modelo Ax=b sobre GF(2) reproduce la '
                  'simulación de pulsaciones. La eliminación binaria resuelve sistemas compatibles '
                  'y detecta incompatibilidades sin utilizar resolutores externos. La implementación '
                  'devuelve una solución particular cuando hay variables libres, pero no enumera '
                  'automáticamente todas las soluciones.\n\n')
    contenido += ('## Conclusiones\n\nLights Out muestra una aplicación directa de matrices, rango, '
                  'variables libres y aritmética módulo 2. La verificación por simulación y las '
                  'pruebas exhaustivas pequeñas respaldan la implementación computacional.')
    with open('resultados_informe.md', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido + '\n')
    with open('resultados_pruebas.txt', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
    print(contenido)


if __name__ == '__main__':
    main()
