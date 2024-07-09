from sympy import symbols, exp, integrate, factorial, sqrt
from scipy.linalg import eig
import numpy as np

r, r1, r2, zeta, zeta1, zeta2 = symbols("r, r1, r2, zeta, zeta1, zeta2")
n = symbols('n', integer=True)

def STO(zeta, n, r=r):
    return (2*zeta)**n*(2*zeta/factorial(2*n))**(1/2)*r**(n-1)*exp(-zeta*r)

def S_int(f1, f2):
    return integrate(f1*f2*r*r, (r, 0, float("inf")))

def H_int(f1, f2, Z):
    return integrate(f1*(-((1/2)*(1/r)*((r*f2).diff(r)).diff(r))-(Z/r)*f2)*r*r, (r, 0, float("inf")))

def H_matrix(fs, Z):
    H = np.zeros((len(fs), len(fs)))
    for i in range(len(fs)):
        for j in range(len(fs)):
            H[i, j] = H_int(fs[i], fs[j], Z)
    return H

def S_matrix(fs):
    S = np.zeros((len(fs), len(fs)))
    for i in range(len(fs)):
        for j in range(len(fs)):
            S[i, j] = S_int(fs[i], fs[j])
    return S

def diagonalize(H, S):
    eigenvalues, eigenvectors = eig(H, S)
    eigenvalues_sorted = np.sort(eigenvalues.real)
    return eigenvalues_sorted, eigenvectors

def iterate_approximations(fs, Z, max_iterations=10):
    H = H_matrix(fs, Z)
    S = S_matrix(fs)
    previous_energy = float('inf')
    current_energy = 0

    for iteration in range(max_iterations):
        eigenvalues, eigenvectors = diagonalize(H, S)
        current_energy = eigenvalues[0]
        
        if abs(current_energy - previous_energy) < 1e-5:
            break

        previous_energy = current_energy

        F = np.zeros(H.shape)
        for i in range(len(fs)):
            for j in range(len(fs)):
                for k in range(len(fs)):
                    F[i, j] += H[i, k] * eigenvectors[k, j]

        H = H + F

    return current_energy

zetas = [[4.61679, 1], [2.46167, 1], [1.96299, 2], [0.67198, 2]]
Z = 3

f1 = STO(zetas[0][0], zetas[0][1])
f2 = STO(zetas[1][0], zetas[1][1])
f3 = STO(zetas[2][0], zetas[2][1])
f4 = STO(zetas[3][0], zetas[3][1])
fs = [f1, f2, f3, f4]

ground_state_energy = iterate_approximations(fs, Z)

print("Energía del estado fundamental: {:.5f}".format(ground_state_energy))
