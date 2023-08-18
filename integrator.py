import abc

class Integrator(abc.ABC):
    '''Abstract base class describing Integrator interface
    '''

    # All Integrator subclasses should will share __init__()
    def __init__(self, model, dt):
        '''
        Parameters
        ----------
    
        model: Model object with a rhs() method that takes a t,y and
        returns dy/dt (for some system of ODEs)

        dt: timestep (fixed) for integrations

        '''
        self._model = model
        self._dt = dt

    
    @abc.abstractmethod
    def step(self, t, y):
        '''
        Parameters:

        t: current time

        y: vector (numpy-like) giving current state

        Returns: y at time t + dt
        '''
        pass

