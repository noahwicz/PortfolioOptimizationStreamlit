# 📊 Portfolio Optimizer & Simulator

A simple Streamlit app to optimize a stock portfolio based on expected returns, risk, and risk tolerance, then simulate future performance using Monte Carlo methods.

---

## Features

- **Portfolio Optimization** using Lagrange multipliers
- **Dollar Allocation** based on total portfolio value
- **Monte Carlo Simulation** of individual stock prices
- **Interactive Plots** using `st.line_chart` for:
  - Stock price simulations
  - Portfolio value simulations

---

## How to Run

1. Clone the repo:
   git clone https://github.com/yourusername/portfolio-optimizer.git
   cd portfolio-optimizer
2. Install dependencies:
    pip install -r requirements.txt
3. Run the app:
    streamlit run app.py

Inputs
Alphas (expected returns)

Risks (standard deviations)

Initial stock prices

Lambda (risk tolerance)

Total portfolio value

Time horizon, steps, and number of simulations

Outputs
Optimized portfolio weights

Dollar amounts to invest in each stock

Simulated stock paths

Simulated portfolio value over time

File Structure

.
├── app.py                  # Streamlit UI
├── portfolio_optimizer.py # Core optimization & simulation logic
├── requirements.txt
└── README.md

Notes
Ensures correct dimensions by removing the Lagrange multiplier from the solution

Uses Geometric Brownian Motion for price simulation