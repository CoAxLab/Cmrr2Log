#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from pathlib import Path
import json
from argparse import ArgumentParser
from argparse import ArgumentDefaultsHelpFormatter
from .extract_cmrr import extract_cmrr_physio
from .utils import (create_format, create_sidecar_dict)

def get_parser():
    
    parser = ArgumentParser(description='cmrr2logs',
                            formatter_class=ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('input_dcm', action='store', type=Path,
                        help='the input dicom file')
    
    parser.add_argument('--output_dir', action='store', type=Path,
                        help='the output path for the outcome log files')
    
    parser.add_argument('-f', '--filename',
                        type = str,
                        default = '{b}_{p}_{t}_{s}', 
                        help = 'filename in new style ({b}=basename, {d}=description,'
                        '{e}=echo number, {f}=folder name, {i}=ID of patient, {j}=seriesInstanceUID,'
                        '{k}=studyInstanceUID, {m}=manufacturer, {n}=name of patient, {p}=protocol,'
                        '{r=instance number, {s}=series number, {t}=time, {u}=acquisition number,'
                        '{v=vendor, {x}=study ID; {z}=sequence name;'
                        'default {b}_{p}_{t}_{s})' )    
    
    parser.add_argument('-b', 
                        dest = 'sidecar',
                        type=str,
                        choices = ['y', 'n'],
                        default = 'y',
                        help = 'whetheteror not to generate a json sidecar' 
                        'with the same basename as the log files')
    
    return parser
    
def main():
    """
    
    main function
    
    """
    opts = get_parser().parse_args()
    
    dcm_path = opts.input_dcm
    if opts.output_dir:
        output_path = opts.output_dir
    else:
        output_path = dcm_path.parent.absolute().as_posix()
    
    output_basename = opts.filename.format(**create_format(dcm_path))
    
    if opts.sidecar == 'y':
        sidecar_dict = create_sidecar_dict(dcm_path)
        json_file = output_path + "/" + output_basename + ".json"
        with open(json_file, 'w') as f:
            json.dump(sidecar_dict, f, indent=4)
                
    extract_cmrr_physio(dcm_path.absolute().as_posix(), output_path, output_basename)
    
if __name__ == '__main__':
    main()
    
    
