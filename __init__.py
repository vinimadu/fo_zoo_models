import torch

def download_model(model_name, model_path):
        pass

def load_model(model_name, model_path, **kwargs):
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

    return model