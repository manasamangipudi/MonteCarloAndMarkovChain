import scipy as sp
from scipy import stats
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import beta
import statistics

#data_binom = binom.rvs(n=2,p=0.5,size=1)
#print(data_binom[0])
alpha=1
beta1=1
eta = 0.90;    # Sensitivity
theta = 0.95;  # Specificity
r = 233;       # Rejected Emails
samples = 1000;      # Total number of emails
tau = r/samples      # Estimate of rejection rate P{R=1}
#print(tau)
psiorg = (tau + theta - 1)/(eta + theta -1)
print(psiorg)
N = 10000
psi=[0]*N
psi[0]=0.5
#print(psi)
for i in range(1,N):
    tau=psi[i-1]*eta+(1-psi[i-1])* (1-theta)  
    X= binom.rvs(n=r,p=psi[i-1]* eta/tau,size=1)
    Y=binom.rvs(n=samples-r,p=psi[i-1]*(1-eta)/(1-tau),size=1)
    psi[i]=beta.rvs(a=alpha+X[0]+Y[0],b=beta1+samples-X[0]-Y[0],size=1)[0]
print(statistics.mean(psi[2000:N+1]))
