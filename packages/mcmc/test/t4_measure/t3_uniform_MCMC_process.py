import torch
import mcmc

def bitstring_to_uint(bitstring_tensor):
    # Convert the bitstring tensor to a Python list
    bitstring_list = bitstring_tensor.tolist()
    if -1 in bitstring_list:
        bitstring_list = [0 if bit == -1 else bit for bit in bitstring_list]

    # Convert the list of bits to a string of '0's and '1's
    bitstring_str = ''.join(str(int(bit)) for bit in bitstring_list)

    # Convert the binary string to an unsigned integer
    uint_value = int(bitstring_str, 2)

    return uint_value

def computeTransitionMatrix(s):

    s = torch.stack(s)
    s = s.squeeze()
    
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
    return p

def postProcessSample(postFn, data, hyperParamsIter, hyperParamKey = "hyperParam"):
    p_data = {}
    for data_run in data:
        p_data[data_run] = {
            'channel': data[data_run]['channel'],
            'hyperSweep' : {}
        }

        hyperParamsList = [hyperParam for _, hyperParam in enumerate(hyperParamsIter)]

        for h in data[data_run]['hyperSweep']:
            if data[data_run]['hyperSweep'][h][hyperParamKey] not in hyperParamsList:
                continue
                
            p_data[data_run]['hyperSweep'][h] = postFn(data[data_run]['hyperSweep'][h])
    return p_data



if __name__ == '__main__':

    data = torch.load('test/t4_measure/small-t2_uniform_MCMC.pt')
    hyperParams = {
        'temperature' : [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    }

    hyperParamsIter = mcmc.hyperparams.getHyperParamVector(hyperParams)
    tMatrix = mcmc.postProcess.postProcessHyper(
        lambda h : ['p', computeTransitionMatrix(h['s'])],
        'p',
        data,
        hyperParamsIter)

    torch.save(tMatrix, 'test/t4_measure/t3_uniform_MCMC_process.pt')
