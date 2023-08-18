import numpy as np
from model import Model

class LoktaVolterra(Model):

    def __init__(self, alpha, beta, gamma, delta):
        self._alpha = alpha
        self._beta = beta
        self._gamma = gamma
        self._delta = delta

    def rhs(self, t, y):
        assert len(y) == 2, f"err: y is of length: {len(y)}, length of y should be 2 instead."
        dydt = np.zeros_like(y)

        x, y = y[0], y[1]
        alpha, beta = self._alpha, self._beta
        gamma, delta = self._gamma, self._delta
        dydt[0] = x * (alpha - beta*y)
        dydt[1] = -y * (gamma - delta*x)

        return dydt
