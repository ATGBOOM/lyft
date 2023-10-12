from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, engine):
        self.engine = engine 
    def needs_Service(self):
        if engine.needs_service():
            return True 
        else:
            return False 