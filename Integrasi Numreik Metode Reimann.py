import numpy as np
import timeit

def riemann_integral(f, a, b, N):
    dx = (b - a) / N
    x = np.linspace(a + dx/2, b - dx/2, N)  # Titik tengah untuk metode Riemann
    integral = np.sum(f(x)) * dx
    return integral

def f(x):
    return 4 / (1 + x**2)

def rms_error(estimated_pi, true_pi):
    return np.sqrt(np.mean((estimated_pi - true_pi)**2))

# Nilai referensi pi
true_pi = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

for N in N_values:
    # Menggunakan timeit untuk menghitung waktu eksekusi
    time_taken = timeit.timeit(lambda: riemann_integral(f, 0, 1, N), number=1)
    
    estimated_pi = riemann_integral(f, 0, 1, N)
    error = rms_error(estimated_pi, true_pi)
    
    print(f"N = {N}")
    print(f"Estimated Pi: {estimated_pi}")
    print(f"RMS Error: {error}")
    print(f"Execution Time: {time_taken} seconds")
    print("-" * 30)