import matplotlib.pyplot as plt
import numpy as np  # <-- cette ligne est essentielle !

# Choc carbone : augmentation soudaine du prix du carbone
annees = np.arange(2020, 2031)
carbon_price = [30, 35, 40, 45, 50, 100, 110, 120, 130, 140, 150]

# Inflation en réponse à ce choc
inflation = [1.5, 1.7, 1.8, 1.9, 2.0, 3.2, 2.8, 2.5, 2.3, 2.1, 2.0]

# Réponse du taux directeur
interest_rate = [0.5, 0.75, 1.0, 1.25, 1.5, 2.75, 2.5, 2.25, 2.0, 1.75, 1.5]

# Tracé des courbes
plt.figure(figsize=(10, 6))
plt.plot(annees, carbon_price, label="Prix du carbone (€/tCO₂)", color="green", marker="o")
plt.plot(annees, inflation, label="Inflation (%)", color="red", marker="s")
plt.plot(annees, interest_rate, label="Taux directeur (%)", color="blue", marker="^")
plt.title("Effets simulés d’un choc de prix du carbone sur l'économie")
plt.xlabel("Année")
plt.ylabel("Valeur")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
