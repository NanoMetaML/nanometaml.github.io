import nanomodules
import torch

def load_nodes_from_config(nodes, name, loss, **kwargs):
    
    node_list = []
    for node in nodes:
        node_list.append(nanomodules.load_module_endpoint(**node.kwargs))

    loss = nanomodules.load_module_endpoint(node_list, **loss.kwargs)

    class Model(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.nodes = torch.nn.ModuleList(node_list)
            self.loss = loss
            self.name = name

        def forward(self, x):
            for node in self.nodes:
                x = node(x)
            return x

        def loss(self, x, y):
            return loss(x, y)

    return Model() 
    

