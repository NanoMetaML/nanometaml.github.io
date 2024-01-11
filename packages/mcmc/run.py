"""
File: run.py
Author: Blake Wilson
Date: 2023-04-06
"""

# This file runs the experiment by specifying the experiment
# name and running it from the config file.
import argparse
import importlib
import sys
from pathlib import Path

import omegaconf


def main():
    """Main"""
    parser = argparse.ArgumentParser(description="Run an experiment")
    parser.add_argument("--exp_path", type=str, help="The name of the experiment to run")
    parser.add_argument("--exp_name", type=str, help="The name of the experiment to run")

    args = parser.parse_args()

    if (Path(args.exp_path) / args.exp_name / "config.yaml").exists():
        # Load the experiment from the top folder
        spec = importlib.util.spec_from_file_location(
            "main", Path(args.exp_path) / "main.py"
        )
        exp_module = importlib.util.module_from_spec(spec)

        # Add module
        sys.modules["main"] = exp_module

        spec.loader.exec_module(exp_module)

        exp_module.main(
            omegaconf.OmegaConf.load(
                Path(args.exp_path) / args.exp_name / "config.yaml"
            )
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
