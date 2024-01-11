import mcmc
import torch

n = 10
deg = 3
coeffs = mcmc.polynomial.genCoeffTensorSparse(n, deg, lambda: torch.randint(0, 10, (1,)).float())
print(coeffs[torch.tensor([0, 1, 2])])

#x = torch.randint(0, 10, (1, n)).float()
#print(x)
#print(mcmc.polynomial.poly(x, coeffs))
