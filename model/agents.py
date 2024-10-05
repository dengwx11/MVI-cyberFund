from abc import ABC, abstractmethod
from dataclasses import dataclass



# Define behavior interfaces
class DepositBehavior(ABC):
    @abstractmethod
    def deposit(self, agent, new_validator_cnt: int):
        pass

class WithdrawBehavior(ABC):
    @abstractmethod
    def full_withdraw(self, agent, validator_cnt: int):
        pass

    @abstractmethod
    def partial_withdraw(self, agent):
        pass

# Implement specific behaviors
class StandardDeposit(DepositBehavior):
    def deposit(self, agent, new_validator_cnt: int):
        agent.balance += new_validator_cnt * 32.0
        agent.cnt += new_validator_cnt

class StandardFullWithdraw(WithdrawBehavior):
    def full_withdraw(self, agent, validator_cnt: int):
        agent.balance -= validator_cnt * 32.0
        agent.cnt -= validator_cnt

    def partial_withdraw(self, agent, partial_withdrawl):
        agent.balance -= partial_withdrawl

# Define the base agent class
@dataclass
class BaseAgent:
    balance: float
    cnt: int
    category: str
    cost_APY: float
    # full_withdrawl: float
    # partial_withdrawl: float
    deposit_behavior: DepositBehavior
    withdraw_behavior: WithdrawBehavior

    def deposit(self, new_validator_cnt: int):
        self.deposit_behavior.deposit(self, new_validator_cnt)

    def full_withdraw(self, validator_cnt: int):
        self.withdraw_behavior.full_withdraw(self, validator_cnt)

    def partial_withdraw(self):
        self.withdraw_behavior.partial_withdraw(self)


@dataclass
class CEXAgent(BaseAgent):
    entity: str

@dataclass
class LSTAgent(BaseAgent):
    entity: str

@dataclass
class LRTAgent(BaseAgent):
    entity: str

@dataclass
class SoloAgent(BaseAgent):
    entity: str

@dataclass
class StakingPoolAgent(BaseAgent):
    entity: str

@dataclass
class ETFAgent(BaseAgent):
    entity: str

