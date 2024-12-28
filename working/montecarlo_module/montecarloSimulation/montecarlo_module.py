import numpy as np
import matplotlib.pyplot as plt
from numba import njit
import argparse

@njit(nopython=True)
def tomorrow(today0, N):
    today = [today0[0]]
    for i in range(N):
        current_state = today[i]
        p = np.random.rand() * 100  # Random probability between 0 and 100

        if current_state == 0:  # Bull market
            if p < 2.5:
                today.append(0)  # Remain bull
            elif p <= 7.5:
                today.append(1)  # Transition to bear
            else:
                today.append(2)  # Transition to stagnant

        elif current_state == 1:  # Bear market
            if p < 5:
                today.append(0)  # Transition to bull
            elif p <= 15:
                today.append(1)  # Remain bear
            else:
                today.append(2)  # Transition to stagnant

        else:  # Stagnant market
            if p < 25:
                today.append(0)  # Transition to bull
            elif p <= 50:
                today.append(1)  # Transition to bear
            else:
                today.append(2)  # Remain stagnant

    return today

def run_sim(use_numba, starting_point, n_days):
    if use_numba:
        the_days = tomorrow(np.array([starting_point]), n_days)
    else:
        the_days = tomorrow.py_func(np.array([starting_point]), n_days)

    return the_days

def plot_res(data):
    # Plot histogram
    plt.hist(data, bins=3, density=True, histtype='step', color='orange', label=['Bull', 'Bear', 'Stagnant'])
    plt.xticks([0, 1, 2], ['Bull', 'Bear', 'Stagnant'])
    plt.xlabel('Market State')
    plt.ylabel('Probability Density')
    plt.title('Market State Distribution Over Time')
    plt.legend()
    plt.show()

def setup_args():
    parser = argparse.ArgumentParser(description="Monte Carlo simulation of market states.")
    parser.add_argument("-i", help="Description of this module", type=str, default='this module runs a Monte Carlo simulation')
    parser.add_argument("-n", help="Use numba version (default: True)", action='store_true')
    parser.add_argument("-d", help="Number of days to simulate (default: 1000)", type=int, default=1000)
    parser.add_argument("-s", help="Initial state among [0,1,2] (default: 0)", type=int, default=0)

    return parser.parse_args()

if __name__ == "__main__":
    args = setup_args()
    sim_data = run_sim(args.n, args.s, args.d)
    plot_res(sim_data)
