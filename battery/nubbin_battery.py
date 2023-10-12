from abc import ABC
from datetime import datetime
from car import Car

class NubbinBattery(Car, ABC):
    def __init__(self):
        self.last_service_date = super().__init__(last_service_date)
        self.today = datetime.today().date()
    
    def needs_service(self):
        if self.today - self.last_service_date >= 4:
            return True 
        else:
            return False

