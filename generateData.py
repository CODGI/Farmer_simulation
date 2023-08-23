# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 10:49:58 2023

@author: danie
"""

def findProfit(revenuePerKg, costsPerKg, massInKg, Subsistence, Luxury, numberOfFields, costsPerFied, numberOfEmployees, costPerEmployee):
    profit = 0
    for i in range(len(massInKg)):
        profit += (revenuePerKg[i] - costsPerKg[i]) * massInKg[i]
    profit -= numberOfFields*costsPerFied
    profit -= numberOfEmployees*costPerEmployee
    return profit


if __name__ == "__main__":
    rev = [2.15, 5, 4.95]
    costs = [0.6, 0.8, 0.6]
    masses = [40000, 20000, 30000]
    sub = 40000
    lux = 20000
    NF = 30000
    CF = 7
    NE = 0
    CE = 30000 

    print(findProfit(rev, costs, masses, sub, lux, NF, CF, NE, CE))