from sympy import *
from numpy import *
import sys

Z = Symbol('Z')  # Número atómico del átomo

class HF:
    """
    Clase para resolver las ecuaciones de Hartree-Fock de forma iterativa.
    """
    def __init__(self, N, basis, Z_value, first_C='identity'):
        """
        N es el número de partículas en el sistema y basis es la base de partícula única para el sistema.
        """
        self.N = N  # Número de partículas en el sistema
        self.basis = basis  # Base de partícula única para el sistema
        self.Z_value = Z_value  # Número atómico del átomo
        self.n = len(basis)  # Número de estados de base de partícula única
        self.ek = zeros((self.n,))  # Nuevas energías de partícula única
        self.E = 0  # Energía total

        # Configurar la primera matriz de coeficientes a utilizar
        if first_C == 'identity':
            self.C = eye(self.n)
        elif first_C == 'zero':
            self.C = zeros((self.n, self.n))
        elif first_C == 'rand':
            self.C = random.rand(self.n, self.n)
        else:
            print("Argumento first_C no reconocido.")
            print("Valores válidos son: 'identity', 'zero', 'rand'")
            sys.exit(1)

        self.h_HF = zeros((self.n, self.n))  # Matriz HF

        self.assemble_HF_matrix()  # Configurar la matriz HF para C = I

    def h_0(self, p, q, Z):
        """Toma los valores enteros de los estados y devuelve el elemento de matriz de dos cuerpos
        asimétrico <pq||rs>."""
        n1, s1 = self.basis[p]
        n2, s2 = self.basis[q]
        if n1 != n2 or s1 != s2:
            return 0
        else:
            return -Z**2 / (2 * n1**2)

    def assemble_HF_matrix(self):
        """
        Ensambla la matriz HF a partir de la matriz de coeficientes.
        """
        n, N = self.n, self.N
        C = self.C
        for a in range(n):
            for g in range(n):
                s = self.h_0(a, g, self.Z_value)
                for p in range(N):
                    for b in range(n):
                        for d in range(n):
                            s += C[p, b]*C[p, d]*self.h_0(b, d, self.Z_value)
                self.h_HF[a, g] = s.subs(Z, self.Z_value)

    def reorder_coefficients(self):
        ek, C = self.ek, self.C
        # Ordenar los eigenvalores y la matriz de coeficientes usando numpy.argsort
        indices = argsort(ek)
        ek = ek[indices]
        C = C[:, indices]
        self.ek, self.C = ek, C.T

    def calc_energy(self):
        """
        Calcula la energía del estado fundamental a partir de la matriz de coeficientes actual.
        """
        n, N = self.n, self.N
        C = self.C
        e = 0
        for p in range(N):
            for a in range(n):
                for b in range(n):
                    e += C[p, a]*C[p, b]*self.h_0(a, b, self.Z_value)
        self.E = e.subs(Z, self.Z_value).evalf()
        return self.E

    def solve(self, tol=1e-6, max_iters=40):
        iterations = 0
        n, N = self.n, self.N
        Ep = 0
        ekp = zeros((self.n,))
        while iterations < max_iters:
            iterations += 1
            # Encontrar los eigenvalores y eigenvectores de la matriz HF
            self.ek, self.C = linalg.eig(self.h_HF)
            # Reordenar los eigenvalores y eigenvectores
            self.reorder_coefficients()
            # Ensamblar la nueva matriz HF
            self.assemble_HF_matrix()
            # Probar la tolerancia del eigenvalor más bajo
            error = sum(abs(ekp - self.ek[0]))
            if error < tol:
                print("Convergencia alcanzada después de %d iteraciones." % iterations)
                return
            Ep = self.E
            ekp = self.ek[0]
        print("Falló en alcanzar convergencia en %d iteraciones." % iterations)

# Datos de entrada
N = int(input("Ingrese el número de partículas: "))
Z_value = int(input("Ingrese el número atómico del átomo: "))

basis = []
n_basis = int(input("Ingrese el número de estados de base de partícula única: "))
for i in range(n_basis):
    n = int(input(f"Ingrese n para el estado {i+1}: "))
    s = int(input(f"Ingrese s para el estado {i+1}: "))
    basis.append((n, s))

solver = HF(N, basis, Z_value, first_C='identity')
solver.solve(max_iters=100)

print("Matriz HF:")
print(solver.h_HF)

print("Energía del estado fundamental:")
print(solver.calc_energy())

