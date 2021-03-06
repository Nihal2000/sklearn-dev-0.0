# python -m pip install --verbose --no-build-isolation --editable .

import sys
import subprocess

# # implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--verbose','--no-build-isolation','--editable','.'])

from sklearn.tree import LinearDecisionTreeRegressor
import numpy as np
import matplotlib.pyplot as plt


#inp1 = int(input("Enter number of examples you want:"))
m = 100
np.random.seed(42)
X = np.random.rand(m, 2)
#X= np.sort(X, axis= 0)
y = 4 * (X[:, 0] - 0.5) ** 2 + 4 * (X[:, 1] - 0.5) ** 2
y = y + np.random.randn(m,) / 10

inp2 = 2#int(input("Enter the Depth of the tree:"))

ldtr = LinearDecisionTreeRegressor(max_depth = inp2)
ldtr.fit(X,y)

y_pred= ldtr.predict(X)

print(np.unique(y_pred))

plt.scatter(X, y)
plt.scatter(X, y_pred)
plt.show()