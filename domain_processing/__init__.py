import re
from main import PATH_TO_DIST

import geopandas
from geopandas import GeoDataFrame
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


class UkPostCodes:

    def __init__(self, load_type='Areas'):
        self.type = load_type
        self.pc = None
        self.gdf_obj_raw = None

    def load_post_code(self, pc: str) -> GeoDataFrame:
        """
        Load uk-post code from shape file
        :param pc: post-code
        :return:
        """
        assert self.is_valid(pc)
        self.pc = pc
        gdf = geopandas.read_file(f'{PATH_TO_DIST}/{self.type}.shp')
        gdf.set_crs(epsg=4326, inplace=True)  # set projection
        self.gdf_obj_raw = gdf.copy()
        gdf = gdf[gdf.name.str.match(self.get_re(pc))]  # filter by post-code
        return gdf

    @staticmethod
    def add_metric(gdf: GeoDataFrame, metric: str) -> GeoDataFrame:
        """

        :param gdf: current geo-pandas dataframe
        :param metric: metric to add to geo-pandas dataframe
        :return:
        """
        assert 'avg' in metric, f'Error avg-price only implemented'
        gdf['avg_price'] = np.linspace(50, 300, gdf.shape[0])
        return gdf

    @staticmethod
    def is_valid(pc: str) -> bool:
        """check a post-code is valid"""
        if re.match(r'^[Ll][Ss]', pc):
            return True
        return False

    def get_re(self, pc):
        """derive regular expression for post-code type combination"""
        if re.match(r'^[Ll][Ss]$', pc) and self.type == 'Districts':
            return rf'^{pc}.*'
        elif re.match(r'^[Ll][Ss]\d{1,2}', pc) and self.type == 'Districts' or self.type == 'Sectors':
            return rf'^{pc}$'

        raise NotImplementedError

    def plot_pc(self, gdf: GeoDataFrame):
        """
        plot geopandas dataframe
        :param gdf:
        :return:
        """
        assert self.pc, f'Error, supply postcode'

        fig, ax = plt.subplots(figsize=(10, 10))
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="2%", pad=-2)
        gdf.plot(column='avg_price', ax=ax, legend=True, cax=cax, edgecolor='white')
        ax.set_title(f'{self.pc} avg_price $1000`s')
        ax.axis('off')
        plt.show()











