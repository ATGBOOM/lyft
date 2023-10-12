from datetime import datetime
from engine import capulet_engine, sternman_engine, willoughby_engine
from car import Car

class ClassFactory():

    def __init__(Car):
        super().__init__(self, engine, battery)
        pass 
    
    def createCalliope(date, currentmileage, lastmileage):
        currentDate = datetime.today().date()
        lastServiceDate = date
        currentMileage = currentmileage
        lastServiceMileage = lastmileage
        engine = capulet_engine.CapuletEngine()
    
    def createGlissade(date, currentmileage, lastmileage):
        currentDate = datetime.today().date()
        lastServiceDate = date
        currentMileage = currentmileage
        lastServiceMileage = lastmileage
        engine = willoughby_engine.WilloughbyEngine()

    def createRorschach(date, currentmileage, lastmileage):
        currentDate = datetime.today().date()
        lastServiceDate = date
        currentMileage = currentmileage
        lastServiceMileage = lastmileage
        engine = willoughby_engine.WilloughbyEngine()

    def createThovex(date, currentmileage, lastmileage):
        currentDate = datetime.today().date()
        lastServiceDate = date
        currentMileage = currentmileage
        lastServiceMileage = lastmileage
        engine = capulet_engine.CapuletEngine()

    def createPalindrome(date, iswarninglight):
        currentDate = datetime.today().date()
        lastServiceDate = date 
        warningLightOn = iswarninglight
        engine = sternman_engine.SternmanEngine()