import numpy as np
import physconst as pc

H = 100
a = np.pi / 3
b = 30

v = np.sqrt(pc.g * H * (np.tan(b))**2 / 2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))) 
print(v)

T = 200
E = 300

N = 2 / np.pi * pc.h / (pc.k * T)**(3 / 2) * pc.e**(-E / pc.k * T) * E**(T / 2)
print(N)