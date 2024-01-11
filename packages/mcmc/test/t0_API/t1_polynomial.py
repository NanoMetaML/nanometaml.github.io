import mcmc
import torch

def test_shape(a, b):

     torch.all(torch.tensor([a[i] == b[i] for i in range(len(a))]))

poly = mcmc.Polynomial()

assert len(poly) == 10
assert poly.degree == 2


poly = mcmc.Polynomial(n = 20, degree=3)

assert len(poly) == 20
assert poly.degree == 3
assert torch.tensor(poly[0].shape) == torch.tensor([1])
assert torch.tensor(poly[1].shape) == torch.tensor([len(poly)])
test_shape(torch.tensor(poly[2].shape), torch.tensor([len(poly), len(poly)]))
test_shape(torch.tensor(poly[3].shape), torch.tensor([len(poly), len(poly), len(poly)]))


