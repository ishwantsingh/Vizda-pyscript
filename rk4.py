from euler import Euler

class RungeKutta4(Euler):

    def step(self, t, y):
        
        dt = self._dt
        k1 =  self._model.rhs(t, y)
        k2 =  self._model.rhs(t + dt/2, y + k1/2)
        k3 =  self._model.rhs(t + dt/2, y + k2/2)
        k4 =  self._model.rhs(t + dt, y + k3)
        ynew = y + (k1 + 2*k2 + 2*k3 + k4)/6
        return ynew
