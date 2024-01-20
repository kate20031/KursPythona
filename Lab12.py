import numpy as np

data = np.array([[1.0, 1.3, 0],
                 [2.2, 1.1, 1],
                 [2.0, 2.4, 1],
                 [1.5, 3.2, 0],
                 [3.2, 1.2, 1]])


def mean_squared_error(y_real, y_pred):
    return np.mean((y_real - y_pred) ** 2)


w0_val = np.arange(0, 1.1, 0.1)
w1_val = np.arange(2, 3.1, 0.1)

mse_results = np.zeros((len(w0_val), len(w1_val)))

for i, w0 in enumerate(w0_val):
    for j, w1 in enumerate(w1_val):
        y_pred = 1 / (1 + np.exp(-(w0 * data[:, 0] + w1 * data[:, 1])))

        mse_results[i, j] = mean_squared_error(data[:, 2], y_pred)

print("Wyniki:")
print(mse_results)
