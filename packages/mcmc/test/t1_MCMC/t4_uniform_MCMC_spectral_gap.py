import torch
import numpy

def main():
    data = torch.load('test/data/t3_uniform_MCMC_process.pt')

    # Compute the spectral gap
    spectral_gap = {}
    for data_run in data:
        spectral_gap[data_run] = {}
        for temperature in data[data_run]:
            print('data_run: {}, temperature: {}'.format(data_run, temperature))
            p = data[data_run][temperature]
            p = p.numpy()
            w, v = numpy.linalg.eig(p)
            w = numpy.sort(w)
            spectral_gap[data_run][temperature] = 1 - max(w[w != 1])

    # Save the spectral gap
    torch.save(spectral_gap, 'test/data/t4_uniform_MCMC_spectral_gap.pt')

if __name__ == '__main__':
    main()
