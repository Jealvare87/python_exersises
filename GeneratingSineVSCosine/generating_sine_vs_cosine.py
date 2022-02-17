import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi)
x1 = np.linspace(0, 2*np.pi, 201)
f = np.zeros(201)
k = np.arange(0, 2*np.pi)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.plot(x1, f)
plt.plot(x, np.arctan(x))
plt.plot(x, -np.arctan(x))
plt.xlabel("Angle [rad]")
plt.ylabel("Sin(x) And Cos(x)")
plt.axis("tight")
plt.show()