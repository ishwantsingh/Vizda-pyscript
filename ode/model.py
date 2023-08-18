import abc

class Model(abc.ABC):
    '''
    Abstract base class describing Model interface.

    Models should be:

    + initialized with (and store) any necessary parameters;

    + have a rhs() method with signature rhs(t, y) (see docstring in
      rhs method below for more info)
    '''
    
    @abc.abstractmethod
    def rhs(self, t, y):
        '''

        Parameters:

        t: current time (scalar)

        y: current state (vector, numpy-like interface; len(y) = number of state vars

        Returns:

        dy/dt:  derivative of state at time t; dydt = rhs(t, y) (numpy array)

        '''
        pass

