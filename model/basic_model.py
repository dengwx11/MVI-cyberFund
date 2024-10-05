def update_timestep(params, step, h, s, _input):
    timestep = s['timestep']
    
    return "timestep", timestep+1

def update_price(params, step, h, s, _input):
    eth_price_process = params["eth_price_process"]
    
    new_price = eth_price_process(s['run'],s["timestep"])

    
    return ("price", new_price)

