from signal_generator import generate_signal
from noise_filter import moving_average
from classical_model import train_model
from quantum_model import quantum_predict
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Generate noisy data
X, y = generate_signal(200)

# Apply noise filter
X_filtered = moving_average(X.flatten())

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_filtered, y, test_size=0.2, random_state=42
)

# Classical
model = train_model(X_train, y_train)
y_pred_classical = model.predict(X_test)

# Quantum
y_pred_quantum = quantum_predict(X_test)

# Results
print("Classical Accuracy:", accuracy_score(y_test, y_pred_classical))
print("Quantum Accuracy:", accuracy_score(y_test, y_pred_quantum))
import matplotlib.pyplot as plt

# Plot comparison
models = ['Classical', 'Quantum']
accuracies = [
    accuracy_score(y_test, y_pred_classical),
    accuracy_score(y_test, y_pred_quantum)
]

plt.bar(models, accuracies)
plt.title("Classical vs Quantum Accuracy")
plt.ylabel("Accuracy")
plt.show()
import numpy as np

# Normalize data
X_train = X_train / np.max(np.abs(X_train)) * np.pi
X_test = X_test / np.max(np.abs(X_test)) * np.pi