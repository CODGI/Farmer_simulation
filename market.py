# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 16:20:01 2023

@author: danie
"""

from generateData import findProfit
from world import World

class Market:
    
    def __init__(self, curves):
        self.curves = curves
    
    def calcRev(self, masses):
        rev = 0
        for i in range(len(masses)):
            rev += masses[i]*self.curves[i](masses[i])
        return rev
    
if __name__ == "__main__":
    w = World()
    f1 = w.returnPriceCurve(3, 0.001)
    f2 = w.returnPriceCurve(4, 0.01)
    f3 = w.returnPriceCurve(2, 0.001)
    m = Market([f1,f2,f3])
    print(m.calcRev([100,100,100]))
        