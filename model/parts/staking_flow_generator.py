import numpy as np
import pandas as pd
from scipy.stats import poisson, norm
from sklearn.linear_model import LinearRegression

# Define the staking flow generator
past_days = 300
n_samples = 150

## loading datasets
staking_flow =  pd.read_csv('model/data/staking_flow.csv')
eth_burn = pd.read_csv('model/data/eth_burn.csv')

staking_flow['amount_full_withdrawn'] = -staking_flow['amount_full_withdrawn']/32
staking_flow['amount_partial_withdrawn'] = -staking_flow['amount_partial_withdrawn']

staking_flow['amount_staked'] = staking_flow['amount_staked']/32

def simulate_data(df, n_samples, past_days, simulated_type, simulated_name):
    # Filter and potentially aggregate the data
    if simulated_type == 'entity':
        filtered_data = df[df[simulated_type] == simulated_name]
    elif simulated_type == 'entity_category':
        filtered_data = df[df[simulated_type] == simulated_name]
        filtered_data = filtered_data.groupby('day').agg({
            'amount_full_withdrawn': 'sum',
            'amount_partial_withdrawn': 'sum',
            'amount_staked': 'sum'
        }).reset_index()
        filtered_data['day'] = pd.to_datetime(filtered_data['day'])
    else:
        raise ValueError("simulated_type must be 'entity' or 'entity_category'")

    # Filter data to include only the last 'past_days'
    max_date = filtered_data['day'].max()
    start_date = max_date - pd.Timedelta(days=past_days)
    filtered_data = filtered_data[filtered_data['day'] > start_date]

    # Perform simulations
    simulated_withdrawn = simulate_zero_inflated_data(filtered_data['amount_full_withdrawn'], n_samples, (filtered_data['amount_full_withdrawn'] == 0).mean())
    simulated_staked = simulate_zero_inflated_data(filtered_data['amount_staked'], n_samples, (filtered_data['amount_staked'] == 0).mean())
    simulated_partial_withdrawn = simulate_based_on_day(filtered_data, n_samples)

    # Make withdrawals negative
    simulated_withdrawn = -np.abs(simulated_withdrawn)
    simulated_partial_withdrawn = -np.abs(simulated_partial_withdrawn)

    # Compile all simulated data into a DataFrame
    simulated_data = pd.DataFrame({
        'day': [max_date + pd.Timedelta(days=i) for i in range(1, n_samples + 1)],
        'amount_full_withdrawn': simulated_withdrawn,
        'amount_partial_withdrawn': simulated_partial_withdrawn,
        'amount_staked': simulated_staked
    })

    return simulated_data

def simulate_zero_inflated_data(data, n_samples, proportion_zeros):
    n_zeros = int(n_samples * proportion_zeros)
    zeros = np.zeros(n_zeros)
    non_zeros = poisson.rvs(mu=data[data > 0].mean(), size=n_samples - n_zeros)
    full_sample = np.concatenate([zeros, non_zeros])
    np.random.shuffle(full_sample)
    return full_sample

def simulate_based_on_day(data, n_samples):
    model = LinearRegression()
    days = np.array(data['day'].map(pd.Timestamp.toordinal)).reshape(-1, 1)
    values = data['amount_partial_withdrawn']
    model.fit(days, values)
    max_day = days.max()
    future_days = np.array([max_day + i for i in range(1, n_samples + 1)]).reshape(-1, 1)
    return model.predict(future_days)

simulated_data = {
    'CEX': simulate_data(staking_flow, n_samples, past_days, 'entity_category', 'CEXs'),
    'LST': simulate_data(staking_flow, n_samples, past_days, 'entity_category', 'Liquid Staking'),
    'LRT': simulate_data(staking_flow, n_samples, past_days, 'entity_category', 'Liquid Restaking'),
    'Solo': simulate_data(staking_flow, n_samples, past_days, 'entity_category', 'Solo Stakers'),
    'StakingPool': simulate_data(staking_flow, n_samples, past_days, 'entity_category', 'Staking Pools'),
} 
