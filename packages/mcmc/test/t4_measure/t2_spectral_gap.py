import mcmc
import itertools
import functools
import torch
import logging

import mcmc

logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':

    n = 6

    hyperParams = {
        'temperature' : [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    }

    proposer = lambda x : mcmc.binaryPriors.uniform(n, 'cpu', basis=mcmc.Basis.spin).unsqueeze(0)

    channelPrior =  lambda : mcmc.channel.BoltzmannPolyMCMC(
                    sampler = proposer,
                    poly = mcmc.Polynomial(n=n, degree=2, basis=mcmc.Basis.spin, device='cpu'))

    results = mcmc.measure.sampleHyperSweep(
                steps=10,
                trials=10,
                initSPrior=lambda : mcmc.binaryPriors.uniform(n, 'cpu', basis=mcmc.Basis.spin).unsqueeze(0),
                channelPrior=channelPrior,
                hyperParamsIter=mcmc.hyperparams.getHyperParamVector(hyperParams),
)
    torch.save(results, 'test/t4_measure/small-t2_uniform_MCMC.pt')

