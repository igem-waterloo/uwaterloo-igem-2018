import numpy as np
from random import random
from gekko import GEKKO
import matplotlib.pyplot as plt


#----- Process Simulation Setup -----#

p = GEKKO()
p.time = [0,0.5]
p.dl = p.MV()
p.beta = p.Param(value=0.05)
p.pop = p.SV()
p.g = p.CV()
p.C = p.Param(value=1)

A = 20
K = 300
p.Equation(p.dl.dt() == (A+(K-A)/(1+20*p.exp(-t*p.beta)))*p.g)
p.Equation(p.pop.dt() == p.C*p.dl.dt())

p.Options.IMODE = 4

#----- Moving Horizon Estimation Model Setup -----#

mhe = GEKKO()
mhe.dl = mhe.MV() #output
mhe.beta = mhe.FV(value = 0.01, lb = 0.0000001, ub = 0.5)
mhe.C = mhe.FV(value = 1, lb = 0.001, ub = 5)
mhe.g = mhe.SV() #measured variable
mhe.pop = mhe.CV()

mhe.Equation(mhe.dl.dt() == (A+(K-A)/(1+20*mhe.exp(-t*0.05)))*mhe.g)
mhe.Equation(mhe.pop.dt() == mhe.C*p.dl.dt())
mhe.options.IMODE = 5
mhe.options.EV_TYPE = 1
mhe.options.DIAGLEVEL = 0

# STATUS = 0, optimizer doesn't adjust value
# STATUS = 1, optimizer can adjust
mhe.dl.STATUS = 0
mhe.beta.STATUS = 1
mhe.g.STATUS = 1
mhe.C.STATUS = 1
mhe.pop.STATUS = 1

# FSTATUS = 0, no measurement
# FSTATUS = 1, measurement used to update model
mhe.dl.FSTATUS = 1
mhe.beta.FSTATUS = 0
mhe.g.FSTATUS = 1
mhe.C.FSTATUS = 0
mhe.pop.FSTATUS = 1

mhe.beta.DMAX = 0.01
mhe.C.DMAX = 0.01

mhe.g.MEAS_GAP = 0.01

mhe.g.TR_INIT = 1

#----- Model Predictive Control Setup -----#

mpc = GEKKO()

mpc.dl = mpc.MV(lb = 0, ub = 1)
mpc.beta = mpc.FV(value = 0.01, lb = 0.0000001, ub = 0.5)
mpc.C = mpc.FV(value = 1, lb = 0.001, ub = 5)
mpc.g = mpc.SV()
mhe.pop = mhe.CV()

mpc.Equation(mpc.dl.dt() == (A+(K-A)/(1+20*mpc.exp(-t*0.05)))*mpc.g)
mpc.Equation(mpc.pop.dt() == mpc.C*p.dl.dt())

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


#----- Simulation Loop for TurboCat Demo -----#

population_meas = np.array([])
population_esti = np.array([])
g_meas = np.array([])
g_esti = np.array([])
C_esti = np.array([])
beta_esti = np.array([])
dl_cont = np.array([])
setpoints = np.array([])

def SimulationLoop(sp):
    setpoint = sp
    mpc.pop.SPHI = setpoint+0.1
    mpc.pop.SPLO = setpoint-0.1
    setpoints = np.append(setpoints, [setpoint])

    mpc.beta.MEAS = mhe.beta.NEWVAL
    mpc.C.MEAS = mhe.C.NEWVAL

    if p.OPTIONS.SOLVESTATUS == 1 :
        mpc.g.MEAS = p.g.MODEL
        mpc.pop.MEAS = p.pop.MODEL

    mpc.solve(disp = True, debug = True)
    dl_cont = np.append(dl_cont, [mpc.dl.NEWVAL])
    p.dl.MEAS = dl_cont[dl_cont.size - 1]

    # import json
    # with open(mpc.path+'//results.json') as f:
    #     results = json.load(f)

    p.solve(disp = True, debug = True)
    population_meas = np.append(population_meas, p.pop.MODEL + (random()*10 - 5))
    g_meas = np.append(g_meas, p.g.MODEL + random()*0.1-0.05)

    mhe.dl.MEAS = dl_cont[dl_cont.size - 1]
    mhe.g.MEAS = g_meas[g_meas.size - 1]
    mhe.pop.MEAS = population_meas[population_meas.size - 1]

    mhe.solve(disp = True, debug = True)

    population_esti = np.append(population_esti, [mhe.pop.MODEL])
    g_esti = np.append(g_esti, [mhe.g.MODEL])
    C_esti = np.append(C_esti, [mhe.C.NEWVAL])
    beta_esti = np.append(beta_esti, [mhe.beta.NEWVAL])

#----- TEST OF SIMULATION LOCALLY -----#
i = 0
plt.figure(figsize=(10,7))
plt.ion()
plt.show()
while i < 21:
    i=i+1
    SimulationLoop(100)
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
