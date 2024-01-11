import torch

def dense(n, degree):
    tensors = [torch.nn.Parameter(torch.rand([1]))]

    for i in range(1, degree+1):
        tensors.append(torch.nn.Parameter(torch.rand(*([n]*i))))

    return tensors

def triangular(n, degree, remove_diagonal=True):
    tensors = dense(n, degree)
    for i in range(2, len(tensors)):
        #.... Remove diagonal from 3+???
        pass
    return tensors


