"""
File: test.py
Author: Alex Nano
Email: wilso692@purdue.edu

Description:
    Test file for nanoml-template.
"""

from pathlib import Path
import numpy as np
from nanometaml import main, download_dataset, upload_dataset

if __name__ == "__main__":

    project_name = 'nanometaml_test'
    
    print("Please enter your name: ")
    my_name = input()
    
    test_file = 'test.npy'
    # Create a test numpy dataset
    path = (Path(__file__).parent / test_file).as_posix()
    my_npy = np.random.normal(0, 1, 5)
    np.save(Path(path), my_npy)

    print("Testing nanoml-template.\n")

    main.main()
    upload_dataset.upload_dataset(path, project_name, my_name)
    download_dataset.download(project_name, my_name, [test_file])

    print("Done!")