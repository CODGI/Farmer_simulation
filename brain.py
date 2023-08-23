# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 11:27:56 2023

@author: danie
"""

import torch

import torch
import torch.nn as nn
import torch.nn.functional as F

class Brain(nn.Module):
    
    def __init__(self, numberOfLayers, neuronsPerLayer):
        super(Brain, self).__init__()
        self.fc = []
        self.fc.append(nn.Linear(6, neuronsPerLayer))
        for i in range(1,numberOfLayers-1):
            self.fc.append(nn.Linear(neuronsPerLayer, neuronsPerLayer))
        self.fc = nn.ModuleList(self.fc)
        self.output = nn.Linear(neuronsPerLayer, 1)
        
    def forward(self, x):
        for f in self.fc:
            x = f(x)
            x = F.relu(x)
        x = self.output(x)
        return x

if __name__ == "__main__":
    from generateData import findProfit
    import matplotlib.pyplot as plt
    import os
    import torch.optim as optim
    os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
    brain = Brain(5,10)
    rev = [2.15, 5, 4.95]
    costs = [0.6, 0.8, 0.6]
    masses = [30000, 30000, 30000]
    sub = 40000
    lux = 20000
    NF = 10
    CF = 20000
    NE = 0
    CE = 30000 
    p = findProfit(rev, costs, masses, sub, lux, NF, CF, NE, CE)
    print(p)
    target = torch.tensor(p)
    optimizer = optim.Adam(brain.parameters(), lr=0.01)
    criterion = nn.MSELoss()
    losses = []
    for i in range(300):
        out = brain.forward(torch.FloatTensor([masses[0],masses[1],masses[2],lux,0,30000]))
        loss = criterion(out, target)
        losses.append(loss.item())
        brain.zero_grad()
        loss.backward()
        optimizer.step()
    plt.clf()
    plt.plot(losses)
    plt.yscale("log")
    plt.savefig("losses_test.png")