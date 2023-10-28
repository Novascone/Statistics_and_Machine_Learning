import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# rows and columns
rows = 30
columns = 6

# initialize array
data = np.zeros((rows,columns))

# fill with data
for i in range(columns):
    data[:,i] = 30*np.random.randn(rows) * (2*i/(columns-1)-1)**2 + (i+1)**2
    
# plot
fig,ax = plt.subplots(1,3,figsize=(8,2))

bars
ax[0].bar(range(columns), np.mean(data,axis=0))
ax[0].set_title('Bar Plot')

# error bars
ax[1].errorbar(range(columns),np.mean(data,axis=0),np.std(data, axis=0, ddof=1), marker='s',linestyle='')
ax[1].set_title('Errorbar Plot')

# both
ax[2].bar(range(columns), np.mean(data,axis=0))
ax[2].errorbar(range(columns),np.mean(data,axis=0),np.std(data, axis=0, ddof=1), marker='s',linestyle='',color='black')
ax[2].set_title('Error+bar Plot')

plt.show()


# xcrossings = [ 1, 2, 4, 5, 6, 9]

# plt.bar(xcrossings,np.mean(data,axis=0))
# plt.errorbar(xcrossings,np.mean(data,axis=0),np.std(data,axis=0,ddof=1),marker='.',linestyle='',color='black')
# plt.xticks(xcrossings)
# plt.title('Bar+error plot')

# plt.show()

# M = [ [2,5,4,3], [1,1,8,6] ]

# fig,ax = plt.subplots(nrows=2,ncols=2,figsize=(8,8))

# ax[0,0].imshow(M)

# df = pd.DataFrame(M, columns=['prop 0', 'prop 1', 'prop 2', 'prop 3'])
# df.plot(ax=ax[1,0],kind='bar')
# ax[1,0].set_title('Grouping by rows')

# ax[0,1].imshow(np.array(M).T)
# df.T.plot(ax=ax[1,1],kind='bar')
# ax[1,1].set_title('Grouping by columns')

# plt.show()