import numpy

def postProcessHyper(postFn, postKey, data, hyperParamsIter, hyperParamKey = "hyperParam"):
    p_data = data

    for data_run in data:

        hyperParamsList = [hyperParam for _, hyperParam in enumerate(hyperParamsIter)]

        for h in data[data_run]['hyperSweep']:
            if data[data_run]['hyperSweep'][h][hyperParamKey] not in hyperParamsList:
                continue
                


            key, r = postFn(data[data_run]['hyperSweep'][h])
            p_data[data_run]['hyperSweep'][h][key] = r     
    return p_data

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

def computeSpectralGapFromPMatrix(pMatrix):

    pMatrix = pMatrix.numpy()
    w, v = numpy.linalg.eig(pMatrix)
    w = numpy.sort(w)
    return 1 - max(w[w != 1])

