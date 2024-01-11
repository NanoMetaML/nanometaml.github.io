import mcmc 
import torch 
if __name__ == '__main__':

    n = 6

    hyperParams = {
        'temperature' : [0.001, 0.01]
    }

    
    s_init = mcmc.binaryPriors.uniform(n, 'cpu', basis=mcmc.Basis.spin).unsqueeze(0)
    poly = mcmc.Polynomial(n=n, degree=2, basis=mcmc.Basis.spin, device='cpu')
    print(mcmc.polynomial.polyD(s_init, poly[0]))
    print(mcmc.polynomial.polyD(s_init, poly[1]))
    print(mcmc.polynomial.polyD(s_init, poly[2]))
    print(mcmc.polynomial.poly(s_init, poly))

    


