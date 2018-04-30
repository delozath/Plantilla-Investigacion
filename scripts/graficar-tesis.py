import numpy as np
import matplotlib.pyplot as plt

t   = np .linspace(1,15,1000)
trs = plt.plot(  t,np.sin(2*np.pi*t)  )
trs = plt.show()
