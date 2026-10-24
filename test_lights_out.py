import itertools
import unittest
from main import aplicar_pulsaciones, resolver_lights_out, verificar_solucion


class PruebasLightsOut(unittest.TestCase):
    def test_casos_basicos(self):
        for tablero in ([[0, 1, 0], [1, 1, 0], [0, 0, 1]],
                        [[0, 0], [0, 0]], [[1, 1], [1, 1]],
                        [[0, 0, 0]] * 3):
            self.assertTrue(verificar_solucion(tablero, resolver_lights_out(tablero)))

    def test_4x4_generado(self):
        p = [1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1]
        t = aplicar_pulsaciones([[0] * 4 for _ in range(4)], p)
        self.assertTrue(verificar_solucion(t, resolver_lights_out(t)))

    def test_incompatible(self):
        self.assertIsNone(resolver_lights_out([[0, 0, 0, 0]] * 3 + [[0, 0, 0, 1]]))

    def test_multiples_soluciones(self):
        p = [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
        self.assertTrue(verificar_solucion([[0] * 4 for _ in range(4)], p))

    def test_invalidas(self):
        for t in ([[0, 1], [0]], [[0, 2], [0, 1]], []):
            with self.assertRaises(ValueError): resolver_lights_out(t)

    def test_exhaustivo_1x1_2x2(self):
        for n in (1, 2):
            for bits in itertools.product((0, 1), repeat=n*n):
                t = [list(bits[i*n:(i+1)*n]) for i in range(n)]
                s = resolver_lights_out(t)
                existe = any(verificar_solucion(t, list(p))
                             for p in itertools.product((0, 1), repeat=n*n))
                self.assertEqual(s is not None, existe)
