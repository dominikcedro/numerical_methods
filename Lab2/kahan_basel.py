"""
original_author: Dominik Cedro
date: 16.10.2024
"""
import math
import time

N_MAX = 94906266


def basel_kahan_summation(n_max, n):
    summ: float = 0.0
    compensation: float = 0.0
    num: int = 1
    n_max *= n

    start_time = time.time()

    while num <= n_max:
        temp = 1 / (num ** 2)
        y = temp - compensation
        t = summ + y
        compensation = (t - summ) - y
        summ = t
        num += 1

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"For {N_MAX} x {n}")
    print(f"Execution time for sum and number: {execution_time} seconds")
    analytical = math.pi ** 2 / 6
    print(f"Analytical value is: {analytical}")
    print(summ)
    relative_percentage_difference = (
            ((analytical - summ) / analytical) * 100)
    print(f"Relative percentage difference is: {relative_percentage_difference}%")


def basel_forward_summation(n_max, n):
    summ: float = 0.0
    compensation: float = 0.0
    num: int = 1
    n_max *= n

    start_time = time.time()

    while num <= n_max:
        temp = 1 / (num ** 2)
        summ = temp+summ
        num += 1

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"For {N_MAX} x {n}")
    print(f"Execution time for sum and number: {execution_time} seconds")
    analytical = math.pi ** 2 / 6
    print(f"Analytical value is: {analytical}")
    print(summ)
    relative_percentage_difference = (
            ((analytical - summ) / analytical) * 100)
    print(f"Relative percentage difference is: {relative_percentage_difference}%")

if __name__ == "__main__":
    # basel_kahan_summation(N_MAX, 1)
    # basel_kahan_summation(N_MAX, 2)
    # basel_kahan_summation(N_MAX, 4)
    # basel_kahan_summation(N_MAX, 8)
    # basel_kahan_summation(N_MAX, 10)
    # basel_kahan_summation(N_MAX, 16)
    #
    basel_forward_summation(N_MAX, 1)
    basel_forward_summation(N_MAX, 2)
    basel_forward_summation(N_MAX, 4)
    basel_forward_summation(N_MAX, 8)
    basel_forward_summation(N_MAX, 10)
    basel_forward_summation(N_MAX, 16)

