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

    #ax.axis('off')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #ax.tight_layout()

fig = plt.figure()
x,y = 6,6
ax1 = plt.subplot2grid((x, y), (0, 0))
ax2 = plt.subplot2grid((x, y), (0, 1), colspan=x, rowspan=1)
ax3 = plt.subplot2grid((x, y), (1, 0), colspan=1, rowspan=y)
ax4 = plt.subplot2grid((x, y), (1, 1), colspan=x, rowspan=y)


example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)

plt.tight_layout()

#plt.set_title('Title', fontsize=2)
#plt.ylabel('some numbers')

#plt.show()
plt.savefig('out03.png')





