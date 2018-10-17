import numpy as np
from random import random
from gekko import GEKKO
import matplotlib.pyplot as plt

Q = 1
beta = 1
nu = 1
#----- Moving Horizon Estimation Model Setup -----#

mhe = GEKKO()
mhe.dl = mhe.MV() #output
mhe.A = mhe.FV(value = 1, lb = 1, ub = 3)
mhe.K = mhe.FV(value = 1, lb = 1, ub = 3)
mhe.g = mhe.CV() #measured control variable

def SUM(init, final, args):
    #sum here
def LOGISTICMHE(a, k, t):
    return a+(k-a)/((C+Q*mhe.exp(-beta*t))**(1/nu))

    #logistic here

mhe.Equation(mhe.dl == SUM(i,f,mhe.g.dt()*LOGISTIC(A,K)))
mhe.options.IMODE = 5
mhe.options.EV_TYPE = 1
mhe.options.DIAGLEVEL = 0

# STATUS = 0, optimizer doesn't adjust value
# STATUS = 1, optimizer can adjust
mhe.dl.STATUS = 0
mhe.A.STATUS = 1
mhe.K.STATUS = 1
mhe.g.STATUS = 1

# FSTATUS = 0, no measurement
# FSTATUS = 1, measurement used to update model
mhe.dl.FSTATUS = 1
mhe.A.FSTATUS = 0
mhe.K.FSTATUS = 0
mhe.g.FSTATUS = 1

mhe.A.DMAX = ADMax
mhe.K.DMAX = KDMax

mhe.g.MEAS_GAP = 0.01

mhe.g.TR_INIT = 1

#----- Model Predictive Control Setup -----#

mpc = GEKKO()

mpc.dl = mpc.MV()
mpc.A = mpc.FV()
mpc.K = mpc.FV()
mpc.g = mpc.CV()

mpc.Equation(mpc.dl == SUM(i,f,mpc.g.dt()*LOGISTIC(A,K)))
