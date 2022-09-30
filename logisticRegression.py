import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.metrics import accuracy_score, confusion_matrix


plt.style.use("ggplot")

# Good luck!


#hold b constant


class LogisticRegression():
    def __init__(self):
        self.b=0     
        self.m = VariableSingleInput()
    def yHat(x, m):
        return 1/(1+(-1*x*m).epow())
    def fit(self, X, y):
        print(X.size())
        
        
    
    
    
X = np.array([1, 2, 3, 3, 4, 4, 5, 5.5])
y = np.array([0, 0, 0, 1, 0, 1, 1, 1])
model = LogisticRegression()
model.fit(X, y)

y_preds = model.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_preds)

X


 