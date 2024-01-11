import torch
from .polynomial import Polynomial 
from .basis import Basis

def toStandard(x, basis):
    if basis == Basis.standard:
        return x
    elif basis == Basis.spin:
        return (x + 1) / 2
    else:
        raise NotImplementedError("Basis {} not implemented".format(basis))


def toBasisFromStandard(x, basis):
    if basis == Basis.standard:
        return x
    elif basis == Basis.spin:
        return 2 * x - 1
    else:
        raise NotImplementedError("Basis {} not implemented".format(basis))

def spinVToStandard(spin):
    return 2 * spin - 1

def standardVToSpin(standard):
    return (standard + 1) / 2

def standardQuadtoSpinQuad(standardP):
    """ Convert a QUBO Polynomial in the standard basis to the spin basis.


        Derivation:
            
            Let N = 1/2 * (I - Z)
            Let H = sum_{i,j: i < j} J_{ij} N_i N_j + sum_i h_i N_i
            H     = sum_{i,j: i < j} J_{ij} (1/2 * (I - Z)_i) (1/2 * (I - Z)_j) + sum_i h_i (1/2 * (I - Z)_i)
            H     = sum_{i,j: i < j} J_{ij} (1/4 * (I_i - Z_i) * (I_j - Z_j)) + sum_i h_i (1/2 * (I_i - Z_i))
            H     = sum_{i,j: i < j} J_{ij} (1/4 * (I_i * I_j - I_i * Z_j - Z_i * I_j + Z_i * Z_j)) + sum_i h_i (1/2 * (I_i - Z_i))
            H     = sum_{i,j} J_{ij} (1/4 * (I_i * I_j  + Z_i * Z_j)) + sum_i h_i (1/2 * I_i - 1/2 * Z_i )

            H_1 = sum_{i,j: i < j} J_{ij} / 4 * I_i * I_j = for all z : sum_{i,j: i < j} J_{ij} / 4
            H_2 = sum_{i,j: i < j} J_{ij} / 4 * Z_i * Z_j
            H_3 = sum_{i,j: i < j} J_{ij} (- I_i * Z_j / 4 - Z_i * I_j / 4)
            H_4 = sum_i h_i / 2 I_i = for all z : sum_{i} h_i / 2
            H_5 = - sum_i h_i / 2 Z_i 


            H_3 = sum_{i,j: i < j} J_{ij} (- I_i * Z_j / 4 - Z_i * I_j / 4)
            H_3 = sum_{i,j: i < j} J_{ij} (- I_i * Z_j / 4)
            H_3 = sum_{i,j: i > j} J_{ij} (- Z_j * I_i / 4)

            H_3 = sum_{i,j: i != j} J_{ij}/4 (- Z_j / 4)
            J_j = sum_{i: i != j} J_{ij}/4
            H_3 = sum_{j} J_j (- Z_j / 4)



            Constant:
            H_1 + H_4 =   sum_{i,j : i < j} J_{ij} / 4 + sum_i h_i / 2

            Linear:
            H_3 + H_5 = - sum_i (J_i/4 + h_i / 2) * Z_i 

            Quadratic:
            H_2 =     sum_{i,j} J_{ij} / 4 * Z_i * Z_j

    """
    Q = standardP.tensors[2]
    h = standardP.tensors[1]
    c = standardP.tensors[0]


    H_1 = torch.sum(Q) / 4
    H_4 = torch.sum(h) / 2

    H_3 = torch.sum(Q, dim=0) / 4 + torch.sum(Q, dim=1) / 4
    H_5 = h / 2

    H_2 = Q / 4

    return Polynomial(
        tensors=[
        c + H_1 + H_4,
        H_3 + H_5,
        H_2
        ],
        basis=Basis.spin,
        dtype = Q.dtype)

def spinQuadtoStandardQuad(standardP):
    """ Convert a QUBO Polynomial in the spin basis to the standard basis.


        Derivation:
            

    """
    Q = standardP.tensors[2]
    h = standardP.tensors[1]
    c = standardP.tensors[0]


    H_1 = torch.sum(Q)
    H_4 = -1 * torch.sum(h)

    H_3 = -2 * (torch.sum(Q, dim=0)  + torch.sum(Q, dim=1))
    H_5 = h * 2

    H_2 = Q * 4

    return Polynomial(
        tensors=[
        c + H_1 + H_4,
        H_3 + H_5,
        H_2
        ],
        basis=Basis.standard,
        dtype = Q.dtype)
