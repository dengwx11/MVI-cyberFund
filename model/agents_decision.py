from model.parts.staking_flow_generator import simulated_data

def deposit_withdraw(params, step, h, s):
    CEXAgent = s["CEXAgent"]
    LSTAgent = s["LSTAgent"]
    LRTAgent = s["LRTAgent"]
    SoloAgent = s["SoloAgent"]
    StakingPoolAgent = s["StakingPoolAgent"]
    ETFAgent = s["ETFAgent"]

    timestep = s['timestep']


    if timestep < len(simulated_data['CEX']):
        print(f"Timestep: {timestep}, Available data: {len(simulated_data['CEX'])}")
        CEXAgent.deposit(simulated_data['CEX'].iloc[timestep-1]['amount_staked'])
    else:
        print(f"Timestep {timestep} out of bounds. Max index: {len(simulated_data['CEX']) - 1}")

    CEXAgent.full_withdraw(simulated_data['CEX'].iloc[timestep-1]['amount_full_withdrawn'])

    LSTAgent.deposit(simulated_data['LST'].iloc[timestep-1]['amount_staked'])
    LSTAgent.full_withdraw(simulated_data['LST'].iloc[timestep-1]['amount_full_withdrawn'])

    LRTAgent.deposit(simulated_data['LRT'].iloc[timestep-1]['amount_staked'])
    LRTAgent.full_withdraw(simulated_data['LRT'].iloc[timestep-1]['amount_full_withdrawn'])

    SoloAgent.deposit(simulated_data['Solo'].iloc[timestep-1]['amount_staked'])
    SoloAgent.full_withdraw(simulated_data['Solo'].iloc[timestep-1]['amount_full_withdrawn'])

    StakingPoolAgent.deposit(simulated_data['StakingPool'].iloc[timestep-1]['amount_staked'])
    StakingPoolAgent.full_withdraw(simulated_data['StakingPool'].iloc[timestep-1]['amount_full_withdrawn'])

    return ({
        "CEXAgent": CEXAgent,
        "LSTAgent": LSTAgent,
        "LRTAgent": LRTAgent,
        "SoloAgent": SoloAgent,
        "StakingPoolAgent": StakingPoolAgent,
        "ETFAgent": ETFAgent,
    })

def update_CEXAgent_deposit_withdraw(params, step, h, s, _input):
    return ("CEXAgent",_input["CEXAgent"])  

def update_LSTAgent_deposit_withdraw(params, step, h, s, _input):
    return ("LSTAgent",_input["LSTAgent"])

def update_LRTAgent_deposit_withdraw(params, step, h, s, _input):
    return ("LRTAgent",_input["LRTAgent"])

def update_SoloAgent_deposit_withdraw(params, step, h, s, _input):
    return ("SoloAgent",_input["SoloAgent"])

def update_StakingPoolAgent_deposit_withdraw(params, step, h, s, _input):
    return ("StakingPoolAgent",_input["StakingPoolAgent"])

def update_ETFAgent_deposit_withdraw(params, step, h, s, _input):
    return ("ETFAgent",_input["ETFAgent"])
