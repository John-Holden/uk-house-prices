import os
from domain_processing.plotting_methods import plot_shp_file

PATH_TO_DATA = f'{os.getcwd()}/data_store'
PATH_TO_DIST = f'{os.getcwd()}/data_store/Distribution'


if __name__ == '__main__':
    from domain_processing import UkPostCodes
    post_codes = UkPostCodes('Districts')
    post_codes.load_post_code('LS')

