import mcmc
import torch
import json

def polynomial_to_json(poly):
    cost_function = {
        "type": "pubo",
        "version": "1.0",
        "q": poly.n,
        "terms": []
    }

    for degree in range(1, poly.degree + 1):
        tensor = poly[degree]
        nonzero_indices = torch.nonzero(tensor)
        for index in nonzero_indices:
            coefficient = tensor[tuple(index)].item()
            indices = index.tolist()
            cost_function["terms"].append({"c": coefficient, "ids": indices})

    return {"cost_function": cost_function}

# Example usage
poly = mcmc.Polynomial(n=10, degree=2)  # Example Polynomial instance

qubo = torch.load("./test/t0_API/QUBO_matrix.pt")
# Make upper triangular
poly.tensors = [torch.tensor([0]), torch.diag(qubo), torch.triu(qubo, diagonal=1) + torch.tril(qubo, diagonal=-1).T]

jsonp = polynomial_to_json(poly)

print(json.dumps(jsonp, indent=4))

with open("./test/t0_API/model.json", "w") as f:
    json.dump(jsonp, f, indent=4)



