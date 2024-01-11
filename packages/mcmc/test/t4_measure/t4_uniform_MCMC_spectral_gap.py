import torch
import numpy
import mcmc

def computeSpectralGapFromPMatrix(pMatrix):

    pMatrix = pMatrix.numpy()
    w, v = numpy.linalg.eig(pMatrix)
    w = numpy.sort(w)
    return 1 - max(w[w != 1])

def main():
    data = torch.load('test/data/t3_uniform_MCMC_process.pt')

    # Compute the spectral gap
    spectral_gap = {}
    for data_run in data:
        spectral_gap[data_run] = {}
        for temperature in data[data_run]:
            print('data_run: {}, temperature: {}'.format(data_run, temperature))
            p = data[data_run][temperature]

    # Save the spectral gap
    torch.save(spectral_gap, 'test/data/t4_uniform_MCMC_spectral_gap.pt')

if __name__ == '__main__':

    data = torch.load('test/t4_measure/t3_uniform_MCMC_process.pt')
    hyperParams = {
        'temperature' : [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    }

    hyperParamsIter = mcmc.hyperparams.getHyperParamVector(hyperParams)

    spectral_gaps = mcmc.postProcess.postProcessHyper(
        lambda h : ['spectral_gap', mcmc.postProcess.computeSpectralGapFromPMatrix(h['p'])],
        'spectral_gap',
        data,
        hyperParamsIter)
    
    torch.save(spectral_gaps, 'test/t4_measure/t4_uniform_MCMC_spectral_gap.pt')
