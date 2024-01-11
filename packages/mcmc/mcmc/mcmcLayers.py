import torch
from .mcmc import MCMCLayer
from . import samplers, acceptanceRules, polynomial, energyFns

class BoltzmannPolyMCMC(MCMCLayer):
    def __init__(self, sampler, poly, temperature = 1.0, steps = 10):
        # Lambda is needed to make sure that the temperature is passed in. Lambda evaluates the expression at runtime.
        energy_fn = lambda x : poly(x)
        probFn = lambda s, s_p : energyFns.clampedBoltzmannFactor(s, s_p, energy_fn = energy_fn, temperature = temperature)
        acceptanceRule = lambda s, s_p: acceptanceRules.batchedProbAccept(s, s_p, probFn=probFn)
        super().__init__(
            proposeNewSample = sampler,
            applyAcceptRule = acceptanceRule,
            steps = steps
        )
        self.poly = poly
        self.temperature = temperature

class Identity(MCMCLayer):
    def __init__(self):
        super().__init__(
            proposeNewSample = lambda x : x,
            applyAcceptRule = lambda x, x_hat : x,
        )

