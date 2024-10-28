from math import sqrt
import numpy as np
import pandas as pd

def calculate_decentralization_metrics(agents, top_k=3):
    # Extract validator counts from agents
    agent_counts = np.array(list(agents.values()))
    
    # Calculate total number of validators
    total_validators = agent_counts.sum()

    # Avoid division by zero
    if total_validators == 0:
        raise ValueError("Total number of validators cannot be zero.")

    # Calculate market shares
    market_shares = agent_counts / total_validators

    # Calculate HHI (Herfindahl-Hirschman Index)
    market_share_percentage = market_shares * 100
    hhi = (market_share_percentage ** 2).sum()

    # Calculate Concentration Ratio (CR_k) for the top_k largest entities
    sorted_market_shares = np.sort(market_shares)[::-1]  # Sort in descending order
    cr_k = sorted_market_shares[:top_k].sum()

    # Calculate Entropy
    market_shares = np.clip(market_shares, 1e-10, None)  # Avoid log(0)
    log_market_shares = np.log(market_shares)
    entropy = -np.sum(market_shares * log_market_shares)

    # Return the metrics as a dictionary
    return {'HHI': hhi, 'CR_k': cr_k, 'Entropy': entropy}


def calc_decentralization_and_total_staked(params, step, h, s):
    CEXAgent = s["CEXAgent"]
    LSTAgent = s["LSTAgent"]
    LRTAgent = s["LRTAgent"]
    SoloAgent = s["SoloAgent"]
    StakingPoolAgent = s["StakingPoolAgent"]
    ETFAgent = s["ETFAgent"]

    total_validator_cnt = CEXAgent.cnt + LSTAgent.cnt + LRTAgent.cnt + SoloAgent.cnt + StakingPoolAgent.cnt + ETFAgent.cnt
    total_staked = total_validator_cnt * 32.0

    agents_cnt = {
        'CEXAgent': CEXAgent.cnt,
        'LSTAgent': LSTAgent.cnt,
        'LRTAgent': LRTAgent.cnt,
        'SoloAgent': SoloAgent.cnt,
        'StakingPoolAgent': StakingPoolAgent.cnt,
        'ETFAgent': ETFAgent.cnt
    }

    decentralization_metrics = calculate_decentralization_metrics(agents_cnt)

    return ({
            "total_staked": total_staked,
            "total_validator_cnt": total_validator_cnt,
            "decentralization_metrics": decentralization_metrics
        })

def update_total_staked(params, step, h, s, _input):
    return ("total_staked",_input["total_staked"])

def update_total_validator_cnt(params, step, h, s, _input):
    return ("total_validator_cnt",_input["total_validator_cnt"])

def update_decentralization_metrics(params, step, h, s, _input):
    return ("decentralization_metrics",_input["decentralization_metrics"]) 


def calc_issuance_APR(params, step, h, s):

    total_validator_cnt = s["total_validator_cnt"]


    # Calculate the issuance rate based on the total staked amount
    issuance_APR = 29.4021 / sqrt(total_validator_cnt)

    return ({
        "issuance_APR": issuance_APR
    })

def update_issuance_APR(params, step, h, s, _input):
    return ("issuance_APR",_input["issuance_APR"])

def calc_revenue_APY(params, step, h, s):

    issuance_APR = s["issuance_APR"]
    total_validator_cnt = s["total_validator_cnt"]


    CEXAgent = s["CEXAgent"]
    LSTAgent = s["LSTAgent"]
    LRTAgent = s["LRTAgent"]
    SoloAgent = s["SoloAgent"]
    StakingPoolAgent = s["StakingPoolAgent"]

    agents_cnt = {
        'CEXAgent': CEXAgent.cnt,
        'LSTAgent': LSTAgent.cnt,
        'LRTAgent': LRTAgent.cnt,
        'SoloAgent': SoloAgent.cnt,
        'StakingPoolAgent': StakingPoolAgent.cnt
    }

    revenue_APY_at_agent = {
        'CEXAgent': issuance_APR - CEXAgent.cost_APY,
        'LSTAgent': issuance_APR - LSTAgent.cost_APY,
        'LRTAgent': issuance_APR - LRTAgent.cost_APY,
        'SoloAgent': issuance_APR - SoloAgent.cost_APY,
        'StakingPoolAgent': issuance_APR - StakingPoolAgent.cost_APY
    }

    # Calculate the revenue APY based on the total staked amount and issuance APR
    revenue_APY = sum([revenue_APY_at_agent[agent] * agent_cnt/total_validator_cnt for agent, agent_cnt in agents_cnt.items()])

    return ({
        "revenue_APY": revenue_APY,
        "revenue_APY_at_agent": revenue_APY_at_agent,
    })

def update_revenue_APY(params, step, h, s, _input):
    return ("revenue_APY",_input["revenue_APY"])

def update_revenue_APY_at_agent(params, step, h, s, _input):
    return ("revenue_APY_at_agent",_input["revenue_APY_at_agent"])