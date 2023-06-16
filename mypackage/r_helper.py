import os
from subprocess import check_output

# global var that stores the paths to the config files
config_dir = {}

def check_r_install():
    base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

    if not os.path.isfile(os.path.join(base_path, 'R.conf')):
        with open(os.path.join(base_path, 'R.conf'), 'w') as wf:
            wf.write(f"R = PATH_TO_RSCRIPT\nRFUNCTIONS = {os.path.join(base_path, 'RFunctions.R')}")
        raise OSError('No R installation configured. Generated autoprot.conf. Please edit and try again.')
    else:
        with open(os.path.join(base_path, 'R.conf'), 'r') as rf:
            for line in rf:
                splitline = [x.strip() for x in line.split('=')]
                if len(splitline) == 2:
                    k, v = [x.strip() for x in line.split('=')]
                    global config_dir
                    config_dir[k] = v

    if not os.path.isfile(config_dir['R']):
        raise OSError(
            'The R variable should point to the Rscript executable. Make sure that it is not the R executable.')

    if not os.path.isfile(config_dir['RFUNCTIONS']):
        raise OSError(f'The RFUNCTIONS variable should point to the RFunctions.R file in your local autoprot '
                      f'directory and not to {config_dir["RFUNCTIONS"]}')


def return_r_path():
    check_r_install()
    return config_dir['RFUNCTIONS'], config_dir['R']
