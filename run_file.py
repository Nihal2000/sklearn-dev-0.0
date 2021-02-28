# python -m pip install --verbose --no-build-isolation --editable .

import sys
import subprocess

# # implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--verbose','--no-build-isolation','--editable','.'])

from sklearn.tree import DecisionTreeRegressor
import numpy as np
import matplotlib.pyplot as plt


#inp1 = int(input("Enter number of examples you want:"))
m = 20
np.random.seed(42)
X = np.random.rand(m, 1)
X= np.sort(X, axis= 0)
y = 4 * (X - 0.5) ** 2
y = y + np.random.randn(m, 1) / 10

inp2 = 1#int(input("Enter the Depth of the tree:"))

ldtr = DecisionTreeRegressor(max_depth = inp2)
ldtr.fit(X,y)

y_pred= ldtr.predict(X)

print(X, y_pred)

plt.scatter(X, y)
plt.scatter(X, y_pred)
plt.show()