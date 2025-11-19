import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

current_price = 120000                   
annual_growth_rate = 0.05          
n_years = 5
n_months = n_years * 12

rate_annual = 0.12                       # roczna stopa zwrotu 12%
r = rate_annual / 12                     
# orientacyjna cena mieszkania za 5 lat
FV_price = current_price * (1 + annual_growth_rate)**n_years
print(f"Przewidywana cena mieszkania za 5 lat: {FV_price:.2f} zł")

# Wyliczenie miesięcznej wpłaty
PMT = -npf.pmt(rate=r, nper=n_months, pv=0, fv=FV_price)
print(f"Potrzebna miesięczna wpłata: {PMT:.2f} zł")

balance = np.zeros(n_months)       # wartość kapitału łącznie
deposits = np.zeros(n_months)      # suma wpłat
interests = np.zeros(n_months)     # odsetki
price_growth = np.zeros(n_months)  # wartość mieszkania miesiąc po miesiącu


balance[0] = PMT
deposits[0] = PMT
interests[0] = 0
price_growth[0] = current_price


for i in range(1, n_months):
    balance[i] = balance[i - 1] * (1 + r) + PMT
    deposits[i] = deposits[i - 1] + PMT
    interests[i] = balance[i] - deposits[i]
    price_growth[i] = current_price * (1 + annual_growth_rate)**(i / 12)


print(f"Łącznie wpłacone: {deposits[-1]:.2f} zł")
print(f"Odsetki zarobione: {interests[-1]:.2f} zł")
print(f"Wartość portfela po 5 latach: {balance[-1]:.2f} zł")


plt.figure(figsize=(10, 6))
plt.plot(balance, label='Wartość portfela (kapitał + odsetki)', color='black', linewidth=2)
plt.plot(deposits, label='Suma wpłat', linestyle='--', color='blue')
plt.fill_between(range(n_months), deposits, balance, color='gold', alpha=0.3, label="Odsetki")

plt.plot(price_growth, label='Cena mieszkania', color='red', linestyle='-.', linewidth=2)

plt.title("Wzrost oszczędności i ceny mieszkania przez 5 lat")
plt.xlabel("Miesiące")
plt.ylabel("Wartość [zł]")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()