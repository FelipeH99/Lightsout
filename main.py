"""Resolución de Lights Out mediante eliminación gaussiana sobre GF(2)."""


def construir_sistema(tablero):
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
    """Resuelve Ax=b sobre GF(2); devuelve una solución o None."""
    m = len(b)
    M = [fila[:] + [valor] for fila, valor in zip(A, b)]
    pivotes = []
    fila_pivote = 0

    for columna in range(m):
        # Para este sistema, si no hay pivote en la posición actual,
        # buscamos otra fila. El intercambio es solo una medida de robustez.
        candidata = next((f for f in range(fila_pivote, m) if M[f][columna]), None)
        if candidata is None:
            continue
        if candidata != fila_pivote:
            M[fila_pivote], M[candidata] = M[candidata], M[fila_pivote]
        for f in range(m):
            if f != fila_pivote and M[f][columna]:
                M[f] = [a ^ b for a, b in zip(M[f], M[fila_pivote])]
        pivotes.append(columna)
        fila_pivote += 1
        if fila_pivote == m:
            break

    for fila in M:
        if not any(fila[:-1]) and fila[-1] == 1:
            return None

    x = [0] * m  # Variables libres = 0; una solución posible.
    for i, columna in enumerate(pivotes):
        x[columna] = M[i][-1]
    return x


def resolver_lights_out(tablero):
    A, b = construir_sistema(tablero)
    return eliminacion_gaussiana(A, b)


def verificar_solucion(tablero, solucion):
    if solucion is None:
        return False
    A, b = construir_sistema(tablero)
    if len(solucion) != len(b) or any(x not in (0, 1) for x in solucion):
        return False
    return all((sum(a * x for a, x in zip(fila, solucion)) % 2) == bi
               for fila, bi in zip(A, b))


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
