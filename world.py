# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 16:07:16 2023

@author: danie
"""

class World:
    
    def returnPriceCurve(self, zeroCut, slope):
        return lambda x: max(0,zeroCut - slope*x)
    

if __name__ == "__main__":
    w = World()
    f = w.returnPriceCurve(3, 0.001)
    print(f(10))