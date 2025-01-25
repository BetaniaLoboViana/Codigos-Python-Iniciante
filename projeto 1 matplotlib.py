#Projeto 1 ML com matplotlib"

# Instalar as bibliotecas e dependencias primeiro

import matplotlib;

from sklearn.datasets import make_regression
x, y = make_regression(n_samples=200, n_features=1, noise=30)
import matplotlib.pyplot as plt


plt.scatter(x,y)
plt.show()


