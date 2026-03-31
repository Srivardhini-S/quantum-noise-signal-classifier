# Quantum Noise-Aware Signal Classifier

This project presents a simple hybrid approach combining classical machine learning and quantum computing for signal classification.

The system generates noisy signal data, applies basic filtering, and compares the performance of a classical model with a quantum circuit-based model.



## Overview

The goal of this project is to explore how quantum circuits can be used alongside traditional machine learning methods for classification tasks, especially in scenarios involving noisy signals.



## Features

* Synthetic noisy signal generation
* Noise reduction using moving average filtering
* Classical classification using Logistic Regression
* Quantum-based prediction using Qiskit
* Performance comparison between classical and quantum approaches
* Visualization of results



## How to Run

Install dependencies:

```bash id="p8mr53"
pip install -r requirements.txt
```

Run the project:

```bash id="6ys96x"
python main.py
```



## Output

* Displays accuracy of both models in the terminal
* Generates a bar graph comparing classical and quantum performance



## Technologies Used

* Python
* Qiskit
* Scikit-learn
* NumPy
* Matplotlib



## Future Scope

* Implementation of trainable quantum circuits (VQC)
* Use of multi-qubit systems for better performance
* Integration with real-world signal datasets
* Extension to advanced sensing applications



## Author

Srivardhini
