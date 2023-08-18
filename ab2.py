from euler import Euler

class AdamsBashforth2(Euler):

    def step(self, t, y):
        if self._prev_y is None or self._prev_dydt is None:

            self._prev_y = y
            self._prev_dydt = self._model.rhs(t, y)
            ynew = y + self._dt * self._prev_dydt

        else:
            
            dydt = self._model.rhs(t, y)
            ynew = y + (3/2 * self._dt * dydt) - (1/2 * self._dt * self._prev_dydt)
            self._prev_y = y
            self._prev_dydt = dydt

        return ynew    