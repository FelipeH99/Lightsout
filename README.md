# Lights Out

Este programa modela Lights Out como `Ax=b` sobre `GF(2)`. `main.py` construye la matriz, resuelve con eliminación gaussiana binaria y verifica las pulsaciones.

La eliminación usa únicamente sumas de filas módulo 2 (`Fi <- Fi + Fj`), sin intercambiar filas. Si aparece una fila nula con término independiente 1, el sistema es incompatible y se devuelve `None`. Si hay variables libres, se fijan en cero y se devuelve una solución particular.

Ejecutar:

```text
python main.py
python -m unittest -v
python generar_resultados.py
python evidencia\generar_evidencia.py
powershell -ExecutionPolicy Bypass -File evidencia\generar_imagenes.ps1
```

`generar_resultados.py` busca por enumeración un tablero incompatible 4x4,
calcula rangos sobre GF(2) y genera `resultados_pruebas.txt` y
`resultados_informe.md` con la salida real.

Los scripts de `evidencia/` generan los registros y las imágenes PNG para el
informe. Las imágenes son representaciones tipográficas de salidas reales,
no capturas de pantalla de una terminal.

## Interfaz web

Abrí `index.html` directamente en un navegador. Permite elegir el tamaño,
encender y apagar luces, generar un tablero aleatorio, reiniciar y mostrar
las posiciones que propone el mismo algoritmo de eliminación gaussiana.
El botón “Aleatorio” aplica pulsaciones aleatorias a un tablero apagado, por
lo que todos los tableros generados desde la interfaz son resolubles.
