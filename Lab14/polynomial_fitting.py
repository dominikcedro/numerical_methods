# File: polynomial_fitting.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from sklearn.metrics import mean_squared_error

def generate_data():
    """Generate data with Gaussian noise"""
    np.random.seed(0)
    x = np.linspace(-5, 5, 100)
    y_true = 2 + 0.5 * x**2 + 0.1 * x**3
    y = y_true + np.random.normal(0, 2, size=x.shape)
    return x, y, y_true

def fit_polynomial(x, y, order):
    """Fit polynomial of given order"""
    coeffs = np.polyfit(x, y, order)
    p = np.poly1d(coeffs)
    y_fit = p(x)
    return y_fit, coeffs

def calculate_aic(y, y_fit, k):
    """Calculate AIC"""
    resid = y - y_fit
    sse = np.sum(resid**2)
    aic = 2 * k + len(y) * np.log(sse / len(y))
    return aic

def calculate_bic(y, y_fit, k):
    """Calculate BIC"""
    resid = y - y_fit
    sse = np.sum(resid**2)
    bic = np.log(len(y)) * k + len(y) * np.log(sse / len(y))
    return bic

def llr_test(y, y_fit1, y_fit2, k1, k2):
    """Perform LLR test"""
    sse1 = np.sum((y - y_fit1)**2)
    sse2 = np.sum((y - y_fit2)**2)
    llr = (sse1 - sse2) / (k2 - k1)
    p_value = 1 - chi2.cdf(llr, k2 - k1)
    return llr, p_value

def main():
    """Main function to fit polynomials and determine best order"""
    x, y, y_true = generate_data()
    orders = range(1, 10)
    aic_values = []
    bic_values = []
    llr_values = []
    p_values = []
    mse_values = []

    for order in orders:
        y_fit, coeffs = fit_polynomial(x, y, order)
        aic = calculate_aic(y, y_fit, order + 1)
        bic = calculate_bic(y, y_fit, order + 1)
        mse = mean_squared_error(y, y_fit)
        aic_values.append(aic)
        bic_values.append(bic)
        mse_values.append(mse)

        if order > 1:
            llr, p_value = llr_test(y, y_fit_prev, y_fit, order, order + 1)
            llr_values.append(llr)
            p_values.append(p_value)

        y_fit_prev = y_fit

    best_order_aic = orders[np.argmin(aic_values)]
    best_order_bic = orders[np.argmin(bic_values)]
    best_order_llr = orders[np.argmax(np.array(p_values) < 0.05) + 1]
    best_order_mse = orders[np.argmin(mse_values)]

    print(f"Best order based on AIC: {best_order_aic}")
    print(f"Best order based on BIC: {best_order_bic}")
    print(f"Best order based on LLR: {best_order_llr}")
    print(f"Best order based on MSE: {best_order_mse}")

    plt.scatter(x, y, label='Data with noise')
    plt.plot(x, y_true, label='True polynomial', color='black')
    for order in [best_order_aic, best_order_bic, best_order_llr, best_order_mse]:
        y_fit, _ = fit_polynomial(x, y, order)
        plt.plot(x, y_fit, label=f'Fitted polynomial order {order}')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynomial Fitting with Different Orders')
    plt.show()

if __name__ == "__main__":
    main()