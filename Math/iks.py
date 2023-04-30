from yahoo_fin import stock_info as si
import pandas as pd

print(si.get_stats_valuation('nflx'))
valuations = si.get_stats_valuation('nflx')
df = pd.DataFrame(valuations)

row= df.loc[df[0] == 'Price/Sales (ttm)']
row1= df.loc[df[0] == 'Price/Book (mrq)']
price_sales = row.iloc[0,1]
price_book = row1.iloc[0,1]
print(price_sales)
print(price_book)




import matplotlib.pyplot as plt

# Výpočet procentuálního rozdílu
percent_difference = abs(1.2 - 0.8) / ((1.2 + 0.8) / 2) * 100

# Vytvoření nového subplotu pro zobrazení rozdílu
fig, ax = plt.subplots()

# Nastavení limitů os pro subplot
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])

# Vykreslení horizontálních čar
plt.axhline(y=1.2, color='g', linestyle='-')
plt.axhline(y=0.8, color='r', linestyle='-')

# Zvýraznění rozdílu a vyšrafování
plt.axhspan(ymin=0.8, ymax=1.2, facecolor='blue', alpha=0.3, hatch='///')

# Přidání popisku s procentuálním rozdílem mimo graf
plt.text(2.1, 1, f'{percent_difference:.2f}%', ha='left', va='center')

# Zobrazení grafu
plt.show()