from model.parts.staking_flow_generator import simulated_data
from functools import partial

from model.utils import sigmoid_logistic_func
from model.agents import BaseAgent

def profit_rationality(
        revenue_APY: float,
        opportunity_cost: float,
        ):
    """ Decision function for profit rationality"""
    return revenue_APY - opportunity_cost

def deposit_or_withdraw(agent, profit_value, action, timestep, agent_type, simulated_data, sigmoid_func):
    """
    Perform deposit or full withdrawal for a given agent based on profit rationality.
    """
    amount = (
        simulated_data[agent_type].iloc[timestep-1]['amount_staked']
        if action == 'deposit' else
        simulated_data[agent_type].iloc[timestep-1]['amount_full_withdrawn']
    )
    amount *= sigmoid_func(profit_value)
    
    if action == 'deposit':
        agent.deposit(amount)
    else:
        agent.full_withdraw(amount)

def deposit_withdraw(params, step, h, s):
    CEXAgent = s["CEXAgent"]
    LSTAgent = s["LSTAgent"]
    LRTAgent = s["LRTAgent"]
    SoloAgent = s["SoloAgent"]
    StakingPoolAgent = s["StakingPoolAgent"]

    agents = {
        "CEXAgent": CEXAgent,
        "LSTAgent": LSTAgent,
        "LRTAgent": LRTAgent,
        "SoloAgent": SoloAgent,
        "StakingPoolAgent": StakingPoolAgent,
    }

    revenue_APY_at_agent = s["revenue_APY_at_agent"]
    price = s["price"]

    timestep = s['timestep']

    opportunity_cost = params['opportunity_cost']

    sigmoid_fixed = partial(sigmoid_logistic_func, alpha=2, theta=0)

    for agent_type, revenue_APY in revenue_APY_at_agent.items():
        profit_rationality_value = profit_rationality(revenue_APY, opportunity_cost)
        action = 'deposit' if profit_rationality_value >= 0 else 'full_withdraw'
        
        # Call function with the specific agent and appropriate values
        deposit_or_withdraw(
            agents[agent_type],
            abs(profit_rationality_value),
            action,
            timestep,
            agent_type,
            simulated_data,
            sigmoid_fixed
        )


    return ({
        "CEXAgent": CEXAgent,
        "LSTAgent": LSTAgent,
        "LRTAgent": LRTAgent,
        "SoloAgent": SoloAgent,
        "StakingPoolAgent": StakingPoolAgent
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

