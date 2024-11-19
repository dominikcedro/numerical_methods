import numpy as np
import math
import matplotlib.pyplot as plt

# Determine the value of machine precision
machine_precision_numpy = np.finfo(float).eps
print(f"Machine precision using numpy library: {machine_precision_numpy}")

log_spaced_numbers = list(np.logspace(-200, 200, num=100))
print(log_spaced_numbers)
values_x = [float(value) for value in log_spaced_numbers]
print("values x")
print(values_x)
# Calculate the next representable floating-point number for each value
values_y = [math.nextafter(delta, math.inf) for delta in values_x]
print("values y")
print(values_y)
# Calculate the delta (Δx) for each number
delta_values = [y - x for x, y in zip(values_x, values_y)]
print(" delta values ")
print(delta_values)

# tickx = np.array()
x_ticks = np.arange(len(values_x))


plt.figure(figsize=(10, 6))
plt.plot(values_x,values_y, color='r')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Values X')
plt.ylabel('Delta (Δx)')
plt.title('Delta (Δx) as a Function of X (Log-Log Scale)')
plt.grid(True)
plt.show()

relative_error = [delta / x for x, delta in zip(values_x, delta_values)]
print(" rel error values ")
print(relative_error)

plt.figure(figsize=(10, 6))
plt.plot(values_x, relative_error, color='r', linestyle='-')
# plt.plot(values_x, relative_error, color='black')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Values X')
plt.ylabel('Relative Error (δx)')
plt.title('Relative Error (δx) as a Function of X (Log-Log Scale)')
plt.grid(True)
plt.show()
