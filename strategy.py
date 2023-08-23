# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 11:52:11 2023

@author: danie
"""
import torch 

class Strategy:
    def strategize(self, facts, N_steps, brain, yieldPerCrop, maxFieldSize):
        pass
    
class GradualChange(Strategy):
    def strategize(self, facts, N_steps, brain, yieldPerCrop, maxFields):
        base = facts[-1]
        fieldChange1 = round(100/yieldPerCrop[0])
        fieldChange2 = round(100/yieldPerCrop[1])
        fieldChange3 = round(100/yieldPerCrop[2])
        for i in range(N_steps):
            out1 = brain.forward(torch.FloatTensor([base[0]+100,base[1],base[2],base[3],base[4],base[5]+fieldChange1]))
            out2 = brain.forward(torch.FloatTensor([base[0]-100,base[1],base[2],base[3],base[4],base[5]-fieldChange1]))
            if out1.item() > base[-1]:
                base = [base[0]+100,base[1],base[2],base[3],base[4],base[5]+fieldChange1, out1.item()]
            if out2.item() > base[-1]:
                base = [base[0]-100,base[1],base[2],base[3],base[4],base[5]-fieldChange1, out2.item()]
            out3 = brain.forward(torch.FloatTensor([base[0],base[1]+100,base[2],base[3],base[4],base[5]+fieldChange2]))
            out4 = brain.forward(torch.FloatTensor([base[0],base[1]-100,base[2],base[3],base[4],base[5]-fieldChange2]))
            if out3.item() > base[-1]:
                base = [base[0],base[1]+100,base[2],base[3],base[4],base[5]+fieldChange2, out3.item()]
            if out4.item() > base[-1]:
                base = [base[0],base[1]-100,base[2],base[3],base[4],base[5]-fieldChange2, out4.item()]
            out5 = brain.forward(torch.FloatTensor([base[0],base[1],base[2]+100,base[3],base[4],base[5]+fieldChange3]))
            out6 = brain.forward(torch.FloatTensor([base[0],base[1],base[2]-100,base[3],base[4],base[5]-fieldChange3]))
            if out5.item() > base[-1]:
                base = [base[0],base[1],base[2]+100,base[3],base[4],base[5]+fieldChange3, out5.item()]
            if out6.item() > base[-1]:
                base = [base[0],base[1],base[2]-100,base[3],base[4],base[5]-fieldChange3, out6.item()]
        if base[5] > maxFields:
            base = [round(base[0]*maxFields/base[5]),round(base[1]*maxFields/base[5]),round(base[2]*maxFields/base[5]),base[3],base[4], maxFields, base[6]]
        return base


        