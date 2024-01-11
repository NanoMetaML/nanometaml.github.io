import torch
from .changeBasis import toStandard, toBasisFromStandard

def bitstring_to_uint(bitstring_tensor, basis):
    # Convert the bitstring tensor to a Python list
    
    bitstring_tensor = toStandard(bitstring_tensor, basis)


    bitstring_list = bitstring_tensor.tolist()

    # Convert the list of bits to a string of '0's and '1's
    bitstring_str = ''.join(str(int(bit)) for bit in bitstring_list)

    # Convert the binary string to an unsigned integer
    uint_value = int(bitstring_str, 2)

    return uint_value

def uint_to_bitstring(uint_value, basis, size):
    # Convert the unsigned integer to a binary string
    bitstring_str = bin(uint_value)[2:]

    # Pad the string with '0's to the correct length
    bitstring_str = bitstring_str.zfill(size)

    # Convert the string to a list of bits
    bitstring_list = [int(bit) for bit in bitstring_str]

    # Convert the list to a tensor
    bitstring_tensor = torch.tensor(bitstring_list, dtype=torch.float)

    bitstring_tensor = toBasisFromStandard(bitstring_tensor, basis)

    return bitstring_tensor
