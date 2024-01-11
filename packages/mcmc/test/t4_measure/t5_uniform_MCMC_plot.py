import torch
import numpy

def main():
    data = torch.load('test/data/t4_uniform_MCMC_spectral_gap.pt')
    sp = {}

    # Compute the spectral gap
    for temperature in data[0]:
        sp[temperature] = []

    for data_run in data:
        for temperature in data[data_run]:
            sp[temperature].append(data[data_run][temperature])

    for temperature in sp:
        sp[temperature] = numpy.mean(sp[temperature])

    # Plot the spectral gap
    import matplotlib.pyplot as plt
    # log-log plot

    plt.figure()
    plt.loglog(list(sp.keys()), list(sp.values()))
    plt.xlabel('Temperature')
    plt.ylabel('Spectral gap')
    plt.savefig('./test/data/t5_uniform_MCMC_plot.png')

if __name__ == '__main__':
    main()
