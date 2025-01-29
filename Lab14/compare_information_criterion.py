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

def calculate_log_likelihood(y, y_fit):
    """Calculate log-likelihood"""
    resid = y - y_fit
    sse = np.sum(resid**2)
    ll = -0.5 * len(y) * np.log(2 * np.pi * sse / len(y)) - 0.5 * len(y)
    return ll

def llr_test(ll_0, ll_1, df):
    """Perform LLR test using log-likelihoods"""
    llr = -2 * (ll_0 - ll_1)
    p_value = 1 - chi2.cdf(llr, df)
    return llr, p_value


def main():
    """Main function to fit polynomials and determine best order"""
    x, y, y_true = generate_data()
    orders = range(1, 10)
    aic_values = []
    bic_values = []

    for order in orders:
        y_fit, coeffs = fit_polynomial(x, y, order)
        aic = calculate_aic(y, y_fit, order + 1)
        bic = calculate_bic(y, y_fit, order + 1)
        aic_values.append(aic)
        bic_values.append(bic)

    plt.figure(figsize=(10, 5))
    plt.plot(orders, aic_values, label='AIC', marker='o')
    plt.plot(orders, bic_values, label='BIC', marker='o')
    plt.xlabel('Polynomial Order')
    plt.ylabel('Information Criterion')
    plt.title('AIC and BIC for Polynomial Fitting')
    plt.legend()
    plt.show()


### LLR test between different polynomials
    y_fit1, _ = fit_polynomial(x, y, 1)
    y_fit2, _ = fit_polynomial(x, y, 2)
    y_fit3, _ = fit_polynomial(x, y, 3)
    y_fit4, _ = fit_polynomial(x, y, 4)

    ll_1 = calculate_log_likelihood(y, y_fit1)
    ll_2 = calculate_log_likelihood(y, y_fit2)
    ll_3 = calculate_log_likelihood(y, y_fit3)
    ll_4 = calculate_log_likelihood(y, y_fit4)

    llr_1_2, p_value_1_2 = llr_test(ll_1, ll_2, 1)
    llr_2_3, p_value_2_3 = llr_test(ll_2, ll_3, 1)
    llr_3_4, p_value_3_4 = llr_test(ll_3, ll_4, 1)

    print(f"LLR for degrees 1-2: {llr_1_2:.4f}, p-value: {p_value_1_2:.4f}")
    print(f"LLR for degrees 2-3: {llr_2_3:.4f}, p-value: {p_value_2_3:.4f}")
    print(f"LLR for degrees 3-4: {llr_3_4:.4f}, p-value: {p_value_3_4:.4f}")

if __name__ == "__main__":
    main()