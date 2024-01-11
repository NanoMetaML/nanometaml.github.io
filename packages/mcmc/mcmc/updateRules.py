import torch
import logging

def bernoulliChoice(x, x_hat, prob_fn, **kwargs):
    """Chooses between x and x_hat with probability p = prob_fn(x, x_hat, **kwargs)"""
    p = prob_fn(x, x_hat, **kwargs)

    accept = torch.bernoulli(p).unsqueeze(1)

    return x * (1 - accept) + x_hat * accept

def thermalBernoulli(x, x_hat, energy_fn, temperature=1, **kwargs):
    return bernoulliChoice(x, x_hat, boltzmannEnergyDiff, energy_fn=energy_fn, temperature=temperature, **kwargs)


def boltzmannEnergyDiff(x, x_hat, energy_fn, **kwargs):
    # Maps all vectors where en(x_hat) < en(x) to be guaranteed to flip.
    # Maps other vectors to flip with probability prop to
    # exp(-|energy(x_hat) - energy(x_hat)|).

    energy_x = energy_fn(x, **kwargs)
    energy_x_hat = energy_fn(x_hat, **kwargs)

    energy_diff = torch.nn.functional.relu(energy_x_noisy - energy_x)

    p_change = torch.exp(-energy_diff)

    return p_change


def _energy_channel_01(self, x):
    """Energy Channel for 0,1 Basis"""
    # Flip 0s to 1s with probability p_0
    # choose random neighbors

    cat_probs = torch.ones_like(x) * 1 / x.shape[-1]
    # logging.debug(f"Categorical probabilities {cat_probs}")
    neighbors = torch.distributions.OneHotCategoricalStraightThrough(
        cat_probs
    ).sample(x.shape[:-2])

    x_0_mask = (x == 0).float() * neighbors
    x_0_flip = x_0_mask * \
        torch.bernoulli(self.p_0 * torch.ones_like(x_0_mask))
    # logging.debug(f"x_0_flip: {x_0_flip}")
    x_1_mask = (x == 1).float() * neighbors
    x_1_flip = x_1_mask * \
        torch.bernoulli(self.p_1 * torch.ones_like(x_1_mask))

    # logging.debug(f"x_1_flip: {x_1_flip}")
    x_flip = x_0_flip + x_1_flip

    # Sanity check to make sure that the gradient is not flowing through the x_flip
    x_noisy = (
        x.detach() * (1 - x_flip.detach()) + (1 - x.detach()) * x_flip.detach()
    )
    # logging.debug(f"x_noisy: {x_noisy}")
    # logging.debug(f"x: {x}")
    # logging.debug(f"Sum diff: {torch.sum(x - x_noisy)}")
    return self.noisy_replace(x, x_noisy)

def _energy_channel_11(self, x):
    cat_probs = torch.ones_like(x) * 1 / x.shape[-1]
    # logging.debug(f"Categorical probabilities {cat_probs}")
    neighbors = torch.distributions.OneHotCategoricalStraightThrough(
        cat_probs
    ).sample(x.shape[:-2])

    x_0_mask = (x == -1).float() * neighbors
    x_0_flip = x_0_mask * \
        torch.bernoulli(self.p_0 * torch.ones_like(x_0_mask))
    # logging.debug(f"x_0_flip: {x_0_flip}")
    x_1_mask = (x == 1).float() * neighbors
    x_1_flip = x_1_mask * \
        torch.bernoulli(self.p_1 * torch.ones_like(x_1_mask))

    # logging.debug(f"x_1_flip: {x_1_flip}")
    x_flip = x_0_flip + x_1_flip
    x_noisy = x * (1 - x_flip) + (-1) * x * x_flip

    # logging.debug(f"x_noisy: {x_noisy}")
    # logging.debug(f"x: {x}")
    # logging.debug(f"Sum diff: {torch.sum(x - x_noisy)}")
    return self.noisy_replace(x, x_noisy)


#if __name__ == "__main__":
#    logging.basicConfig(level=logging.DEBUG)
#    H = torch.randn(121, 121).to("cuda").to(torch.float32)
#
#    def energy_fn(x):
#        return torch.einsum("bi,ij,bj->b", x, H, x)
#
#    channel = SimulatedAnnealingChannel(energy_fn, temperature=0.01, steps=3)
#    in_tensor = torch.randint(0, 2, [100, 121]).to("cuda").to(torch.float32)
#    out_tensor = channel(in_tensor)
#
