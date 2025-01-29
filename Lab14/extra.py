import numpy as np
import statsmodels.api as sm

def generate_data():
    """Generate data with Gaussian noise"""
    np.random.seed(0)
    x = np.linspace(-5, 5, 100)
    y_true = 2 + 0.5 * x**2 + 0.1 * x**3
    y = y_true + np.random.normal(0, 2, size=x.shape)
    return x, y, y_true

def fit_polynomial(x, y, order):
    """Fit polynomial of given order using statsmodels"""
    X = np.vander(x, order + 1)
    model = sm.OLS(y, X).fit()
    return model

def main():
    """Main function to fit polynomials and determine best order"""
    x, y, y_true = generate_data()

    model1 = fit_polynomial(x, y, 1)
    model2 = fit_polynomial(x, y, 2)
    model3 = fit_polynomial(x, y, 3)
    model4 = fit_polynomial(x, y, 4)

    llr_1_2 = model1.compare_lr_test(model2)
    llr_2_3 = model2.compare_lr_test(model3)
    llr_3_4 = model3.compare_lr_test(model4)

    print(f"LLR for degrees 1-2: {llr_1_2[0]:.4f}, p-value: {llr_1_2[1]:.4f}")
    print(f"LLR for degrees 2-3: {llr_2_3[0]:.4f}, p-value: {llr_2_3[1]:.4f}")
    print(f"LLR for degrees 3-4: {llr_3_4[0]:.4f}, p-value: {llr_3_4[1]:.4f}")

if __name__ == "__main__":
    main()