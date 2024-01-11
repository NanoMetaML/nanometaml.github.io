<p align=center>
<picture><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Purdue_Boilermakers_logo.svg/1200px-Purdue_Boilermakers_logo.svg.png" alt="Purdue Logo" width=200></picture>
</p>
<p style="font-size:40px;" align=center>
NanoML MCMC Package
</p>

![Purdue](https://img.shields.io/badge/Purdue-University-cfb991?style=for-the-badge) 
![Version](https://img.shields.io/static/v1?label=Version&message=0.0.1&color=cfb991&style=for-the-badge)
![License](https://img.shields.io/static/v1?label=License&message=MIT&color=cfb991&style=for-the-badge)
![Python](https://img.shields.io/badge/-Python-cfb991?logo=python&logoColor=white&style=for-the-badge)


<p style="font-size:30px;" align=center>
MCMC
</p>

## Usage

    import mcmc
    

## Installation

    git clone https://github.com/nanometaml/mcmc.git
    cd ./mcmc
    python -m pip install -e .

## Usage

### Polynomial

We store polynomials using the sparse tensor of the coefficients. For example, let the polynomial

  p(x) = c + \sum_i x_i h_i + \sum_{i \leq j} x_i x_j w_{ij} + ...

Then, c is a 0-tensor, i.e., it has shape (1), h is a 1-tensor with shape (n), w is a 2-tensor with shape (n , n) and so on. Without sparsity, these tensors would take up O(n^d) where d is the maximum degree. However, with sparse representations the storage space scales with the number of non-zero coefficients. 

To initialize a polynomial, simply call mcmc.Polynomial()

    import mcmc
    poly = mcmc.Polynomial()

By default, the constructor creates a quadratic, or two-degree, random polynomial.




# License

All NanoML projects are released under the MIT License. This permissive license allows you to use, modify, and distribute our code, as long as you include the original copyright and license information.
