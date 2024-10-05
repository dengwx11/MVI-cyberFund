from dataclasses import dataclass

from model.stochastic_processes import create_stochastic_process

@dataclass
class ExternalParams:
    interest_rate: float
    nasdap: float
    exchange_rate: float

    def __init__():
       self.interest_rate = create_stochastic_process(
            price_traj_type = 'convex',
            minimum_price=0,
            target_avg=2,
            maximum_price=10,
            )
       self.exchange_rate = create_stochastic_process(
           price_traj_type = 'concave',
           minimum_price=1500,
           target_avg=2500,
           maximum_price=5000,
           )
       self.nasdap = create_stochastic_process(
           price_traj_type = 'convex',
           minimum_price=15e3,
           target_avg=18e3,
           maximum_price=25e3,
           )