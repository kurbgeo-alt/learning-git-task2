import numpy as pd
import numpy financial as npf
import maltplotlib.pyplot as plt
freq=0.05
rate =0.12
years =5
pv = 120000
rate /= freq
nper = years*freq


interest_equal = -np.around(npf.ipmt(rate,periods,nper,pv),2)
interest_equal[:10]
np.set_printoptions(supress= True)
principal_decreasing = np.around(np.zeros(nper) + (pv/nper),2)
principal_decreasing[:10]
balance = np.zeros(nper) + pv
balance_close = np.around(balance - np.cumsum(principal_decreasing),2)
balance_close[[0,1,2,-3,-2,-1]]
np.cumsum(principal_decreasing)[:10]
balance_open = balance_close + principal_decreasing
interest_decreasing = -np.around(balance_open * rate,2)
interest_decreasing[:10]
print("Wartośc odsetek do zapłaty  w wariancie kredytu w równych ratach wynosi:" + str("{:.2f}".format(interest_equal.sum())))
print("Wartośc  odsetek do zapłaty w wariancie kredytu w ratach malejących wynosi: + str(*{:.2f}".format(interest_equal.sum()))

plt.plot(interest_equal.cumsum(),label='raty równe')
plt.plot(interest_decreasing.cumsum(),label='raty malejące')
plt.legend()
plt.xlabel('Liczba okresów')
plt.ylabel = ('Skumulowana wartość')