from .hyperparams import getHyperParamVector
import logging

def sample(sampler, prior, num_samples):
    samples = []
    for i in range(num_samples):
        samples.append(sampler(prior(i)))
    return samples


def sampleHyperSweep(steps, 
                     trials, 
                     initSPrior, 
                     channelPrior, 
                     hyperParamsIter,
                     ):
    """ 
    steps: number of steps to run MCMC
    trials: number of trials to run
    initSPrior: function that returns a sample from the prior
    channelPrior: function that returns an MCMC channel
    hyperParamsIter: iterator that returns hyperparams to run MCMC 
    """

    data = {}

    for run_idx in range(trials):
        logging.debug(f"Trial {run_idx}")

        channel = channelPrior()

        data[run_idx] = {
            'channel': channel.__class__.__name__,
            'hyperSweep' : {}
        }

        for idx, hyperParam in enumerate(hyperParamsIter):
            logging.debug(f"Channel {run_idx} HyperParams: {hyperParam}" )

            s = initSPrior()

            data[run_idx]['hyperSweep'][idx] = {
                'hyperParam': hyperParam,
            }
            x, xprop = channel.validate(s, steps=steps, **hyperParam)

            data[run_idx]['hyperSweep'][idx]['s'] = x
    return data
