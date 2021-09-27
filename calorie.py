from temperature import Temperature

class Calorie:
    """Represents amount of ca;ories calculated with
    BMR=10*weight+6.25*height-5*age+5-10*temperature"""

    def __init__(self,weight,height, age,temperature):
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight

    def calculate(self):
        result=10*self.weight+6.25*self.height-5*self.age+5-10*self.temperature
        return result

    if __name__=='__main__':
        temperature=Temperature(country="Italy",city='Rome').get()
        calorie=Calorie(weight=70,height=175,age=32,temperature=temperature)
        print(calorie.calculate())
