# python -m pip install --verbose --no-build-isolation --editable .

import sys
import subprocess

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
