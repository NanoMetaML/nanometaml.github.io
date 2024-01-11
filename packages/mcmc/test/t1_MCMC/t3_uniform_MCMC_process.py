import torch

def bitstring_to_uint(bitstring_tensor):
    # Convert the bitstring tensor to a Python list
    bitstring_list = bitstring_tensor.tolist()

    # Convert the list of bits to a string of '0's and '1's
    bitstring_str = ''.join(str(int(bit)) for bit in bitstring_list)

    # Convert the binary string to an unsigned integer
    uint_value = int(bitstring_str, 2)

    return uint_value

def main():
    data = torch.load('test/data/t2_uniform_MCMC.pt')
    p_data = {}
    for data_run in data:
        p_data[data_run] = {}
        for temperature in data[data_run]:

            if temperature == 'H' or temperature == 'spectral_gap':
                continue
            print('data_run: {}, temperature: {}'.format(data_run, temperature))
            s = data[data_run][temperature]['s']
            s = torch.stack(s)
            n = s.shape[1]
            p = torch.zeros(2**n, 2**n)
            for i in range(len(s) - 1):
                s_i = bitstring_to_uint(s[i])
                s_i_plus_1 = bitstring_to_uint(s[i + 1])
                p[s_i, s_i_plus_1] += 1
            for i in range(p.shape[0]):
                if p[i].sum() == 0:
                    continue
                p[i] = p[i] / p[i].sum()
            p_data[data_run][temperature] = p

    torch.save(p_data, 'test/data/t3_uniform_MCMC_process.pt')

if __name__ == '__main__':
    main()
