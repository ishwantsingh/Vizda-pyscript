# from ModelFactory import ModelFactory
# from PlotFactory import PlotFactory
# from IntegratorFactory import IntegratorFactory

# import numpy as np
# # import sys
# # import yaml

# #use sys to get arguments from the yaml file
# # arguments = sys.argv[1:]

# # #load params from yaml into variable
# # with open(arguments[0], 'r') as f:
# #         params = yaml.safe_load(f)


# # #get model factory class method
# # model = ModelFactory.get_model(params['model']['name'])

# # #in the model pass the ddo with the required parameters
# # ddo_model = model(params['model']['params']['omega0'], params['model']['params']['beta'],params['model']['params']['omega'],params['model']['params']['F'])

# # #get integrator factory class method
# # integrator = IntegratorFactory.get_integrator(params['integrator']['name'])

# # #in the integrator pass the ddo model
# # integrator_ob = integrator(ddo_model,params['integrator']['dt'])

# # plotCurve = PlotFactory.get_PlotCurve(params['plot']['name'])
# # lineGraph = plotCurve()

# # print(params['plot'])

# # t = 0.0
# # y = np.array([0.0,0.0])

# # x_arr = []
# # y_arr = []

# # for i in range(20):
# #         y = integrator_ob.step(t,y)
# #         t+=params['integrator']['dt']
# #         x_arr.append(y[0])
# #         y_arr.append(y[1])
# #         print("{:.15f} {:.15f} {:.15f}".format(t, y[0],y[1]))
# # print('params', params)

# # lineGraph.plot(x_arr, y_arr)


# params = {
#         'model': {
#         'name': 'ddo', 
#         'params': {
#                 'omega0': 0.5, 
#                 'beta': 0.25, 
#                 'omega': 0.5, 
#                 'F': 1.0
#         }
#         }, 
#         'integrator': {
#         'name': 'euler', 
#         'dt': 0.9424777960769379
#         }, 
#         'data': {
#         'ICs': {
#                 't': 0.0, 
#                 'x': 0.0, 
#                 'v': 0.0
#         }, 
#         'N': 20
#         }, 
#         'plot': {
#         'name': 'lineGraph'
#         }
# }

# #get model factory class method
# model = ModelFactory.get_model(params['model']['name'])

# #in the model pass the ddo with the required parameters
# ddo_model = model(params['model']['params']['omega0'], params['model']['params']['beta'],params['model']['params']['omega'],params['model']['params']['F'])

# #get integrator factory class method
# integrator = IntegratorFactory.get_integrator(params['integrator']['name'])

# #in the integrator pass the ddo model
# integrator_ob = integrator(ddo_model,params['integrator']['dt'])

# plotCurve = PlotFactory.get_PlotCurve(params['plot']['name'])
# lineGraph = plotCurve()


# t = 0.0
# y = np.array([0.0,0.0])

# x_arr = []
# y_arr = []

# for i in range(20):
#         y = integrator_ob.step(t,y)
#         t+=params['integrator']['dt']
#         x_arr.append(y[0])
#         y_arr.append(y[1])
#         print("{:.15f} {:.15f} {:.15f}".format(t, y[0],y[1]))

# lineGraph.plot(x_arr, y_arr)

    # Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import js
import json
import plotly
import plotly.express as px

import numpy as np
import abc

## Get the data
from pyodide.http import open_url

url = 'https://raw.githubusercontent.com/alanjones2/uk-historical-weather/main/data/Heathrow.csv'
url_content = open_url(url)

df = pd.read_csv(url_content)
df = df[df['Year']==2020]
print('df',df)
def plot(chart):
        fig = px.line(df,
        x="Month", y=chart,
        width=800, height=400)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        js.plot(graphJSON,"chart1")
                
from js import document
from pyodide import create_proxy

def selectChange(event):
        choice = document.getElementById("select").value

def setup():
        # Create a JsProxy for the callback function
        change_proxy = create_proxy(selectChange)
        e = document.getElementById("select")
        e.addEventListener("change", change_proxy)

setup()





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

# create ModelFactory method to document which ODEs/integrators are available, and return objects of the appropriate subclass

class ModelFactory:

        __models_list = {}

        #create static method to add models, without the factory explicitly knowing the models beforehand
        @staticmethod
        def create(model: Model, name: str):
                if name not in ModelFactory.__models_list:
                        ModelFactory.__models_list[name] = model
                else:
                        print('Model exists')

        #create static method to get the model, without the factory haveing explicit knowledge of what will be asked beforehand
        @staticmethod
        def get_model(name: str) -> Model:
                try:
                        return ModelFactory.__models_list[name]
                except KeyError:
                        raise Exception(f"Requested Model: {name} - does not exist.")


ModelFactory.create(DDOscillator, "ddo")


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

class Euler(Integrator):

        def step(self, t, y):
        
                # Compute dydt based on *current* state
                dydt = self._model.rhs(t, y)

                # Use dydt to get state at t + dt
                ynew = y + (dydt * self._dt)

                return ynew

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
        

class LineGraph(PlotCurve):

        def plot(self, x_arr, y_arr):
        
                # <!-- plt.figure(figsize=(7,5))
                # plt.plot(x_arr, y_arr, label="Numerical solution:\nRunge-Kutta", dashes=(3,2), color="blue", lw=3)
                # # Compute dydt based on *current* state
                # # dydt = self._model.rhs(t, y)

                # # # Use dydt to get state at t + dt
                # # ynew = y + (dydt * self._dt)
                # plt.legend(loc="best", fontsize=12)
                # plt.title(r"Solution to ODE: $\quad\frac{dy}{dx}=x^2$")
                # plt.xlabel("x", fontsize=12)
                # plt.ylabel("y", fontsize=12)
                # plt.show() -->
                df = pd.DataFrame(dict(
                        x = x_arr,
                        y = y_arr
                ))
                fig = px.line(df, x="x", y="y", title="Unsorted Input", width=500, height=500)
                graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
                js.plot(graphJSON,"chart1")
                # return 

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

params = {
        'model': {
        'name': 'ddo', 
        'params': {
                'omega0': 0.5, 
                'beta': 0.25, 
                'omega': 0.5, 
                'F': 1.0
        }
        }, 
        'integrator': {
        'name': 'euler', 
        'dt': 0.9424777960769379
        }, 
        'data': {
        'ICs': {
                't': 0.0, 
                'x': 0.0, 
                'v': 0.0
        }, 
        'N': 20
        }, 
        'plot': {
        'name': 'lineGraph'
        }
}

#get model factory class method
model = ModelFactory.get_model(params['model']['name'])

#in the model pass the ddo with the required parameters
ddo_model = model(params['model']['params']['omega0'], params['model']['params']['beta'],params['model']['params']['omega'],params['model']['params']['F'])

#get integrator factory class method
integrator = IntegratorFactory.get_integrator(params['integrator']['name'])

#in the integrator pass the ddo model
integrator_ob = integrator(ddo_model,params['integrator']['dt'])

plotCurve = PlotFactory.get_PlotCurve(params['plot']['name'])
lineGraph = plotCurve()


t = 0.0
y = np.array([0.0,0.0])

x_arr = []
y_arr = []

for i in range(20):
        y = integrator_ob.step(t,y)
        t+=params['integrator']['dt']
        x_arr.append(y[0])
        y_arr.append(y[1])
        print("{:.15f} {:.15f} {:.15f}".format(t, y[0],y[1]))

lineGraph.plot(x_arr, y_arr)