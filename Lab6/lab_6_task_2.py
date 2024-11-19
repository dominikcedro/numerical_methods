def bisection_method(flow_function, g, t, L, target_v, xl, xu, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        xr = (xl + xu) / 2
        f_xl = flow_function(g, xl, t, L) - target_v
        f_xr = flow_function(g, xr, t, L) - target_v

        if abs(f_xr) < tol:
            return xr

        if f_xl * f_xr < 0:
            xu = xr
        else:
            xl = xr

    return xr


L = 5
t = 3
g = 9.81
target_v = 4

# Initial guesses for H
xl = 0
xu = 50

optimal_H = bisection_method(flow_function, g, t, L, target_v, xl, xu)