from .polynomial import Polynomial
import torch


def uniformPolynomial(n, d, basis, device):
    """
    Generates a random polynomial with coefficients sampled from a uniform distribution

    Parameters:
        n (int) : Number of variables in the polynomial
        d (int) : Degree of the polynomial
        basis (mcmc.polynomial.Basis) : Basis for the polynomial
        device (str) : Device to use for the tensor

    Returns:
        mcmc.polynomial.Polynomial : A polynomial with coefficients sampled from a uniform distribution
    """
    tensors = []
    for i in range(d+1):
        tensors.append(torch.rand(*([n]*d), device=device))
    return Polynomial(tensors=tensors, basis=basis)



def normalPolynomial(n, d, basis, device):
    """
    Generates a random polynomial with coefficients sampled from a gaussian distribution

    Parameters:
        n (int) : Number of variables in the polynomial
        d (int) : Degree of the polynomial
        basis (mcmc.polynomial.Basis) : Basis for the polynomial
        device (str) : Device to use for the tensor

    Returns:
        mcmc.polynomial.Polynomial : A polynomial with coefficients sampled from a uniform distribution
    """
    tensors = []
    for i in range(d+1):
        tensors.append(torch.randn(*([n]*d), device=device))
    return Polynomial(tensors=tensors, basis=basis)
