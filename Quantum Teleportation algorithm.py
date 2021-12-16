#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *


# In[2]:


circuit = QuantumCircuit(3,3)


# In[3]:


circuit.x(0)
circuit.barrier()


# In[4]:


circuit.h(1)
circuit.cx(1,2)
circuit.barrier()


# In[5]:


circuit.cx(0,1)
circuit.h(0)
circuit.barrier()


# In[6]:


circuit.measure([0, 1], [0, 1])
circuit.barrier()


# In[7]:


circuit.cx(1, 2)
circuit.cz(0, 2)


# In[8]:


circuit.measure([2], [2])


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
circuit.draw(output='mpl')


# In[10]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots=1024).result()
from qiskit.visualization import plot_histogram
plot_histogram(result.get_counts(circuit))


# In[ ]:





# In[ ]:




