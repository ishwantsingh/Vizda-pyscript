from IntegratorFactory import IntegratorFactory
from ModelFactory import ModelFactory
from PlotFactory import PlotFactory

import numpy as np
# import sys
# import yaml

#use sys to get arguments from the yaml file
# arguments = sys.argv[1:]

# #load params from yaml into variable
# with open(arguments[0], 'r') as f:
#         params = yaml.safe_load(f)


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

# print(params['plot'])

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
# print('params', params)

# lineGraph.plot(x_arr, y_arr)


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