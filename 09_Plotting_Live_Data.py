import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('ggplot')

x = []
y = []

index = count()

def animate(i):
    data = pd.read_csv('data/gen_data.csv')
    x = data['x']
    y1 = data['ch1']
    y2 = data['ch2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=200)
plt.tight_layout()
plt.show()
