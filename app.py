import streamlit as st
import numpy as np
from portfolio_optimizer import optimize_portfolio, monte_carlo_simulation, calculate_portfolio_values

st.title("Portfolio Optimizer")

st.sidebar.header("Input Parameters")

# Input fields for alphas, risks, initial stock prices, and lambda
alphas = st.sidebar.text_input("Enter Alphas (comma separated)", "0.1, 0.2")
risks = st.sidebar.text_input("Enter Risks (comma separated)", "0.05, 0.07")
initial_prices = st.sidebar.text_input("Enter Initial Stock Prices (comma separated)", "100, 200")
lambday = st.sidebar.number_input("Enter Lambda (risk tolerance)", value=1.0)
total_portfolio_value = st.sidebar.number_input("Total Portfolio Value", value=100000.0)

# Convert inputs into numpy arrays
alphas = np.array([float(x) for x in alphas.split(',')])
risks = np.array([float(x) for x in risks.split(',')])
initial_prices = np.array([float(x) for x in initial_prices.split(',')])

# Validate input lengths
if len(alphas) != len(risks) or len(alphas) != len(initial_prices):
    st.error("The number of alphas, risks, and initial stock prices must be the same.")
else:
    # Monte Carlo Simulation parameters
    T = st.sidebar.number_input("Time Horizon (T in years)", value=1.0)
    steps = st.sidebar.number_input("Number of Steps", value=252)
    simulations = st.sidebar.number_input("Number of Simulations", value=100)

    if st.sidebar.button("Optimize and Simulate"):
        # Step 1: Optimize portfolio weights and dollar amounts
        ws, dollar_amounts = optimize_portfolio(alphas, risks, lambday, total_portfolio_value)
        st.write("Optimized Weights: ", ws)
        st.write("Dollar Amounts Allocated to Each Stock: ", dollar_amounts)

        # Step 2: Run Monte Carlo simulation for stock prices
        all_paths = monte_carlo_simulation(initial_prices, alphas, risks, T, steps, simulations)
        
        # Check that the dimensions match for multiplication
        if all_paths.shape[2] != len(ws):
            st.error(f"Mismatch in the number of stocks: {all_paths.shape[2]} in simulations vs {len(ws)} in weights.")
        else:
            # Step 3: Calculate portfolio values for each simulation
            portfolio_values = calculate_portfolio_values(all_paths, ws)
            
            # Step 4: Plot the stock simulations using Streamlit's line_chart
            st.header("Stock Price Simulations")
            for i in range(len(initial_prices)):
                st.line_chart(all_paths[:, :, i])  # Plot all simulations for each stock
            
            # Step 5: Plot the portfolio value simulations using Streamlit's line_chart
            st.header("Portfolio Value Simulations")
            st.line_chart(portfolio_values)  # Plot all portfolio value simulations
