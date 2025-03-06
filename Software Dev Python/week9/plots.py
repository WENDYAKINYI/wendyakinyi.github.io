# Assignment 9.3:
# Use only methods from numpy and matplotlib.
# Display the plot of one period of both the cosine and sine. They should appear on the same axes. Label the axes and the plot. Provide a grid.
# Display the plot of one period of both the cosine and sine. They should appear on the different axes but share the y-axis. Label the axes and the plot. Provide a grid.
# Display the plot of one period of both the cosine and sine. They should appear on the different axes but share the x-axis. Label the axes and the plot. Provide a grid.


import matplotlib.pyplot as plt
import numpy as np


def plot_functions():
    """
    Plots one period of both cosine and sine functions using NumPy and Matplotlib.

    This function plots the cosine and sine functions on the same axes,
    on different axes sharing the y-axis, and on different axes sharing the x-axis.
    """
    # Values for one period of cosine and sine
    x = np.linspace(0, 2 * np.pi, 1000)
    cosine_values = np.cos(x)
    sine_values = np.sin(x)

    # Plot of one period cosine and sine on the same axes
    plt.figure(figsize=(8, 6))
    plt.plot(x, cosine_values, label='Cosine', color='blue')
    plt.plot(x, sine_values, label='Sine', color='red')
    plt.title('Plot of one period of Cosine and Sine')
    plt.xlabel('Angle (radians)')
    plt.ylabel('Value')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Plot of both cosine and sine on different axes but sharing the y-axis
    fig, (ax1, ax2) = plt.subplots(2, 1, sharey=True, figsize=(8, 6))
    ax1.plot(x, cosine_values, label='Cosine', color='blue')
    ax1.set_title('Cosine')
    ax1.set_xlabel('Angle (radians)')
    ax1.set_ylabel('Value')
    ax1.grid(True)

    ax2.plot(x, sine_values, label='Sine', color='red')
    ax2.set_title('Sine')
    ax2.set_xlabel('Angle (radians)')
    ax2.set_ylabel('Value')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

    # Plot of both cosine and sine on different axes but sharing the x-axis
    fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, figsize=(10, 4))
    ax1.plot(x, cosine_values, label='Cosine', color='blue')
    ax1.set_title('Cosine')
    ax1.set_xlabel('Angle (radians)')
    ax1.set_ylabel('Value')
    ax1.grid(True)

    ax2.plot(x, sine_values, label='Sine', color='red')
    ax2.set_title('Sine')
    ax2.set_xlabel('Angle (radians)')
    ax2.set_ylabel('Value')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

    return


if __name__ == "__main__":
    plot_functions()
