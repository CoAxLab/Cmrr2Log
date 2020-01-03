#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

def create_format(dcm_path):
    
    import pydicom
    
    dcm = pydicom.read_file(dcm_path.absolute().as_posix())
    
    folder_name = dcm_path.parent.name
    base_name = dcm_path.name
    
    format_dict = {
            'p': str(dcm[0x00181030].value), 
            'd': str(dcm[0x0008103e].value),
            'i': str(dcm[0x00100020].value),
            's': str(dcm[0x00200011].value),
            't': str(dcm[0x00080020].value + "_" + dcm[0x00080030].value.split(".")[0]),
            'u': str(dcm[0x00200012].value),
            'x': str(dcm[0x00200010].value),
            'z': 'cmrr',
            'v': 'Siemens',
            'r': str(dcm[0x00200013].value),
            'n': str(dcm[0x00100010].value),
            'm': 'Si',
            'k': str(dcm[0x0020000d].value),
            'j': str(dcm[0x0020000e].value),
            'f': str(folder_name),
            'b': str(base_name),
            }
    
    return format_dict


    

