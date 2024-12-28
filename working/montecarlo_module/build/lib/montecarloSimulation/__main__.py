from .montecarloSimulation import setup_args, run_sim, plot_res

if __name__ == "__main__":
    args = setup_args()
    sim_data = run_sim(args.n, args.s, args.d)
    plot_res(sim_data)
