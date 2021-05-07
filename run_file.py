<<<<<<< HEAD
# # python -m pip install --verbose --no-build-isolation --editable .
=======
# python -m pip install --verbose --no-build-isolation --editable .
>>>>>>> e9663175df63bca0c059409ef58b78094ce15703

import sys
import subprocess

<<<<<<< HEAD
# #
# #  # implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--verbose','--no-build-isolation','--editable','.'])

# from sklearn.tree import LinearDecisionTreeRegressor, DecisionTreeRegressor
# from sklearn.metrics import mean_squared_error
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import make_regression


# #inp1 = int(input("Enter number of examples you want:"))
# m = 100
# np.random.seed(42)
# X = np.random.rand(m, 1)
# X= np.sort(X, axis= 0)
# y = 4 * (X[:, 0] - 0.5) ** 2 #+ 4 * (X[:, 1] - 0.5)**2 + 4 * (X[:, 2] - 0.5)**3
# y = y + np.random.randn(m,) / 10

# #X, y= make_regression(n_features= 4, random_state=42)


# x_test= X[:20]
# y_test= y[:20]

# X= X[20:]
# y= y[20:]

# print("shape:", X.shape)

# inp2 = 2#int(input("Enter the Depth of the tree:"))

# ldtr = LinearDecisionTreeRegressor(max_depth = inp2)
# ldtr.fit(X,y)

# y_pred= ldtr.predict(X)
# print("error",mean_squared_error(y, y_pred), mean_squared_error(y_test, ldtr.predict(x_test)))
# ldtr = DecisionTreeRegressor(max_depth = inp2)
# ldtr.fit(X,y)

# y_pred1= ldtr.predict(X)
# print("error normal", mean_squared_error(y, y_pred1), mean_squared_error(y_test, ldtr.predict(x_test)))

# plt.scatter(X[:, 0], y)
# plt.scatter(X[:, 0], y_pred)
# plt.scatter(X[:, 0], y_pred1)
# plt.show()

# plt.scatter(X[:, 1], y)
# plt.scatter(X[:, 1], y_pred)
# plt.scatter(X[:, 1], y_pred1)
# plt.show()

# plt.scatter(X[:, 2], y)
# plt.scatter(X[:, 2], y_pred)
# plt.scatter(X[:, 2], y_pred1)
# plt.show()

# import sklearn
# print(sklearn)
=======
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--verbose','--no-build-isolation','--editable','.'])

from sklearn.tree import LinearDecisionTreeRegressor
import numpy as np

inp1 = int(input("Enter number of examples you want:"))
m = inp1
np.random.seed(42)
X = np.random.rand(m, 1)
y = 4 * (X - 0.5) ** 2
y = y + np.random.randn(m, 1) / 10

inp2 = int(input("Enter the Depth of the tree:"))

ldtr = LinearDecisionTreeRegressor(max_depth = inp2)
ldtr.fit(X,y)
>>>>>>> e9663175df63bca0c059409ef58b78094ce15703
