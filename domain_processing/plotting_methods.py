import geopandas
import numpy as np
import matplotlib.pyplot as plt

pltParams = {'figure.figsize': (7.5, 5.5),
             'axes.labelsize': 15,
             'ytick.labelsize': 15,
             'xtick.labelsize': 15,
             'legend.fontsize': 'x-large'}

plt.rcParams.update(pltParams)


def plot_map(domain:np.ndarray, save, title):

    im = plt.imshow(domain)
    plt.colorbar(im)

    if title:
        plt.title(title)

    if save:
        plt.savefig('Domain')

    plt.show()
    plt.close()


def plot_shp_file(filepath):
    df = geopandas.read_file(filepath)

    df.plot()
    plt.savefig('all_post_codes.pdf')
    plt.show()
