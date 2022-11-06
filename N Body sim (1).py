#!/usr/bin/env python
# coding: utf-8

# In[42]:


import rebound
import numpy as np
import matplotlib.pyplot as plt

sim = rebound.Simulation()

sim.units = ['mearth', 'day', 'AU']
sim.add(m= 333000) ## the sun at 0,0 coords
sim.add(m=317.8, P=4330.3, e=0.048775) ## jupiter
sim.add(m= 3.6837408053*10**-11, P= 27375, e=.97) ##halley's comet


# In[43]:


sim.status()


# In[44]:


rebound.OrbitPlot(sim)
plt.show()

