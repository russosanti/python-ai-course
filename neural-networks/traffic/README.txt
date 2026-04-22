# Traffic Sign Classification - Model Experiments

## Overview

In this project, I experimented with different convolutional neural network (CNN) architectures to improve classification accuracy on the traffic sign dataset. Below are the configurations tested and their corresponding results.

---

## Experiments and Results

### 1. Baseline Model  
**Architecture:**
- 1 Convolutional layer  
- 1 Max Pooling layer  
- 1 Dense layer  

**Result:**
- Accuracy: **0.9650**
- Loss: **0.1531**

---

### 2. Two Convolutional Layers  
**Architecture:**
- 2 Convolutional layers  
- 2 Max Pooling layers  
- 1 Dense layer  

**Result:**
- Accuracy: **0.9855**
- Loss: **0.0621**

**Observation:**
Adding a second convolutional layer significantly improved performance, likely due to better feature extraction.

---

### 3. Three Convolutional Layers + Extra Dense Layer  
**Architecture:**
- 3 Convolutional layers  
- 3 Max Pooling layers  
- 2 Dense layers  

**Result:**
- Accuracy: **0.9873**
- Loss: **0.0467**

**Observation:**
Increasing depth and adding an additional dense layer further improved accuracy, but with diminishing returns.

---

### 4. Batch Normalization on All Layers  
**Architecture:**
- Batch normalization applied after all convolutional layers  

**Result:**
- Accuracy: **0.9742**

**Observation:**
Applying batch normalization everywhere reduced performance, possibly due to over-regularization or disrupting learned feature distributions.

---

### 5. Batch Normalization on First Two Layers  
**Architecture:**
- Batch normalization applied only to the first two convolutional layers  

**Result:**
- Accuracy: **0.9914**
- Loss: **0.0358**

**Observation:**
Selective use of batch normalization produced the best results, improving generalization without harming feature learning.

---

## Conclusion

- Adding more convolutional layers improves performance up to a point.
- Additional dense layers provide marginal gains.
- Batch normalization must be used carefully:
  - Overuse can hurt performance.
  - Strategic placement (early layers) yields the best results.

**Best performing model:**
- 3 convolutional layers  
- Batch normalization on first two layers  
- Accuracy: **99.14%**

---