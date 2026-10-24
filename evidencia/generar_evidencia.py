"""Ejecuta y guarda los registros reales usados para las figuras."""
from contextlib import redirect_stdout
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from main import posiciones_pulsadas, resolver_lights_out, aplicar_pulsaciones, verificar_solucion

CARPETA = Path(__file__).parent


def imprimir_tablero(tablero):
    for fila in tablero:
        print('  ' + ' '.join(map(str, fila)))


def registrar_3x3():
    tablero = [[0, 1, 0], [1, 1, 0], [0, 0, 1]]
    solucion = resolver_lights_out(tablero)
    final = aplicar_pulsaciones(tablero, solucion)
    with open(CARPETA / 'ejecucion_3x3.txt', 'w', encoding='utf-8') as salida:
        with redirect_stdout(salida):
            print('EJECUCIÓN REAL: TABLERO 3 x 3')
            print('Tablero inicial:')
            imprimir_tablero(tablero)
            print('Vector solución:', solucion)
            print('Posiciones a pulsar:', posiciones_pulsadas(solucion, 3))
            print('Tablero final:')
            imprimir_tablero(final)
            print('Verificación:', verificar_solucion(tablero, solucion))


def registrar_pruebas():
    resultado = subprocess.run(
        [sys.executable, '-m', 'unittest', '-v'],
        cwd=CARPETA.parent, capture_output=True, text=True, check=False)
    texto = resultado.stdout + resultado.stderr
    (CARPETA / 'pruebas_automatizadas.txt').write_text(texto, encoding='utf-8')
    if resultado.returncode != 0:
        raise SystemExit('Las pruebas automatizadas fallaron.')


if __name__ == '__main__':
    registrar_3x3()
    registrar_pruebas()
    print('Registros guardados en evidencia/.')
