import logging
import eta.core.web as etaw
from fiftyone.operators import types

import torch
import fiftyone.utils.torch as fout

logger = logging.getLogger(__name__)

MODEL_URL = "https://drive.usercontent.google.com/download?id=1xRDxfN5nIMjxtAUQWzqDiPIk2Y9bFKgX&export=download&authuser=0&confirm=t&uuid=6f9b3aa6-42d8-4fc0-841d-280d7dcf4d9d&at=AEz70l4_GFVTcb1dFQcxlJGhJ2MH:1742683378839"

def download_model(model_name, model_path):
    logger.info("Downloading model...")

    etaw.download_file(MODEL_URL, path=model_path)

    

def load_model(model_name, model_path, classes, **kwargs):
    """Loads the model.

    Args:
        model_name: the name of the model to load, as declared by the
            ``base_name`` and optional ``version`` fields of the manifest
        model_path: the absolute filename or directory to which the model was
            donwloaded, as declared by the ``base_filename`` field of the
            manifest
        **kwargs: optional keyword arguments that configure how the model
            is loaded

    Returns:
        a :class:`fiftyone.core.models.Model`
    """

    print(model_name)

    # Consturct the specified `Model` instance, generally by importing
    # other modules in `model_dir`
    model = torch.load(model_path,weights_only=False)

    d = dict(model_path=model_path, classes=classes)

    config = fout.TorchImageModelConfig(d)

    return fout.TorchImageModel(config)
