import random
import torch
from torch import nn
from src.TicTacToe import TicTacToe

class TicTacNet(nn.Module):
  def __init__(self, n_inpt: int, n_hidn: int, n_oupt: int):
    super(TicTacNet, self).__init__()
    self.f1 = nn.Linear(in_features=n_hidn, out_features=n_hidn)
    self.f2 = nn.Linear(in_features=n_hidn, out_features=n_hidn)
    self.f3 = nn.Linear(in_features=n_hidn, out_features=n_oupt)
    self.relu = nn.ReLU()
  # __init__

  def forward(self, x):
    x = self.f1(x)
    x = self.relu(x)
    x = self.f2(x)
    x = self.relu(x)
    x = self.f3(x)
    x = self.relu(x)
    return x
  # forward
# TicTacNet

class TicTacAgent:
  def __init__(self, model_config: tuple, hyper_parameter: dict):
    self.lr, self.gamma = hyper_parameter['lr'], hyper_parameter['gamma']
    self.epsilon = hyper_parameter['epsilon']
    self.epsilon_decay, self.epsilon_min = hyper_parameter['epsilon_decay'], hyper_parameter['epsilon_min']
    self.game = TicTacToe()
    self.model = TicTacNet(*model_config)
  # __init__

  def pi(self, state, actions):
# TicTacAgent
