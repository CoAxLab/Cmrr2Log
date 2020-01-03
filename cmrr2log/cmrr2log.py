#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

#TODO: Add option to generate a json file sidecar

"""
from pathlib import Path
from argparse import ArgumentParser
from argparse import ArgumentDefaultsHelpFormatter
from .extract_cmrr import extract_cmrr_physio
from .utils import create_format

def get_parser():
    
    parser = ArgumentParser(description='cmrr2logs',
                            formatter_class=ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('input_dcm', action='store', type=Path,
                        help='the input dicom file')
    
    parser.add_argument('--output_dir', action='store', type=Path,
                        help='the output path for the outcome log files')
    
    parser.add_argument('-f', '--filename',
                        type = str,
                        default = '{f}_{p}_{t}_{s}', 
                        help = 'filename in new style ({b}=basename, {d}=description,'
                        '{e}=echo number, {f}=folder name, {i}=ID of patient, {j}=seriesInstanceUID,'
                        '{k}=studyInstanceUID, {m}=manufacturer, {n}=name of patient, {p}=protocol,'
                        '{r=instance number, {s}=series number, {t}=time, {u}=acquisition number,'
                        '{v=vendor, {x}=study ID; {z}=sequence name;'
                        'default {f}_{p}_{t}_{s})' )
    
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
    
    extract_cmrr_physio(dcm_path.absolute().as_posix(), output_path, output_basename)
    
if __name__ == '__main__':
    main()
    
    
