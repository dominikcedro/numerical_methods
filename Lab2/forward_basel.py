"""
original_author: Dominik Cedro
date: 02.10.2024
"""
import math
import time

full_sum: float = 0
partial_sum: float = 0
num: int = 1

start_time = time.time()

while True:
    partial_sum = 1/(num**2)
    if (partial_sum + full_sum) == full_sum:
        print(f"Number is {num}")
        print(f"Total sum is {full_sum}")
        break
    full_sum += partial_sum
    num += 1

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for sum and number: {execution_time} seconds")

analytical = math.pi**2 / 6
print(f"Analytical value is: {analytical}")

relative_percentage_difference = (
        ((analytical - full_sum) / analytical) * 100)
print(f"Relative percentage difference is:"
      f" {relative_percentage_difference}%")
