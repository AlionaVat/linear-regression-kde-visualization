import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Generate Sample Data
np.random.seed(42)
x = np.random.rand(100) * 10
y = 3 * x + np.random.normal(0, 3, 100)

data = pd.DataFrame({'X': x, 'Y': y})

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    data[['X']], data['Y'], test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Plot KDE
plt.figure(figsize=(8, 5))
sns.kdeplot(y_test, label='Actual', fill=True)
sns.kdeplot(y_pred, label='Predicted', fill=True)

plt.xlabel('Target Variable')
plt.ylabel('Density')
plt.title('KDE Plot of Actual vs Predicted Values')
plt.legend()
plt.show()
