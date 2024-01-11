import torch
import itertools
from . import basis
from . import generators


class Polynomial(torch.nn.Module):
    def __init__(self, n=10, degree=2, generator=generators.dense):
        """

        Parameters:
            n (int) : number of variables
            degree (int) : degree of polynomial

        """
        super(Polynomial, self).__init__()

        self.tensors = generator(n, degree)

        tensors = [torch.nn.Parameter(torch.rand([1]))]

        for i in range(1, degree + 1):
            tensors.append(torch.nn.Parameter(torch.rand(*([n] * i))))

        self.tensors = tensors
        self.n = n
        self.degree = degree

    def forward(self, x):
        return poly(x, self.tensors)

    def to(self, **kwargs):
        for tensor in self.tensors:
            tensor.to(kwargs)

    def __getitem__(self, idx):
        return self.tensors[idx]

    def __setitem__(self, idx, value):
        self.tensors[idx] = value

    def __len__(self):
        return self.n

    def sparsity(self):
        return sum([torch.nonzero(t) for t in self.tensors])


def poly(x, T):
    s = polyD(x, T[0])
    if len(T) > 1:
        for t in T[1:]:
            s = s + polyD(x, t)
    return s


def polyD(x, T):
    """
    Computes the polynomial given by tensor T acting on input vector x

    We use the Einstein summation convention to compute the polynomial.
    For example, if we given the 3-dimensional polynomial


    Parameters:
        x (torch.Tensor) : Tensor of shape (batch_size, num_dim) representing the configuration of the system.
        T (torch.Tensor) : Tensor representing the high-dimensional triangular polynomial matrix.

    Returns:
        torch.Tensor : The energy for each configuration in the batch.
    """
    k = len(T.shape)

    params = [T, list(range(k))]

    # Exploit einsum's broadcasting to compute the polynomial
    for i in range(k):
        params.append(x)
        params.append([..., i])

    return torch.einsum(*params)


def genCoeffTensorDense(n, deg, sample_fn):
    """
    Generates the coefficients for the polynomial of degree deg

    Parameters:
        deg (int) : Degree of the polynomial

    Returns:
        torch.Tensor : Tensor representing the high-dimensional triangular polynomial matrix.
    """
    # Compute dense tensor of coefficients
    coeffs = torch.zeros(*([n] * deg))
    for i in itertools.combinations(range(n), deg):
        coeffs[i] = sample_fn()
    return coeffs


def genCoeffTensorSparse(n, deg, sample_fn):
    """
        Generates the coefficients for the polynomial of degree deg in a flat sparse format
        ----------------
        |0   c12   c13 |
        |0     0   c23 |  -->  [c12, c13, c23, c34, c35, c45]
        | ...          |


    Parameters:
        deg (int) : Degree of the polynomial

    Returns:
        torch.Tensor : Tensor representing the high-dimensional triangular polynomial matrix.
    """

    return genCoeffTensorDense(n, deg, sample_fn).flatten().to_sparse()


def monoExpand(x, deg):
    """Compute all unique monomials of degree deg"""
    raise NotImplementedError("monoExpand not implemented yet")

    params = []

    # Exploit einsum's broadcasting to compute the polynomial
    for i in range(k):
        params.append(x)
        params.append([..., i])

    return torch.einsum(*params)


def polySparse(x, T):
    """Computes the batched polynomial on a list of sparse terms"""
    sum = T[0]
    for terms in T[1:]:
        for term in terms:
            sum = sum + torch.prod(x[:, term[0]], dim=1) * term[1]
    return sum
