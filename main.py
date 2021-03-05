import os

PATH_TO_DATA = f'{os.getcwd()}/data_store'


def test_me():
    from domain_processing import UkPostCodes

    post_codes = UkPostCodes()
    post_codes.plot_domain(title='fill me with fucking data you bladddy LEGGGEND!!!')

    cg_factor = 25
    post_codes.reshape(cg_factor)
    post_codes.plot_domain(title=f'I have been re-shpaed to {cg_factor}km^2 ')

    post_codes.reset_domain()
    post_codes.plot_domain(title='I have been reset...')



if __name__ == '__main__':
    test_me()

