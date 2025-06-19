import numpy as np
import pylab as pl

x = np.linspace(-6, 6, 1000)
y = np.sin(x)

pl.plot(x, y, 'r--')
pl.savefig('sinfunction.pdf')
pl.show()

