# -*- coding: cp1252 -*-

import matplotlib.pyplot as plt
import warnings

import random
fontsizes = [8, 16, 24, 32]


def example_plot(ax):
    ax.plot([1, 2])
    #ax.set_xlabel('x-label', fontsize=random.choice(fontsizes))
    #ax.set_ylabel('y-label', fontsize=random.choice(fontsizes))
    #ax.set_title('Title', fontsize=random.choice(fontsizes))

fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0))
ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2, rowspan=1)
ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=1, rowspan=2)
ax4 = plt.subplot2grid((3, 3), (1, 1), colspan=2, rowspan=2)


example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)

plt.tight_layout()

plt.show()





