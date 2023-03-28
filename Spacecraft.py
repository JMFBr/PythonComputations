import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sats = pd.read_csv("Sat_Space.csv")

ranges = np.linspace(0,20000,2700)
numsats = sats.groupby(pd.cut(sats.APOGEE, ranges)).count()

num_np = numsats['APOGEE'].to_numpy()

# plt.plot(ranges[0:2699], num_np)
# plt.xlim(0,1500)
# plt.xlabel("Altitude (km)")
# plt.ylabel("Number of objects")
# plt.show()

