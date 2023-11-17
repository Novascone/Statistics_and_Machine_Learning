import numpy as np
import matplotlib.pyplot as plt
from statsmodels import robust
import scipy.stats as stats

N = 400

data = np.random.randn(N)
samples = np.arange(1,401)
print(samples)
data = np.random.randn(N)**4
#  z

dataZ = (data-np.mean(data)) / np.std(data)

# compute modified z

dataMed = np.median(data)
dataMAD = robust.mad(data)

dataMz = stats.norm.ppf(.75)*(data-dataMed) / dataMAD

fig, ax = plt.subplots(2,1,figsize=(8,6))
ax[0].plot(samples,dataZ)
ax[0].set_xlabel('Number of data points')
ax[0].set_ylabel('Z')

ax[1].plot(samples,dataMz)
ax[1].set_xlabel('Number of data points')
ax[1].set_ylabel('Modified Z')
# plt.plot(samples,dataZ)
# plt.plot(samples,dataZ)



plt.show()