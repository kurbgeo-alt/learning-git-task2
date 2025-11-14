import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
#Dane dotyczące nieruchomości
#obecna cena = 120000"
#roczny wzrost 5% (0.05)
#cena za 5 lat(FV)=120000*(1+0.05)^5=12000*1.27628= 153153.79
# docelowa kwota  153153.79 zł okres 5 lat(60 miesięcy)

FV = 153153.79 # Orientacyjna cena mieszkania za 5 lat 
current_price =120000 
n_years= 5
n_months = n_years *12
rate_annual = 0.12
r = rate_annual/12 #miesięczna stopa procentowa 

#Wyliczenie miesięcznej wpłaty(PMT) z użyciem numpy financial
#npf.pmt(rate,nper,pv,fv,when)
PMT= -npf.pmt(rate =r,nper = n_months,pV=0, fv = -FV,when ='end')



balance = np.zeros(n_months)
deposits = np.zeros(n_months)
interests = np.zeros(n_months)


balance[0]= PMT


for i in range(1,n_months):
    balance[i] = balance[i-1]  * (1 + r) + PMT
    deposits[i] = PMT * (i +1) 
    interests[i] = balance[i] - deposits[i]

    

print(f"Miesięczna wpłata : {PMT:.2f} zł")    
print(f"Łącznie wpłacone:{deposits[-1]:.2f} zł")
print(f"Odsetki zarobione:{interests[-1]:.2f} zł")


plt.figure(figsize =(9,5))
plt.plot(balance,label = 'Całkowity kapitał', color = 'black',linewidth = 2)
plt.plot(deposits,label = 'Suma wpłat(kapitał własny)',linestyle ='--',color='blue')
plt.fill_between(range(n_months),deposits,balance,color = 'gold',alpha =0.3,label = "Odsetki i zysk")
plt.title("Wzrost oszczędności po 5 latach przy 12% rocznej stopie zwrotu")
plt.xlabel("Miesiące")
plt.ylabel("Zgromadzony kapitał[zł]")
plt.legend()
plt.tight_layout()
plt.show()






