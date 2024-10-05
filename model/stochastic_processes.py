from config import (
    TIMESTEPS,
    DELTA_TIME,
)
import numpy as np
from stochastic import processes
import matplotlib.pyplot as plt

def create_stochastic_process(
    timesteps=TIMESTEPS,  
    dt=DELTA_TIME,        
    rng=np.random.default_rng(1),
    price_traj_type='convex',  # convex, concave or none
    minimum_price=1000,
    target_avg=2500,
    maximum_price=7000,
):
    process = processes.continuous.BrownianMotion(t=(timesteps * dt), rng=rng)
    samples = process.sample(timesteps + 1)

    normalized_samples = (np.abs(samples) - np.min(samples)) / (np.max(samples) - np.min(samples))
    samples = normalized_samples * (maximum_price - minimum_price) + minimum_price
    #plot_price(samples)
    t = timesteps * dt
    if price_traj_type == 'convex':
        para = (maximum_price - minimum_price) / ((t + 1)**2)
        print(para.__class__)
        samples_add_on = [para * (i**2)+minimum_price for i in range(t+2)]
    elif price_traj_type == 'concave':
        para = (maximum_price - minimum_price) / ((t + 1)**2)
        samples_add_on = [para * ((t+1-i)**2)+minimum_price for i in range(t+2)]
    else:
        samples_add_on = [0 for _ in range(timesteps + 1)]
    
    samples = [max(sample + add_on, minimum_price) for sample, add_on in zip(samples, samples_add_on)]
    #plot_price(samples)
    curr_average = sum(samples) / len(samples)
    adjustment_factor = (target_avg - minimum_price) / (curr_average - minimum_price)
    samples = [minimum_price + (sample - minimum_price) * adjustment_factor for sample in samples]
    
    return samples

def plot_price(samples: list):
    x = list(range(1, len(samples) + 1))
    plt.scatter(x, samples)

    plt.title('Scatter Plot of Values')
    plt.xlabel('Index')
    plt.ylabel('Value')

    plt.show()