import numpy as np

def optimize_portfolio(alphas, risks, lambday, total_portfolio_value):
    # Create matrix A for the system of equations
    A = np.vstack([np.diag(risks * lambday), np.ones(len(alphas))])
    
    # Adjust the shapes to match the optimization requirements
    better_lambda = np.append(np.ones(len(alphas)), 0).reshape(-1, 1)
    
    A = np.hstack([A, better_lambda])
    
    # Create vector b
    b = np.append(alphas / lambday, 0)
    
    # Solve the system of linear equations
    ws = np.linalg.solve(A.T @ A, A.T @ b)
    
    # Remove the last element associated with the Lagrangian multiplier
    ws = ws[:-1]
    
    # Calculate the dollar amount allocated to each stock
    dollar_amounts = ws * total_portfolio_value
    
    return ws, dollar_amounts

def monte_carlo_simulation(S0, alphas, risks, T, steps, simulations):
    n_stocks = len(S0)
    dt = T / steps
    all_paths = np.zeros((steps, simulations, n_stocks))

    for i in range(n_stocks):
        paths = np.zeros((steps, simulations))
        paths[0] = S0[i]
        for t in range(1, steps):
            z = np.random.standard_normal(simulations)
            paths[t] = paths[t - 1] * np.exp((alphas[i] - 0.5 * risks[i]**2) * dt + risks[i] * np.sqrt(dt) * z)
        all_paths[:, :, i] = paths

    return all_paths

def calculate_portfolio_values(paths, ws):
    portfolio_values = np.dot(paths, ws)
    return portfolio_values