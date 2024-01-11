
import hydra
from omegaconf import DictConfig
import nanomodules
import logging

from clearml import Task
import torch

torch.set_float32_matmul_precision("medium")


def run_experiment(cfg: DictConfig, log_task=True) -> None:
    "Running experiment"
    if log_task:
        task = Task.init(project_name=cfg.project_name,
                         task_name=cfg.task_name)

    logging.debug(cfg)
    cfg = nanomodules.configToDict(cfg)
    loaded_dict = nanomodules.configWalkBuild(cfg)
    logging.debug("loaded_dict: ")
    logging.debug(loaded_dict)

    logging.basicConfig(filename='app.log',
                        filemode='w', level=logging.DEBUG)
    print(loaded_dict['model'])
    print(loaded_dict['model'].model.parameters())
#    logging.debug("Model: ", loaded_dict['model'])
    loaded_dict['trainer'].fit(
        loaded_dict['model'], loaded_dict['datasets']['train'], loaded_dict['datasets']['valid'])
