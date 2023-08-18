from model import Model
from ddo import DDOscillator
from lv import LoktaVolterra

# create ModelFactory method to document which ODEs/integrators are available, and return objects of the appropriate subclass

class ModelFactory:

    __models_list = {}

    #create static method to add models, without the factory explicitly knowing the models beforehand
    @staticmethod
    def create(model: Model, name: str):
        if name not in ModelFactory.__models_list:
            ModelFactory.__models_list[name] = model
        else:
            print('Model exists')

    #create static method to get the model, without the factory haveing explicit knowledge of what will be asked beforehand
    @staticmethod
    def get_model(name: str) -> Model:
        try:
            return ModelFactory.__models_list[name]
        except KeyError:
            raise Exception(f"Requested Model: {name} - does not exist.")


ModelFactory.create(DDOscillator, "ddo")
ModelFactory.create(LoktaVolterra, "LoktaVolterra")