"""
File: template_download_dataset.py
Author: Alexander Nano
Email: wilso692@purdue.edu

Description:
    Template file for downloading datasets.
"""

from clearml import Dataset
import numpy as np
from pathlib import Path

def download(dataset_project, dataset_name, files):
    """Main function for template_download_dataset.py"""
    dataset = Dataset.get(dataset_project=dataset_project, dataset_name=dataset_name).get_local_copy()
    for file in files:
        
        np.load(Path(dataset) / file)
        print('Downloaded dataset: {}'.format(Path(dataset) / file))

    