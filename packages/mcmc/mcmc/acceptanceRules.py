import torch 


def batchedProbAccept(s, s_p, probFn, detach:bool = True, **kwargs):
    """
    Batched probabilistic acceptance rule.
    Parameters
        s [b, ...] : current state
        s_p [b, ...] : proposed state
        prob [b, ...] x [b, ...] -> [b, 1]: function that returns the batched probability of accepting state s_p given state s

    """
    p_change = probFn(s, s_p, **kwargs)

    accept = torch.bernoulli(p_change)
    accept = accept.unsqueeze(1)

    s = s * (1 - accept.detach()) + s_p * accept.detach()

    return s

def probAccept(s, s_p, prob):
    """
    Applies generic acceptance rule.
    Parameters
        s: current state
        s_p: proposed state
        prob: function that returns the probability of a state

    """

    acceptance_prob = min(1, prob(s_p))
    if torch.rand(1) < acceptance_prob:
        s = s_p

    return s
