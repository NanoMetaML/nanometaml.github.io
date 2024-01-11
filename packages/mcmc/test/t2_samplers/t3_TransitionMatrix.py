import mcmc
import torch

# Test 3: TransitionMatrix

tMatrix = torch.tensor([[1.0, 0], [1.0, 0]])

tSampler = mcmc.samplers.TransitionMatrix(tMatrix)

x = torch.randint(2, (1000,1))

y = tSampler(x).float()

print("Transition matrix sampler statistics:")
print("Mean: ", torch.mean(y))
print("Variance: ", torch.var(y))

print("Diff statistics:")
print("Mean: ", torch.mean(torch.abs(x-y)))
print("Variance: ", torch.var(torch.abs(x-y)))


import pathlib

# Create and Save Transition Matrix
tMatrix = torch.tensor([[1.0, 0], [1.0, 0]])

tMatrixPath = pathlib.Path("./tMatrix.npy")

torch.save(tMatrix, tMatrixPath)

tMatrix = torch.load(tMatrixPath)

# Load Transition Matrix
tMatrix = mcmc.samplers.TransitionMatrix(tMatrix)

x = torch.randint(2, (1000,1))

y = tMatrix(x).float()

print("Transition matrix sampler statistics:")
print("Mean: ", torch.mean(y))
print("Variance: ", torch.var(y))

print("Diff statistics:")
print("Mean: ", torch.mean(torch.abs(x-y)))
print("Variance: ", torch.var(torch.abs(x-y)))

# delete the file
tMatrixPath.unlink()




