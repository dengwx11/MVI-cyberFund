from config import DELTA_TIME

# Hardware costs
solo_hardware_cost = 800
large_node_operator = 7.75e6
large_node_quntity = 1e5

 
solo_operational = 74

large_node_operational = 2e7

solo_maintainance = 0


large_node_maintainance = 1.14e7

large_node_commision_rate = 0.1

def calc_costs(params, step, h, s):
    timestep = s['timestep']
    price = s['price']

    CEXAgent = s["CEXAgent"]
    LSTAgent = s["LSTAgent"]
    LRTAgent = s["LRTAgent"]
    SoloAgent = s["SoloAgent"]
    StakingPoolAgent = s["StakingPoolAgent"]
    ETFAgent = s["ETFAgent"]

    solo_cost = (solo_operational + solo_maintainance)   \
                            + solo_hardware_cost /5
    large_node_cost = (large_node_operational + large_node_maintainance  + large_node_operator /5) \
                        / large_node_quntity

    # CEXAgent.cost_APY = large_node_cost  / price / 32
    # LSTAgent.cost_APY = large_node_cost / price / 32
    # LRTAgent.cost_APY = large_node_cost / price / 32
    CEXAgent.cost_APY = 0.0
    LSTAgent.cost_APY = 0.0
    LRTAgent.cost_APY = 0.0
    SoloAgent.cost_APY = solo_cost / price / 32
    StakingPoolAgent.cost_APY = large_node_cost / price / 32
    ETFAgent.cost_APY = 0.0

    return ({
        "CEXAgent": CEXAgent,
        "LSTAgent": LSTAgent,
        "LRTAgent": LRTAgent,
        "SoloAgent": SoloAgent,
        "StakingPoolAgent": StakingPoolAgent,
        "ETFAgent": ETFAgent,
    })

def update_CEXAgent_cost(params, step, h, s, _input):
    return ("CEXAgent",_input["CEXAgent"])  

def update_LSTAgent_cost(params, step, h, s, _input):
    return ("LSTAgent",_input["LSTAgent"])

def update_LRTAgent_cost(params, step, h, s, _input):
    return ("LRTAgent",_input["LRTAgent"])

def update_SoloAgent_cost(params, step, h, s, _input):
    return ("SoloAgent",_input["SoloAgent"])

def update_StakingPoolAgent_cost(params, step, h, s, _input):
    return ("StakingPoolAgent",_input["StakingPoolAgent"])

def update_ETFAgent_cost(params, step, h, s, _input):
    return ("ETFAgent",_input["ETFAgent"])
