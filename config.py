DELTA_TIME = 1  # iteration time per day
SIMULATION_TIME_MONTHS = 60  # number of months
TIMESTEPS = (
    30 * SIMULATION_TIME_MONTHS // DELTA_TIME
)  # number of simulation timesteps
MONTE_CARLO_RUNS = 1  # number of runs