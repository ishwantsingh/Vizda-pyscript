from integrator import Integrator
from euler import Euler
from rk4 import RungeKutta4
from ab2 import AdamsBashforth2

class IntegratorFactory:
    
    __integrators_list = {}

    #get a list of available integrators
    @staticmethod
    def get_integrators_list():
        return IntegratorFactory.__integrators_list.keys()
    
    #create a new integrator if it doesn't already exist
    @staticmethod
    def create(integrator: Integrator, name: str):
        if name not in IntegratorFactory.__integrators_list:
            IntegratorFactory.__integrators_list[name] = integrator
        else:
            print('Integrator exists')

    #get the required integrator based on the name provided in input
    @staticmethod
    def get_integrator(name: str) -> Integrator:
        try:
            return IntegratorFactory.__integrators_list[name]
        except KeyError:
            raise Exception(f"Requested Integrator: {name} - does not exist.")

IntegratorFactory.create(Euler, 'euler')
IntegratorFactory.create(AdamsBashforth2,'adam')
IntegratorFactory.create(RungeKutta4,'rungeKutta')