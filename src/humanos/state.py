from dataclasses import dataclass


@dataclass
class HumanState:
    knowledge: float = 0.0
    skill: float = 0.0
    energy: float = 100.0
    fatigue: float = 0.0