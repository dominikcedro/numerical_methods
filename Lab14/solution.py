import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression

def saturation_growth_rate_model(x, alpha, betha):
    """Saturation growth rate model"""
    return alpha * (x / (betha + x))

def power_equation(x, alpha, betha):
    """Power equation model"""
    return alpha * x ** betha

def exponential_model(x, alpha, betha):
    """Exponential model"""
    return alpha * np.exp(betha * x)

def linearize_saturation_growth_rate(x, y):
    """Linearize saturation growth rate model"""
    return 1 / x, 1 / y

def linearize_power_equation(x, y):
    """Linearize power equation model"""
    return np.log10(x), np.log10(y)

def linearize_exponential_model(x, y):
    """Linearize exponential model"""
    return x, np.log(y)

def plot_data(x, y, y_fit, label, title):
    """Plot data and fitted model"""
    plt.scatter(x, y, color='black', label='Data points')
    plt.plot(x, y_fit, label=label, color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title(title)
    plt.show()

def main():
    """Main function to fit models and plot results"""
    x = np.array([0.75, 2, 3, 4, 6, 8, 8.5])
    y = np.array([1.2, 1.95, 2, 2.4, 2.5, 2.7, 2.6])

    # Fit and plot saturation growth rate model
    popt_saturation, _ = curve_fit(saturation_growth_rate_model, x, y)
    y_saturation_fit = saturation_growth_rate_model(x, *popt_saturation)
    print(f"Saturation Growth Rate Model: alpha = {popt_saturation[0]:.4f}, betha = {popt_saturation[1]:.4f}")
    plot_data(x, y, y_saturation_fit, label="Saturation Growth Rate Model", title="Saturation Growth Rate Model")

    # Fit and plot power equation model
    popt_power, _ = curve_fit(power_equation, x, y)
    y_power_fit = power_equation(x, *popt_power)
    print(f"Power Equation Model: alpha = {popt_power[0]:.4f}, betha = {popt_power[1]:.4f}")
    plot_data(x, y, y_power_fit, label="Power Equation Model", title="Power Equation Model")

    # Fit and plot exponential model
    popt_exponential, _ = curve_fit(exponential_model, x, y)
    y_exponential_fit = exponential_model(x, *popt_exponential)
    print(f"Exponential Model: alpha = {popt_exponential[0]:.4f}, betha = {popt_exponential[1]:.4f}")
    plot_data(x, y, y_exponential_fit, label="Exponential Model", title="Exponential Model")

    x_lin, y_lin = linearize_saturation_growth_rate(x, y)
    reg = LinearRegression().fit(x_lin.reshape(-1, 1), y_lin)
    alpha_saturation = 1 / reg.intercept_
    betha_saturation = reg.coef_[0] * alpha_saturation
    print(f"Linearized Saturation Growth Rate Model: alpha = {alpha_saturation:.4f}, betha = {betha_saturation:.4f}")
    plot_data(x_lin, y_lin, reg.predict(x_lin.reshape(-1, 1)), label="Linearized Saturation Growth Rate Model", title="Linearized Saturation Growth Rate Model")

    x_lin, y_lin = linearize_power_equation(x, y)
    reg = LinearRegression().fit(x_lin.reshape(-1, 1), y_lin)
    alpha_power = 10 ** reg.intercept_
    betha_power = reg.coef_[0]
    print(f"Linearized Power Equation Model: alpha = {alpha_power:.4f}, betha = {betha_power:.4f}")
    plot_data(x_lin, y_lin, reg.predict(x_lin.reshape(-1, 1)), label="Linearized Power Equation Model", title="Linearized Power Equation Model")

    x_lin, y_lin = linearize_exponential_model(x, y)
    reg = LinearRegression().fit(x_lin.reshape(-1, 1), y_lin)
    alpha_exponential = np.exp(reg.intercept_)
    betha_exponential = reg.coef_[0]
    print(f"Linearized Exponential Model: alpha = {alpha_exponential:.4f}, betha = {betha_exponential:.4f}")
    plot_data(x_lin, y_lin, reg.predict(x_lin.reshape(-1, 1)), label="Linearized Exponential Model", title="Linearized Exponential Model")

if __name__ == "__main__":
    main()