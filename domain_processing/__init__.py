import re
from main import PATH_TO_DIST, PATH_TO_DATA

import geopandas
import numpy as np
import contextily as ctx

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

class UkPostCodes:

    def __init__(self, load_type='Areas'):
        self.type = load_type

    def load_post_code(self, pc: str):
        # load post-codes
        assert self.is_valid(pc)

        gdf = geopandas.read_file(f'{PATH_TO_DIST}/{self.type}.shp')
        gdf.set_crs(epsg=4326, inplace=True)  # set projection
        gdf = gdf[gdf.name.str.match(self.get_re(pc))]  # filter by post-code
        gdf['avg_price'] = np.linspace(50, 300, gdf.shape[0])
        fig, ax = plt.subplots(figsize=(10, 10))
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="2%", pad=-2)
        gdf.plot(column='avg_price', ax=ax, legend=True, cax=cax, edgecolor='white')
        ax.set_title(f'{pc} avg_price $1000`s')
        ax.axis('off')
        plt.show()


    @staticmethod
    def is_valid(pc: str) -> bool:
        """check a post-code is valid"""
        if re.match(r'^[Ll][Ss]', pc):
            return True
        return False

    def get_re(self, pc):
        if re.match(r'^[Ll][Ss]$', pc) and self.type == 'Districts':
            return rf'^{pc}.*'
        elif re.match(r'^[Ll][Ss]\d{1,2}', pc) and self.type == 'Districts' or self.type == 'Sectors':
            return rf'^{pc}$'












