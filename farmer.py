# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 12:32:43 2023

@author: danie
"""

from brain import Brain
from strategy import GradualChange
from employee import Employee
import random
import torch
import torch.optim as optim
import torch.nn as nn
import torch.utils.data as data_utils


class Farmer:
    
    def __init__(self, name, n_layers, n_neurons, memory, N_opt_steps, money, strategy, maxFieldSize):
        self.name = name
        self.brain = Brain(n_layers, n_neurons)
        self.facts = []
        self.memory = memory
        self.N_opt_steps = N_opt_steps
        self.money = money
        self.strategy = strategy
        self.maxFieldSize = maxFieldSize
        
    def init_yieldPerCrop(self, yieldPerCrop):
        self.yieldPerCrop = yieldPerCrop
        
    def init_fieldsPerCrop(self, fieldsPerCrop):
        self.fieldsPerCrop = fieldsPerCrop
        
    def addFact(self,fact):
        self.facts.append(fact)
        if len(self.facts) > self.memory:
            self.facts.pop(0)
            
    def think(self):
        features = torch.FloatTensor([x[:-1] for x in self.facts])
        targets = torch.FloatTensor([x[-1] for x in self.facts])
        train = data_utils.TensorDataset(features, targets)
        train_loader = data_utils.DataLoader(train, batch_size=len(self.facts)-1, shuffle=True)
        optimizer = optim.Adam(self.brain.parameters(), lr=0.01)
        criterion = nn.MSELoss()
        losses = []
        for i in range(1000):
            for j, data in enumerate(train_loader):
                inputData, t = data
                out = self.brain.forward(inputData)
                loss = criterion(out, t)
                self.brain.zero_grad()
                loss.backward()
                optimizer.step()
                
    def plant(self):
        self.harvest = [self.fieldPlan[i]* self.yieldPerCrop[i] for i in range(len(self.fieldPlan))]
        
    def sell(self):
        return self.harvest
    
    def calculateCosts(self, costsPerCrop, costsPerField, employees):
        costs = 0
        for i in range(len(self.harvest)):
            costs += costsPerCrop[i]*self.harvest[i]
        for i in range(len(self.fieldPlan)):
            costs += costsPerField[i]*self.fieldPlan[i]
        for e in employees:
            costs += employees.getSalary()
        return costs
    
    def calculateProfit(self, revenue, cost):
        return (revenue - cost)
    
    def calculateMoney(self, prof, sub, lux):
        self.money += prof
        self.money -= (sub+lux)
    
    def getMoney(self):
        return self.money

        
    def do(self):
        self.think()
        s = self.strategy.strategize(self.facts, self.N_opt_steps, self.brain, self.yieldPerCrop, self.maxFieldSize)
        self.fieldPlan = [round(s[0]/self.yieldPerCrop[0]), round(s[1]/self.yieldPerCrop[1]), round(s[2]/self.yieldPerCrop[2])]
        self.plant()
        return self.sell()


if __name__ == "__main__":
    f = Farmer("Bob", 5, 10, 10, 10, 100000, GradualChange(),100000)
    f.init_yieldPerCrop([3,3,3])
    f.init_fieldsPerCrop([10000,10000,10000])
    f.addFact([30000,30000,30000,7,0,30000, 33000])
    f.addFact([40000,20000,30000,7,0,30000, 6500])
    print(f.do())
    

