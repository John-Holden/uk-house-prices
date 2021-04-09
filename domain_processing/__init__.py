import numpy as np
from typing import Union
from main import PATH_TO_DATA, PATH_TO_DIST

import matplotlib.pyplot as plt
import geopandas
from geopandas import GeoDataFrame


class UkPostCodes:

    def __init__(self, load_type='Areas'):
        self.type = load_type


    def load_post_code(self, pc: str):
        df = geopandas.read_file(f'{PATH_TO_DIST}/{self.type}.shp')
        df.boundary.plot()
        plt.show()
        ls_pc = [df.loc[i] for i, row in enumerate(df.name.str.contains(f'^{pc}') ) if row]


        assert 0


    def reset_domain(self):
        self.domain = np.copy(self._domain_raw_)

    def reshape(self, cg_factor:int) -> np.ndarray:
        from .domain_processing import coarse_grain
        self.domain = coarse_grain(self.domain, cg_factor)
        return self.domain


    def plot_domain(self, save:bool=False, title:Union[None, str]=None):
        from .plotting_methods import plot_map

        plot_map(self.domain, save, title)














