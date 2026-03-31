import numpy as np

def moving_average(signal, window=3):
    filtered = []
    
    for i in range(len(signal)):
        start = max(0, i - window)
        filtered.append(np.mean(signal[start:i+1]))
    
    return np.array(filtered).reshape(-1,1)