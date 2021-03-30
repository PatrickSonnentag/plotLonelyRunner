# MIT License
#
# Copyright (c) 2021 Patrick Sonnentag
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
import matplotlib.pyplot as plt

v = [3, 1, 2]  # Speeds of all moving runners
max_t = 1.001  # (Exclusive) max t to which values will be calculated
delta_t = 0.001
numberOfRunners = len(v)


def function_f():
    solutions = []

    for t in np.arange(0, max_t, delta_t):
        is_lonely = 0
        solution = complex(0, 0)

        for y in v:
            angle = 2 * np.pi * y * t

            # Reduces the angle until it is within [0; 2pi)
            while angle >= 2 * np.pi:
                angle -= 2 * np.pi

            # Increases the angle until it is within [0; 2pi)
            while angle < 0:
                angle += 2 * np.pi

            solution += np.divide(np.exp(angle * complex(0, 1)), 2 * np.pi)

            if (np.divide(2 * np.pi, 2 * (numberOfRunners + 1)) < angle <
                    2 * np.pi - np.divide(2 * np.pi, 2 * (numberOfRunners + 1))):
                is_lonely += 1
        solutions.append([solution, is_lonely])
    return solutions


def plot():
    function_points = function_f()

    for pointValues in function_points:

        if pointValues[1] != numberOfRunners:
            plt.scatter(pointValues[0].real, pointValues[0].imag, c='red', s=2)

        else:
            plt.scatter(pointValues[0].real, pointValues[0].imag, c='green', s=2)
    plt.show()


plot()
