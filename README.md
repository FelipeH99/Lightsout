# Lights Out

El programa resuelve el juego Lights Out usando sistemas lineales sobre los
ceros y unos. El archivo `main.py` construye la matriz, aplica eliminación
gaussiana módulo 2 y comprueba la solución encontrada.

La eliminación usa sumas de filas (`Fi <- Fi + Fj`) y no intercambia filas.
Si el sistema no tiene solución, la función devuelve `None`. Cuando hay
variables libres, devuelve una solución posible fijándolas en cero.

## Ejecutar el programa

```text
python main.py
python -m unittest -v
python generar_resultados.py
python evidencia\generar_evidencia.py
powershell -ExecutionPolicy Bypass -File evidencia\generar_imagenes.ps1
```

`generar_resultados.py` busca un caso incompatible, calcula rangos sobre GF(2)
y actualiza los archivos de resultados.

Los scripts de `evidencia/` guardan los registros de ejecución y generan las
imágenes que se pueden insertar en el informe.

## Interfaz web

Abrí `index.html` directamente en un navegador. Permite elegir el tamaño,
encender y apagar luces, generar un tablero aleatorio, reiniciar y mostrar
las posiciones que propone el mismo algoritmo de eliminación gaussiana.
El botón “Aleatorio” aplica pulsaciones aleatorias a un tablero apagado, por
lo que todos los tableros generados desde la interfaz son resolubles.
