import mcmc
import itertools
import functools
import torch

def getHyperParam(hyperParams):
    # Get the keys and lists from the dictionary
    keys = list(hyperParams.keys())
    lists = list(hyperParams.values())

    # Generate the Cartesian product of all lists
    combinations = list(itertools.product(*lists))

    # Create a list of key-value pairs for each combination
    result = [{keys[i]: item[i] for i in range(len(keys))} for item in combinations]
    return result

def pick_items_from_lists(list_of_lists):
    # Generate the Cartesian product of all lists
    combinations = list(itertools.product(*list_of_lists))
    return combinations

def acceptancesampler(s, s_p, energy_fn):

    b = torch.exp(energy_fn(s_p) - energy_fn(s))
    acceptance_prob = min(1, b)
    if torch.rand(1) < acceptance_prob:
        s = s_p
    return s

def quboPrior(n):
    H = torch.rand(n, n)
    energy_fn = functools.partial(mcmc.energy_fn.quboEnergy, H = H)
    return H, energy_fn

# Simple MCMC sampler
def main(n, init_s_prior, quboPrior, getProposal, sampleAccept, temps):

    data = {}

    for run_idx in range(10):

        H, energy_fn = quboPrior(n)

        data[run_idx] = {
            'spectral_gap': mcmc.energy_fn.spectralGap(energy_fn, n),
            'probleminstance': [H, energy_fn],
        }

        for temperature in temps:
            print(f"QUBO: {run_idx} Temperature: {temperature}" )

            s = init_s_prior()

            data[run_idx][temperature] = {
                's': [s]
            }

            energy_fn =  functools.partial(mcmc.energy_fn.quboEnergy, H = H / temperature)
            for sample_idx in range(100):
                s_p = getProposal(s=s)
                s = sampleAccept(s, s_p, energy_fn)
                data[run_idx][temperature]['s'].append(s)
    # Save
    torch.save(data, 'test/data/t2_uniform_MCMC.pt')

if __name__ == '__main__':
    n = 6
    hyperParams = {
        temperature : [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    }
    channel = mcmc.channels.BoltzmannPolyMCMC
    uniformPrior = functools.partial(mcmc.binarypriors.uniform, n=n, device = 'cpu')
    main(n, uniformPrior, quboPrior, getProposal=uniformPrior, sampleAccept=acceptancesampler, temps=temps)

