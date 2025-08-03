**📈 Monte Carlo & Black-Scholes Option Pricing Simulator**
A comprehensive Python tool for pricing European call and put options using both Monte Carlo simulations and the Black-Scholes-Merton analytical model. This project helps visualize stock price distributions at maturity using Geometric Brownian Motion (GBM) and provides an intuitive comparison between theoretical and empirical option pricing methods.

🧠 **Overview**
Option pricing is central to quantitative finance and risk management. This project simulates the movement of stock prices over time using Geometric Brownian Motion, calculates option values through:

Monte Carlo methods (numerical simulations)

Black-Scholes formula (closed-form solution)

It also includes:

A visual plot of stock price outcomes at maturity.

A side-by-side numerical comparison of Monte Carlo and Black-Scholes prices.

🚀 **Features**

✅ Simulates terminal stock prices using Geometric Brownian Motion.

✅ Prices European call and put options using Monte Carlo simulation.

✅ Computes theoretical prices using the Black-Scholes formula.

✅ Visualizes the distribution of simulated stock prices.

✅ Compares Monte Carlo estimates with Black-Scholes values.

<img width="859" height="547" alt="image" src="https://github.com/user-attachments/assets/b9667f15-c606-4af1-a55f-9ca93a81dec8" />

Option Pricing Comparison (100000 Simulations)
--------------------------------------------------
Call Option Price (Monte Carlo):  10.4106
Call Option Price (Black-Scholes): 10.4506
Difference (Call): 0.0399
--------------------------------------------------
Put Option Price (Monte Carlo):  5.5698
Put Option Price (Black-Scholes): 5.5735
Difference (Put): 0.0038

