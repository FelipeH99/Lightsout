# Resultados reproducibles de Lights Out

### Prueba 1: consigna 3x3

Tablero inicial:
```text
0 1 0
1 1 0
0 0 1
```

Clasificación: única
Rango de A: 9 de 9
Solución obtenida: [0, 0, 0, 0, 1, 0, 0, 0, 1]
Posiciones: [(2, 2), (3, 3)]
Verificación: True
Tablero final:
```text
0 0 0
0 0 0
0 0 0
```

### Prueba 2: 2x2 apagado

Tablero inicial:
```text
0 0
0 0
```

Clasificación: única
Rango de A: 4 de 4
Solución obtenida: [0, 0, 0, 0]
Posiciones: []
Verificación: True
Tablero final:
```text
0 0
0 0
```

### Prueba 3: 2x2 encendido

Tablero inicial:
```text
1 1
1 1
```

Clasificación: única
Rango de A: 4 de 4
Solución obtenida: [1, 1, 1, 1]
Posiciones: [(1, 1), (1, 2), (2, 1), (2, 2)]
Verificación: True
Tablero final:
```text
0 0
0 0
```

### Prueba 4: 3x3 apagado

Tablero inicial:
```text
0 0 0
0 0 0
0 0 0
```

Clasificación: única
Rango de A: 9 de 9
Solución obtenida: [0, 0, 0, 0, 0, 0, 0, 0, 0]
Posiciones: []
Verificación: True
Tablero final:
```text
0 0 0
0 0 0
0 0 0
```

### Prueba 5: 4x4 generado

Tablero inicial:
```text
1 1 1 1
1 0 0 0
0 1 0 1
1 0 0 0
```

Clasificación: múltiples
Rango de A: 12 de 16
Solución obtenida: [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
Posiciones: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 4), (3, 1)]
Verificación: True
Tablero final:
```text
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
```

### Caso A: tablero 4x4 incompatible

Tablero inicial:
```text
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 1
```

Clasificación: incompatible
Rango de A: 12 de 16
Solución obtenida: None
Verificación: no corresponde; el sistema es incompatible.

### Caso B: tablero 4x4 con múltiples soluciones

Tablero inicial:
```text
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
```

Clasificación: múltiples
Rango de A: 12 de 16
Solución obtenida: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Posiciones: []
Verificación: True
Tablero final:
```text
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
```
Segunda solución: [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
Verificación de la segunda solución: True

## Análisis de casos especiales

El caso incompatible aparece como una fila nula con término independiente 1 durante la reducción, equivalente a la contradicción 0=1. Por eso no existe ningún vector de pulsaciones que apague ese tablero.

En el caso múltiple, el rango de A es menor que la cantidad de incógnitas. Las variables que no son pivote son libres; al fijarlas en cero se obtiene la solución particular del algoritmo, mientras que una combinación con un vector del núcleo produce otra solución válida.

## Discusión

La evidencia confirma que el modelo Ax=b sobre GF(2) reproduce la simulación de pulsaciones. La eliminación binaria resuelve sistemas compatibles y detecta incompatibilidades sin utilizar resolutores externos. La implementación devuelve una solución particular cuando hay variables libres, pero no enumera automáticamente todas las soluciones.

## Conclusiones

Lights Out muestra una aplicación directa de matrices, rango, variables libres y aritmética módulo 2. La verificación por simulación y las pruebas exhaustivas pequeñas respaldan la implementación computacional.
