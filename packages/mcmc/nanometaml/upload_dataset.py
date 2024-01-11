"""
File: template_upload.py
Author: Alexander Nano
Email: wilso692@purdue.edu

Description:
    Template file for uploading modules to clearml.
"""

from clearml import Task
from clearml import Dataset
import numpy as np
from pathlib import Path

def upload_dataset(path, dataset_project, dataset_name):
    
    dataset = Dataset.create(
        dataset_name=dataset_name,
        dataset_project=dataset_project,
        dataset_tags=[dataset_name],
    )
    
    dataset.add_files(path)
    dataset.upload()
    dataset.finalize()
    print("Successfully Uploaded dataset: {}".format(dataset))