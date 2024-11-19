"""
original_author: Dominik Cedro
date: 09.10.2024
"""
import math
import time

N_MAX = 94906266
def backwards_summation(N_MAX,n):

    num: int = N_MAX
    full_sum: float = 0

    start_time = time.time()

    while num > 0:
        partial_sum = 1 / (num ** 2)
        full_sum += partial_sum
        num -= 1

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Results for n={n}")
    print(f"Execution time for sum and number: {execution_time} seconds")
    analytical = math.pi**2 / 6
    print(f"Analytical value is: {analytical}")
    print(f"Total sum is: {full_sum}")
    relative_percentage_difference = (
            ((analytical - full_sum) / analytical) * 100)
    print(f"Relative percentage difference is:"
        f" {relative_percentage_difference:.10f}%")

backwards_summation(N_MAX,1)
backwards_summation(2*N_MAX,2)
backwards_summation(4*N_MAX,4)
backwards_summation(8*N_MAX,8)
backwards_summation(10*N_MAX,10)
backwards_summation(16*N_MAX,16)


""" OUTPUT
Results for n=1
Execution time for sum and number: 9.817232370376587 seconds
Analytical value is: 1.6449340668482264
Total sum is: 1.6449340563115145
Relative percentage difference is: 0.0000006406%
Results for n=2
Execution time for sum and number: 33.84731388092041 seconds
Analytical value is: 1.6449340668482264
Total sum is: 1.6449340615798704
Relative percentage difference is: 0.0000003203%
Results for n=4
Execution time for sum and number: 81.29956865310669 seconds
Analytical value is: 1.6449340668482264
Total sum is: 1.6449340642140484
Relative percentage difference is: 0.0000001601%
Results for n=8
Execution time for sum and number: 158.62014770507812 seconds
Analytical value is: 1.6449340668482264
Total sum is: 1.6449340655311373
Relative percentage difference is: 0.0000000801%

"""