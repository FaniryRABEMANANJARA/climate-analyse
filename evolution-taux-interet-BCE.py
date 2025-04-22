import matplotlib.pyplot as plt
import pandas as pd

# Données simulées des taux d'intérêt de la BCE (en %)
dates = pd.date_range(start='2008-01-01', periods=17, freq='Y')
taux_bce = [4.25, 3.75, 1.00, 1.00, 0.75, 0.25, 0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.50, 1.50, 2.50]

# Données simulées des émissions d'obligations vertes (en milliards USD)
emissions_vertes = [0.5, 0.8, 1.2, 1.5, 2.0, 2.5, 3.0, 3.8, 4.5, 5.2, 6.0, 7.0, 8.5, 10.0, 12.0, 14.0, 16.0]

# Création d'un DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Taux_BCE': taux_bce,
    'Emissions_Vertes': emissions_vertes
})

# Tracer les données
fig, ax1 = plt.subplots(figsize=(12, 6))

color = 'tab:red'
ax1.set_xlabel('Année')
ax1.set_ylabel('Taux BCE (%)', color=color)
ax1.plot(df['Date'], df['Taux_BCE'], color=color, marker='o', label='Taux BCE')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')

ax2 = ax1.twinx()  # Instancier un second axe qui partage le même axe x
color = 'tab:green'
ax2.set_ylabel('Émissions d\'obligations vertes (Mds USD)', color=color)
ax2.plot(df['Date'], df['Emissions_Vertes'], color=color, marker='s', label='Obligations vertes')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

plt.title('Évolution des taux d\'intérêt de la BCE et des émissions d\'obligations vertes')
plt.grid(True)
plt.tight_layout()
plt.show()
