import numpy as np
from typing import Union
from main import PATH_TO_DATA


class UkPostCodes:

    def __init__(self):
        self._domain_raw_ = np.load(f'{PATH_TO_DATA}/uk_isle_shape.npy')
        self.domain = np.copy(self._domain_raw_)

    def reset_domain(self):
        self.domain = np.copy(self._domain_raw_)

    def reshape(self, cg_factor:int) -> np.ndarray:
        from .domain_processing import coarse_grain
        self.domain = coarse_grain(self.domain, cg_factor)
        return self.domain


    def plot_domain(self, save:bool=False, title:Union[None, str]=None):
        from .plotting_methods import plot_map

        plot_map(self.domain, save, title)














