import numpy as np
from random import random
from gekko import GEKKO
import matplotlib.pyplot as plt


#----- Process Simulation Setup -----#

p = GEKKO(remote = True)
p.time = np.linspace(0,0.5,0.01)
p.dl = p.MV()
p.beta = p.Param(value=0.05)
p.pop = p.CV()
p.g = p.CV()
p.C = p.Param(value = 1)
p.t = p.Param(value = p.time)
A = 20
K = 300
p.Equation((A+(K-A)/(1+20*p.exp(-p.t*p.beta)))*p.g.dt() == p.dl)
p.Equation(p.pop.dt() == p.C*p.dl)

p.options.IMODE = 4

#----- Moving Horizon Estimation Model Setup -----#
mhe = GEKKO(remote = True)
mhe.time = np.linspace(0,0.5,0.01)
mhe.dl = mhe.MV() #output
mhe.beta = mhe.FV(value = 0.01, lb = 0.0000001, ub = 0.5)
mhe.C = mhe.FV(value = 1, lb = 0.001, ub = 5)
mhe.g = mhe.CV() #measured variable
mhe.pop = mhe.CV()
mhe.t = mhe.Param(value = mhe.time)

mhe.Equation(mhe.dl == (A+(K-A)/(1+20*mhe.exp(-mhe.t*0.05)))*mhe.g.dt())
mhe.Equation(mhe.pop.dt() == mhe.C*p.dl)
mhe.options.IMODE = 5
mhe.options.EV_TYPE = 1
mhe.options.DIAGLEVEL = 0

# STATUS = 0, optimizer doesn't adjust value
# STATUS = 1, optimizer can adjust
mhe.dl.STATUS = 0
mhe.beta.STATUS = 1
mhe.C.STATUS = 1
mhe.pop.STATUS = 1
mhe.g.STATUS = 1

# FSTATUS = 0, no measurement
# FSTATUS = 1, measurement used to update model
mhe.dl.FSTATUS = 1
mhe.beta.FSTATUS = 0
mhe.g.FSTATUS = 1
mhe.C.FSTATUS = 0
mhe.pop.FSTATUS = 1

mhe.beta.DMAX = 0.01
mhe.C.DMAX = 0.01

mhe.pop.MEAS_GAP = 10
mhe.g.MEAS_GAP = 0.01

mhe.g.TR_INIT = 1

#----- Model Predictive Control Setup -----#
mpc = GEKKO(remote = True)
mpc.time = np.linspace(0,0.5,0.01)
mpc.dl = mpc.MV(lb = 0, ub = 1)
mpc.beta = mpc.FV(value = 0.01, lb = 0.0000001, ub = 0.5)
mpc.C = mpc.FV(value = 1, lb = 0.001, ub = 5)
mpc.g = mpc.CV()
mpc.pop = mpc.CV()
mpc.t = mpc.Param(value = mpc.time)

mpc.Equation(mpc.dl == (A+(K-A)/(1+20*mpc.exp(-mpc.t*0.05)))*mpc.g.dt())
mpc.Equation(mpc.pop.dt() == mpc.C*p.dl)

mpc.dl.STATUS = 1
mpc.beta.STATUS = 0
mpc.C.STATUS = 0
mpc.g.STATUS = 1

mpc.dl.FSTATUS = 0
mpc.beta.FSTATUS = 1
mpc.C.FSTATUS = 1
mpc.g.FSTATUS = 1
mpc.pop.FSTATUS = 1

mpc.dl.DCOST = 0.5

mpc.CV_TYPE = 1

setpoint = 0.0
mpc.pop.SPHI = setpoint+0.1
mpc.pop.SPLO = setpoint-0.1

mpc.pop.TR_INIT = 0
mpc.options.IMODE = 6

#----- Simulation Loop for TurboCat Demo -----#

population_meas = []
population_esti = []
g_meas = []
g_esti = []
C_esti = []
beta_esti = []
dl_cont = []
setpoints = []
plt.figure(figsize=(10,7))
plt.ion()
plt.show()
def SimulationLoop(sp):
    setpoint = sp
    mpc.pop.SPHI = setpoint+0.1
    mpc.pop.SPLO = setpoint-0.1
    setpoints.append(setpoint)

    mpc.beta.MEAS = mhe.beta.NEWVAL
    mpc.C.MEAS = mhe.C.NEWVAL

    if p.options.SOLVESTATUS == 1 :
        mpc.g.MEAS = p.g.MODEL
        mpc.pop.MEAS = p.pop.MODEL

    mpc.solve(disp = True, debug = True)
    dl_cont.append(mpc.dl.NEWVAL)
    p.dl.MEAS = dl_cont[dl_cont.size - 1]

    # import json
    # with open(mpc.path+'//results.json') as f:
    #      results = json.load(f)

    p.solve(disp = True, debug = True)
    population_meas.append(p.pop.MODEL + (random()*10 - 5))
    g_meas.append(p.g.MODEL + random()*0.1-0.05)

    mhe.dl.MEAS = dl_cont[dl_cont.size - 1]
    mhe.g.MEAS = g_meas[g_meas.size - 1]
    mhe.pop.MEAS = population_meas[population_meas.size - 1]

    mhe.solve(disp = True, debug = True)

    population_esti.append(mhe.pop.MODEL)
    g_esti.append(mhe.g.MODEL)
    C_esti.append(mhe.C.NEWVAL)
    beta_esti.append(mhe.beta.NEWVAL)
    plt.clf()
    plt.subplot(4,1,1)
    plt.plot(g_meas[0:i])
    plt.plot(g_esti[0:i])
    plt.legend(('meas','pred'))
    plt.ylabel('GFP')
    plt.subplot(4,1,2)
    plt.plot(np.ones(i)*p.C.value[0])
    plt.plot(beta_esti[0:i])
    plt.legend(('actual','pred'))
    plt.ylabel('beta value')
    plt.subplot(4,1,3)
    plt.plot(np.ones(i)*p.beta.value[0])
    plt.plot(C_esti[0:i])
    plt.legend(('actual','pred'))
    plt.ylabel('C value')
    plt.subplot(4,1,4)
    plt.plot(dl_cont[0:i])
    plt.legend('Output Control')
    plt.subplot(4,1,5)
    plt.plot(population_meas[0:i])
    plt.plot(population_esti[0:i])
    plt.plot(setpoints[0:i])
    plt.legend('meas', 'pred', 'setpoint')
    plt.draw()
    plt.pause(0.05)

#----- TEST OF SIMULATION LOCALLY -----#
i = 0
while i <= 21:
    i=i+1
    SimulationLoop(100)
