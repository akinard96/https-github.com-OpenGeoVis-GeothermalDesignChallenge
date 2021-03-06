"""utilities for setting up your working directory"""

import os
import glob

import gdc19


def _get_path(folder, filename=None):
    if filename is None:
        return os.path.join(gdc19.DATA_DIRECTORY, folder)
    return os.path.join(os.path.join(gdc19.DATA_DIRECTORY, folder), filename)


def set_data_directory(path):
    """This will set the root directory of the data folder. This is likely the
    `utah-forge` Google Drive folder that was shared with you
    """
    gdc19.DATA_DIRECTORY = path
    return gdc19.DATA_DIRECTORY

def get_data_directory():
    """Returns the root directory for the data files"""
    return gdc19.DATA_DIRECTORY

def get_drilling_path(filename=None):
    return _get_path('drilling', filename)

def get_gis_path(filename=None):
    return _get_path('gis', filename)

def get_web_path(filename=None):
    return get_gis_path('web-friendly/{}'.format(filename))

def get_shp_path(filename=''):
    filename = os.path.join('Roosevelt Hot Springs FORGE Site Outline', filename)
    return get_gis_path(filename=filename)

def get_injection_path(filename=None):
    return _get_path('injection', filename)

def get_surfaces_path(filename=None):
    return _get_path('surfaces', filename)

def get_temperature_path(filename=None):
    return _get_path('temperature', filename)

def get_well_path(filename=None):
    return _get_path('well', filename)

def get_krig_path(filename=None):
    return _get_path('geotherm-export', filename)

def get_bad_path(filename=None):
    return get_well_path('bad-conversions/{}'.format(filename))

def get_well_vtm_path(filename=None):
    return get_well_path('VTM-AGGREGATED/{}'.format(filename))

def get_well_vtm_file():
    return get_well_path('VTM-AGGREGATED/WELLS.vtm')

def get_tem_path(filename=None):
    return _get_path('TEM', filename)

def get_gravity_path(filename=None):
    return _get_path('gravity', filename)

def list_filenames(folder):
    """List all the filenames in a given subfolder of the project data"""
    full = glob.glob(os.path.join(_get_path(folder), '*'))
    ignore = ['Icon',]
    return [os.path.basename(f.strip()) for f in full if os.path.basename(f.strip()) not in ignore]

def get_project_path(filename):
    return os.path.join(get_data_directory(), filename)

def get_omf_project_filename():
    return get_project_path('FORGE.omf')
