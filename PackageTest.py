from symbulate import *
import matplotlib
import matplotlib.pyplot as plt

x = RV(Binomial(4, 0.5)).sim(10000)
plt.figure()
x.plot()
plt.show()
print(x)