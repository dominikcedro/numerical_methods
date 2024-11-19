"""
author: Dominik Cedro
date: 11.10.2024
"""
import math
from icecream import ic

def calculate_power_e(power):
    ic('for power', power)
    x = power
    e_calc_total = 1
    e_math = math.e ** x
    n = 1
    factorial = 1
    while True:
        factorial *= n
        e_calc_next = (x**n)/factorial
        e_calc_total += e_calc_next
        n += 1
        if (e_calc_total + e_calc_next) == e_calc_total:
            ic('break statement for ', e_calc_total)
            break

    ic('e from .math is ',e_math)
    ic('e calculated is ', e_calc_total)
    relative_percentage_difference = (((e_math - e_calc_total) / e_math) * 100)
    ic( relative_percentage_difference)
    ic('')
    return e_calc_total, e_math

list_of_powers = [ 1, 0.1, 20, -20]
for power in list_of_powers:
    calculate_power_e(power)

"""OUTPUT 
'for power', power: 1
ic| 'break statement for ', e_calc_total: 2.7182818284590455
ic| 'e from .math is ', e_math: 2.718281828459045
ic| 'e calculated is ', e_calc_total: 2.7182818284590455
ic| relative_percentage_difference: -1.6337129034990843e-14
ic| ''
ic| 'for power', power: 0.1
ic| 'break statement for ', e_calc_total: 1.1051709180756473
ic| 'e from .math is ', e_math: 1.1051709180756477
ic| 'e calculated is ', e_calc_total: 1.1051709180756473
ic| relative_percentage_difference: 4.0182853401836004e-14
ic| ''
ic| 'for power', power: 20
ic| 'break statement for ', e_calc_total: 485165195.40979016
ic| 'e from .math is ', e_math: 485165195.40978974
ic| 'e calculated is ', e_calc_total: 485165195.40979016
ic| relative_percentage_difference: -8.599803064507199e-14
ic| ''
ic| 'for power', power: -20
ic| 'break statement for ', e_calc_total: 5.47810291652921e-10
ic| 'e from .math is ', e_math: 2.06115362243856e-09
ic| 'e calculated is ', e_calc_total: 5.47810291652921e-10
ic| relative_percentage_difference: 73.42215128027166
ic| ''
"""