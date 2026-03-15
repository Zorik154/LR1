from typing import Dict

class Car:
    def __init__(self, model: str, owner: str):
        self.Model: str = model
        self.Owner: str = owner

    def to_dict(self) -> Dict[str, str]:
        return {"Model": self.Model, "Owner": self.Owner}

    @staticmethod
    def from_dict(data: Dict[str, str]) -> 'Car':
        return Car(data["Model"], data["Owner"])