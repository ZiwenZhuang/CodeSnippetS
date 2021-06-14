import torch

def count_parameters(model):
    """ Count the number of trainable parameters in the given torch model
    """
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
