# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:06:21 2023

@author: danie
"""

from farmer import Farmer
from world import World
from strategy import GradualChange
from market import Market
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

w = World()
f1 = w.returnPriceCurve(2.15, 1E-6)
f2 = w.returnPriceCurve(5, 1E-6)
f3 = w.returnPriceCurve(4.95, 1E-6)
m = Market([f1,f2,f3])
 

f = Farmer("Bob", 5, 10, 10, 20, 100000, GradualChange(),100000)
f.init_yieldPerCrop([3,3,3])
f.init_fieldsPerCrop([10000,10000,10000])
f.addFact([30000,30000,30000,7,0,30000, 93000])
f.addFact([40000,20000,30000,7,0,30000, 66500])

farmer_subsistence = 40000
farmer_luxury = 20000
costsPerCrop = [0.6, 0.8, 0.6]


numberOfYears = 30

profits = []
money = [100000]
crops = []

for i in range(numberOfYears):
    print(i)
    masses = f.do()
    crops.append(masses)
    revenue = m.calcRev(masses)
    costs = f.calculateCosts(costsPerCrop, [7,7,7], [])
    profit = f.calculateProfit(revenue, costs)
    f.calculateMoney(profit, farmer_subsistence, farmer_luxury)
    money.append(f.getMoney())
    profits.append(profit)
    n_fields = f.fieldPlan[0]+ f.fieldPlan[1]+ f.fieldPlan[2]
    f.addFact([masses[0], masses[1], masses[2], 7, 0, n_fields, profit])

plt.clf()
plt.plot(money)
plt.savefig("money.png")