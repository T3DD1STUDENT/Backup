import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x= np.random.rand(50,1) * 5
plt.figure(num="The powewer og love" ,figsize=(10,6))
plt.title("The Power of Love")
y=2*x+1+np.random.randn(50,1)*2
plt.scatter(x, y ,color='blue', label='RandomDataGenerated 1') 
plt.scatter(np.random.rand(50,1) * 5, y ,color='red', label='RandomDataGenerated 2',)
plt.xlabel("Hari")
plt.ylabel("Produc sold")
plt.legend()
plt.grid(True)

plt.show()

df_data=pd.DataFrame({'Data1': x.flatten(), 'y=Data2': y.flatten()}) # buat DataFrame / Dictionary dari data x dan y
print("\nDataFrame:\n", df_data)
