import torch
import random
import functools
import enum
import math

from . import flipFns, utils, changeBasis
from .basis import Basis



# ---------------------------- SAMPLER FUNCTION BUILDER ---------------------------- #
# The following function is a builder function that takes in a flip function and returns a sampler function
def sampleFnFromFlipFn(
                    x,                              # input tensor
                    flip_fn,                        # flip function
                    basis: Basis = Basis.standard,  # basis of the input tensor
                    **kwargs                        # keyword arguments for flip_fn
                    ):
    """
        Builds a sampler function that applies the output of a flip function to a tensor x
    """

    x_flip = flip_fn(x, **kwargs)

    if basis == Basis.spin:
        x_noisy = x * (1 - x_flip) + (-1) * x * x_flip

    elif basis == Basis.standard:
        x_noisy = (
            x * (1 - x_flip) + (1 - x) * x_flip
        )
    else:
        raise NotImplementedError("Basis {} not implemented".format(basis))

    return x_noisy


def buildFlipFnFromSampleFn(
                    x,                              # input tensor
                    sampler_fn,                     # sample function
                    **kwargs                        # keyword arguments for flip_fn
                    ):
    """
        Builds a flip function that applies the output of a sampler function to a tensor x
    """

    x_new = sampler_fn(x, **kwargs)

    return torch.abs(torch.sign(x_new - x)) 


def buildNoisySampleFn(
                    sampler_fn,                     # sample function
                    basis: Basis = Basis.standard,  # basis of the input tensor
                    **kwargs                        # keyword arguments for flip_fn and sampler_fn
                    ):
    """
        Builds a sampler function that adds noise onto x such that x_{t} = f(x_{t-1})
    """
    flip_fn = functools.partial(
        buildFlipFnFromSampleFn,
        sampler_fn=sampler_fn,  # sample function
        **kwargs)               # keyword arguments for flip_fn

    return functools.partial(sampleFnFromFlipFn,
                             basis=basis,
                             flip_fn=flip_fn)


# ---------------------------- SAMPLE FUNCTIONS ---------------------------- #


sampleBiasedFlipCategorical = lambda x : sampleFnFromFlipFn(x, flip_fn=flipFns.categoricalFlip)
sampleFlipChooseK = lambda x,k : sampleFnFromFlipFn(x, k, flip_fn=flipFns.uniformPermFlip)

sampleBiasedFlipCategorical.__doc__ = """
        Sampler function that applies a biased categorical flip to a tensor x. 
        Randomly chooses a single bit along the last dimension and flips it
        with probability p_0 if the bit is 0 and p_1 if the bit is 1.
        Parameters:
            x: input tensor
            bias: bias of the bernoulli distribution
    """


sampleFlipChooseK.__doc__ = """
        Sampler function that applies a uniform choose k flip to a tensor x.
        Randomly chooses k bits along the last dimension and flips them.
    """

class ChooseKFlip:
    """
        Sampler function that applies a uniform choose k flip to a tensor x.
        Randomly chooses k bits along the last dimension and flips them.
    """

    def __init__(self, k):
        self.k = k

    def __call__(self, x):
        return sampleFnFromFlipFn(x, k = self.k, flip_fn=flipFns.uniformPermFlip)

class Identity:
    """
        Sampler function that applies a uniform choose k flip to a tensor x.
        Randomly chooses k bits along the last dimension and flips them.
    """

    def __init__(self):
        pass

    def __call__(self, x):
        return x

class ChooseOneFlip:
    """
        Sampler function that applies a biased categorical flip to a tensor x. 
        Randomly chooses a single bit along the last dimension and flips it
        with probability p_0 if the bit is 0 and p_1 if the bit is 1.
        Parameters:
            x: input tensor
            bias: bias of the bernoulli distribution
    """

    def __init__(self, bias):
        self.bias = bias

    def __call__(self, x):
        return sampleFnFromFlipFn(x, self.bias, flip_fn=flipFns.categoricalFlip)

class TransitionMatrix:

    def __init__(self, 
                 tMatrix,
                 basis = Basis.spin
                 ):
        self.basis = basis

        if isinstance(tMatrix, str):
            tMatrix = torch.tensor(np.load(tMatrix))
        else:
            self.tMatrix = tMatrix
        
        if self.tMatrix.shape[0] != self.tMatrix.shape[1]:
            raise ValueError("Transition matrix must be square")

    def __call__(self, x):
        re_batched = torch.zeros_like(x)
        for batch in range(x.shape[0]):
            s = changeBasis.toStandard(x[batch], self.basis)
            s = utils.bitstring_to_uint(x[batch], self.basis)
            s_sample = self.tMatrix[s]
            s_next = utils.uint_to_bitstring(torch.multinomial(s_sample, 1), self.basis, int(math.log2(self.tMatrix.shape[0])))
            re_batched[batch] = s_next
        return re_batched.detach()


def sampleBiasedUniform(x, bias=0.5, basis = Basis.standard, **kwargs):
    """
        Samples a biased bernoulli distribution over the 
        tensor shape.
    """
    if basis == Basis.spin:
        
        return torch.bernoulli(torch.ones_like(x) * bias) * 2 - 1

    return torch.bernoulli(torch.ones_like(x) * bias)


