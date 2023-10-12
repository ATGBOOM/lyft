from abc import ABC, abstractmethod
from engine.engine import Engine
from battery.battery import  Battery

class Car(ABC):
    def __init__(self, engine, battery):
        self.last_service_date = last_service_date
        self.engine = Engine(engine)
        self.battery = Battery(battery)

  
    def needs_service(self):
    
        if self.engine.needs_service() and self.battery.needs_service():
            return True
        else:
            return False
            

        
