
import numpy as np
from typing import Iterable, Union, Type
from scipy.optimize import curve_fit



def coarse_grain(domain: np.ndarray, cg_factor:int) -> np.ndarray:
    """
    Re-scale original domain to a given resolution -- max resolution 1km
    """
    if 1 in np.isnan(domain):
        domain = np.where(np.isnan(domain), 0, domain)

    x_ind = 0
    new_xaxis = np.arange(0, domain.shape[0], cg_factor)
    new_yaxis = np.arange(0, domain.shape[1], cg_factor)
    cg_arr = np.zeros([len(new_xaxis), len(new_yaxis)])
    for row in new_xaxis:
        y_ind = 0
        for col in new_yaxis:
            patch = domain[row:row + cg_factor, col:col + cg_factor]
            av_value = np.sum(patch)
            cg_arr[x_ind][y_ind] = av_value

            y_ind += 1
        x_ind += 1
    cg_arr = cg_arr / cg_factor ** 2
    if 1 in np.isnan(domain):
        cg_arr[np.where(cg_arr == 0)] = np.nan

    return np.where(cg_arr > 0, 1, np.nan)

