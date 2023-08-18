from integrator import Integrator

class Euler(Integrator):


    def step(self, t, y):
        
        # Compute dydt based on *current* state
        dydt = self._model.rhs(t, y)

        # Use dydt to get state at t + dt
        ynew = y + (dydt * self._dt)

        return ynew

