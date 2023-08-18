import numpy as np

from model import Model


class DDOscillator(Model):


    def __init__(self, omega0, beta, omega, F):
        '''

        Parameters:

        omega0: natural oscillator frequency (angular)

        beta: damping coefficient of oscillator

        omega: driving frequency (angular) 

        F: driving amplitude
        '''
        self._omega0 = omega0
        self._beta = beta
        self._omega = omega
        self._F = F

        
    def rhs(self, t, y):
        '''Damped driven oscillator as a system of first-order coupled ODEs:

        dxdt = v
        dvdt = F*cos(omega*t) - (omega0**2)*x - 2.0*beta*v

        Parameters:

        t: current time

        y: state vector at t (numpy-like, length 2: [x,v])
        
        Returns:
        
        dydt: (numpy-like) [dxdt, dvdt]
        '''
        assert len(y) == 2, f"State y should be length 2; got length: {len(y)}"

        dydt = np.zeros_like(y)
        
        # Legibility lines
        x, v = y[0], y[1]
        om0, beta = self._omega0, self._beta
        om, F = self._omega, self._F

        # Set dxdt, dvdt
        dydt[0] = v        
        dydt[1] = F*np.cos(om*t) - (om0**2)*x - 2.0*beta*v
        
        return dydt
