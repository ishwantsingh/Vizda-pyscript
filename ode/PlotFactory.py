from plotCurve import PlotCurve
from lineGraph import LineGraph

class PlotFactory:
    
    __plot_list = {}

    #get a list of available integrators
    @staticmethod
    def get_plot_list():
        return PlotFactory.__plot_list.keys()
    
    #create a new integrator if it doesn't already exist
    @staticmethod
    def create(plotCurve: PlotCurve, name: str):
        if name not in PlotFactory.__plot_list:
            PlotFactory.__plot_list[name] = plotCurve
        else:
            print('Plot already exists')

    #get the required integrator based on the name provided in input
    @staticmethod
    def get_PlotCurve(name: str) -> PlotCurve:
        try:
            print('exists')
            return PlotFactory.__plot_list[name]
        except KeyError:
            raise Exception(f"Requested Plot: {name} - does not exist.")

PlotFactory.create(LineGraph, 'lineGraph')