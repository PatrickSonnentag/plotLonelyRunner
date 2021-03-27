import numpy as np
import matplotlib.pyplot as plt

v = [3, -1, 3, -0.5]
max_t = 10.001
t_steps = 0.001
numberOfRunners = len(v)


def function_f():
    solutions = []
    for t in np.arange(0, max_t, t_steps):
        is_lonely = 0
        solution = complex(0, 0)
        for y in v:
            angle = 2 * np.pi * y * t
            while angle >= 2 * np.pi:
                angle -= 2 * np.pi
            while angle <= -2 * np.pi:
                angle += 2 * np.pi
            if angle < 0:
                angle += 2 * np.pi
            solution += np.divide(np.exp(angle * complex(0, 1)), 2 * np.pi)
            if (np.divide(2 * np.pi, 2 * (numberOfRunners + 1)) < angle <
                    2 * np.pi - np.divide(2 * np.pi, 2 * (numberOfRunners + 1))):
                is_lonely += 1
            solutions.append([solution, is_lonely])
    return solutions


def plot():
    function = function_f()
    for pointValues in function:
        if pointValues[1] != numberOfRunners:
            plt.scatter(pointValues[0].real, pointValues[0].imag, c='red', s=2)
        else:
            plt.scatter(pointValues[0].real, pointValues[0].imag, c='green', s=2)
    plt.show()


plot()
