import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def geometric_brownian_motion(S0, mu, sigma, T, num_simulations=10000):
    """Vectorized simulation of stock prices using Geometric Brownian Motion."""
    Z = np.random.randn(num_simulations)  # Generate all random variables at once
    return S0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

def monte_carlo_option_price(S0, K, T, r, sigma, option_type="call", num_simulations=10000):
    """Vectorized Monte Carlo estimation of European option prices."""
    ST = geometric_brownian_motion(S0, r, sigma, T, num_simulations)
    payoffs = np.maximum(ST - K, 0) if option_type == "call" else np.maximum(K - ST, 0)
    return np.exp(-r * T) * np.mean(payoffs)

def black_scholes_option_price(S0, K, T, r, sigma, option_type="call"):
    """Black-Scholes formula for European option pricing."""
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == "call":
        return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)

def plot_price_distribution(ST, S0, title="Stock Price Distribution at Maturity"):
    """Histogram of simulated stock prices."""
    plt.figure(figsize=(10, 6))
    plt.hist(ST, bins=50, color='blue', edgecolor='black', alpha=0.7)
    plt.axvline(S0, color='r', linestyle='dashed', linewidth=2, label=f'Initial Price: {S0}')
    plt.axvline(np.mean(ST), color='g', linestyle='dashed', linewidth=2, label=f'Mean Price: {np.mean(ST):.2f}')
    plt.title(title)
    plt.xlabel("Stock Price")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

def compare_models(S0, K, T, r, sigma, num_simulations=10000):
    """Compares Monte Carlo and Black-Scholes option pricing models."""
    call_mc = monte_carlo_option_price(S0, K, T, r, sigma, "call", num_simulations)
    put_mc = monte_carlo_option_price(S0, K, T, r, sigma, "put", num_simulations)
    call_bs = black_scholes_option_price(S0, K, T, r, sigma, "call")
    put_bs = black_scholes_option_price(S0, K, T, r, sigma, "put")

    print(f"\nOption Pricing Comparison ({num_simulations} Simulations)")
    print("-" * 50)
    print(f"Call Option Price (Monte Carlo):  {call_mc:.4f}")
    print(f"Call Option Price (Black-Scholes): {call_bs:.4f}")
    print(f"Difference (Call): {abs(call_mc - call_bs):.4f}")
    print("-" * 50)
    print(f"Put Option Price (Monte Carlo):  {put_mc:.4f}")
    print(f"Put Option Price (Black-Scholes): {put_bs:.4f}")
    print(f"Difference (Put): {abs(put_mc - put_bs):.4f}")

def main():
    """Runs Monte Carlo simulations and compares with Black-Scholes."""
    S0, K, T, r, sigma, num_simulations = 100.0, 100.0, 1.0, 0.05, 0.2, 100000
    ST = geometric_brownian_motion(S0, r, sigma, T, num_simulations)
    plot_price_distribution(ST, S0)
    compare_models(S0, K, T, r, sigma, num_simulations)

if __name__ == "__main__":
    main()
