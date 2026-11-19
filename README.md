# Lights Out · Álgebra lineal aplicada

Juego de luces con un solucionador basado en eliminación gaussiana sobre **GF(2)**: cada pulsación alterna una celda y sus vecinas, y el objetivo es apagar el tablero.

**Python · JavaScript · HTML/CSS · unittest**

## Probarlo

Abrí [`index.html`](index.html) en un navegador, o serví la carpeta:

```sh
git clone https://github.com/FelipeH99/Lightsout.git
cd Lightsout
python3 -m http.server 8080
```

Entrá en `http://localhost:8080`. Podés elegir tamaño, cambiar luces, generar un tablero y pedir una solución. Los tableros aleatorios de la interfaz se construyen mediante pulsaciones válidas y son resolubles.

## Algoritmo y validación

El problema se expresa como `A · x = b (mod 2)`. La matriz representa qué luces cambia cada pulsación. El solucionador usa sumas de filas sin intercambiarlas; devuelve `None` si el sistema es incompatible. Si existen variables libres, las fija en cero para obtener una solución, que no necesariamente minimiza la cantidad de pulsaciones.

```sh
python3 main.py
python3 -m unittest -v
```

No requiere paquetes externos para el solucionador ni sus pruebas.

## Evidencia y documentación

- [Informe](InformeLightsout.pdf): desarrollo del trabajo.
- [Resultados](resultados_informe.md): casos y análisis de rangos.
- [`test_lights_out.py`](test_lights_out.py): pruebas del solucionador.
- [`evidencia/`](evidencia/): registros e imágenes de ejecución.

`python3 generar_resultados.py` regenera resultados. Los scripts de imágenes en PowerShell son opcionales y no se necesitan para jugar ni ejecutar las pruebas.

## Qué aporta al perfil

Un ejemplo acotado de modelado matemático, implementación de algoritmos y verificación automática. Complementa los proyectos de APIs e integración con una muestra de fundamentos.
