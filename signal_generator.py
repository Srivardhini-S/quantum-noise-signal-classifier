import numpy as np

def generate_signal(n=100):
    X = []
    y = []

    for i in range(n):
        signal = np.sin(np.random.rand()*10) + np.random.normal(0, 0.5)
        label = 1 if signal > 0 else 0
        
        X.append([signal])
        y.append(label)

    return np.array(X), np.array(y)