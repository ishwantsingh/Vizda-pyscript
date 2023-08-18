[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/JlcqyvbY)
# S23_ode_design_assgnmt
Practice with interfaces, object-oriented design, Git &amp; Python basics

# Solving 2nd order differential equations using abstract classes

## Programming Language used:

### Python

## Goals and overview of the assignment

### Factory classes: IntegratorFactory and ModelFactory ```(IntegratorFactory.py & ModelFactory.py)```
Take in the Model and Integrator abstract base class, have the functions for creating and getting new models and integrators.

### Driver code ```(ode_solve.py)```
Generally written, all-purpose code with no specifics to the model or integrator being used.

### RungeKutta4 and AdamsBashforth2 Integrators
New integrator methods implemented using the IntegratorFactory. Can be used by changing the 'name' field of the integrator in the ddo_euler_sample.yml file to either 'rangeKutta' or 'adam'.

### LotkaVolterra Model
New Model implemented using the ModelFactory. Can be used by changing the 'name' field of the Model in the ddo_euler_sample.yml file to 'LoktaVolterra'.

### Collaboration note:
Discussed implementation of factory methods with Sukriti Macker and the implementation of driver code with Satya Vamsi

Reffered to: 
[this website](https://www.codesansar.com/numerical-methods/runge-kutta-fourth-order-rk4-python-program.htm) for the implementation of Rangekutta4

[this website](https://scicomp.stackexchange.com/questions/35676/solving-lotka-volterra-equations-on-python) and [this website](https://scientific-python.readthedocs.io/en/latest/notebooks_rst/3_Ordinary_Differential_Equations/02_Examples/Lotka_Volterra_model.html) for the implementation of LotkaVolterra