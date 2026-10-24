"""Resolución de Lights Out mediante eliminación gaussiana sobre GF(2)."""


def construir_sistema(tablero):
    """Construye la matriz A y el vector b del sistema Ax=b módulo 2.

    Cada variable representa una pulsación y cada fila representa una luz.
    La fila indica qué pulsaciones cambian el estado de esa luz.
    """
    n = len(tablero)
    if n == 0 or any(len(fila) != n for fila in tablero):
        raise ValueError('El tablero debe ser cuadrado y no vacío.')
    if any(valor not in (0, 1) for fila in tablero for valor in fila):
        raise ValueError('El tablero solo puede contener ceros y unos.')

    m = n * n
    A = [[0] * m for _ in range(m)]
    b = [tablero[f][c] for f in range(n) for c in range(n)]

    for f in range(n):
        for c in range(n):
            i = f * n + c
            for df, dc in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                nf, nc = f + df, c + dc
                if 0 <= nf < n and 0 <= nc < n:
                    j = nf * n + nc
                    A[i][j] = 1
    return A, b


def eliminacion_gaussiana(A, b):
    """Resuelve Ax=b sobre GF(2) usando operaciones binarias.

    La única operación elemental utilizada es Fi <- Fi + Fj módulo 2,
    que equivale a aplicar XOR componente a componente. Si el sistema es
    incompatible devuelve None; si tiene variables libres, fija esas
    variables en cero y devuelve una solución particular.
    """
    if len(A) != len(b) or not A or any(len(fila) != len(A[0]) for fila in A):
        raise ValueError('Las dimensiones de A y b no son compatibles.')
    m, columnas = len(b), len(A[0])
    M = [[valor % 2 for valor in fila] + [b[i] % 2]
         for i, fila in enumerate(A)]
    pivotes = []
    fila_pivote = 0

    for columna in range(columnas):
        if fila_pivote == m:
            break
        # Si falta el pivote, sumamos una fila inferior en vez de intercambiarla.
        if M[fila_pivote][columna] == 0:
            fuente = next((f for f in range(fila_pivote + 1, m)
                           if M[f][columna]), None)
            if fuente is not None:
                M[fila_pivote] = [a ^ b for a, b in zip(M[fila_pivote], M[fuente])]
        if M[fila_pivote][columna] == 0:
            continue
        # Eliminamos el pivote de las demás filas para obtener forma reducida.
        for f in range(m):
            if f != fila_pivote and M[f][columna]:
                M[f] = [a ^ b for a, b in zip(M[f], M[fila_pivote])]
        pivotes.append(columna)
        fila_pivote += 1
        if fila_pivote == m:
            break

    # Una fila 0...0 | 1 significa 0 = 1, por lo que no hay solución.
    for fila in M:
        if not any(fila[:-1]) and fila[-1] == 1:
            return None

    x = [0] * columnas  # Variables libres = 0; una solución posible.
    for i, columna in enumerate(pivotes):
        x[columna] = M[i][-1]
    return x


def resolver_lights_out(tablero):
    """Resuelve un tablero y devuelve el vector de pulsaciones o None."""
    A, b = construir_sistema(tablero)
    return eliminacion_gaussiana(A, b)


def verificar_solucion(tablero, solucion):
    """Comprueba que una solución propuesta satisface el sistema completo."""
    if solucion is None:
        return False
    A, b = construir_sistema(tablero)
    if len(solucion) != len(b) or any(x not in (0, 1) for x in solucion):
        return False
    return all((sum(a * x for a, x in zip(fila, solucion)) % 2) == bi
               for fila, bi in zip(A, b))


def aplicar_pulsaciones(tablero, solucion):
    """Aplica las pulsaciones y devuelve el estado final del tablero.

    El vector se recorre en orden por filas y cada valor 1 cambia la luz
    pulsada y sus vecinas ortogonales.
    """
    n = len(tablero)
    if len(solucion) != n * n:
        raise ValueError('La solución debe tener n*n valores.')
    resultado = [fila[:] for fila in tablero]
    for i, pulsada in enumerate(solucion):
        if pulsada:
            f, c = divmod(i, n)
            for df, dc in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                nf, nc = f + df, c + dc
                if 0 <= nf < n and 0 <= nc < n:
                    resultado[nf][nc] ^= 1
    return resultado


def posiciones_pulsadas(solucion, n):
    """Convierte el vector en coordenadas (fila, columna), comenzando en 1."""
    return [(i // n + 1, i % n + 1) for i, valor in enumerate(solucion) if valor]


if __name__ == '__main__':
    ejemplos = [
        [[0, 1, 0], [1, 1, 0], [0, 0, 1]],
        [[0, 0], [0, 0]],
        [[1, 1], [1, 1]],
    ]
    for tablero in ejemplos:
        solucion = resolver_lights_out(tablero)
        print('Tablero:', tablero)
        print('Solución:', solucion)
        print('Verificada:', verificar_solucion(tablero, solucion))
        print()
