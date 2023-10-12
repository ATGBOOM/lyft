from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, battery):
        self.battery = battery 
    def needsService():
        if battery.needs_service():
            return True 
        else:
            return False 