import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

#hyperparameters
n_input = 0
n_hidden = 0
n_output = 0


class Model(nn.Module):
    def __init__(self, n_input, n_hidden, n_output):
        super().__init__()
        self.lstm = nn.LSTMCell(self.n_input, self.n_hidden)
        self.linear = nn.Linear(self.n_hidden, self.n_output)

    def forward(self, 
