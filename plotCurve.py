import abc

class PlotCurve(abc.ABC):
    '''Abstract base class describing Plot interface
    '''

    # All Integrator subclasses should will share __init__()
    def __init__(self):
        '''
        Parameters
        ----------
    
        graph: string telling the type of graph to be plotted

        data: data to be plotted

        '''
        # self._graph = graph
        # self._data = data

    
    @abc.abstractmethod
    def plot(self, x, y):
        '''
        Parameters:

        t: x data points

        y: y data points

        Returns: plot of x and y
        '''
        pass

