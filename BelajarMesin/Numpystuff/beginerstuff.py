# install scikit-learn
# pip install scikit-learn
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # untuk visualisasi data

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

np.random.seed(42) # set seed untuk reproducibility

#generate nilai x
x=np.random.rand(100,1) * 10 # 100 data acak antara 0-10
# print(x)

#generate nilai y dengan linear relation dengan x
y= 2*x+1+np.random.randn(100,1)*2 # y = 2x + 1 + noise
plt.figure(figsize=(10, 6))
plt.title('Random Data Generated')

plt.scatter(x,y, color='blue', label='RandomDataGenerated')

plt.show()