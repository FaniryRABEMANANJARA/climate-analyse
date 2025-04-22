# 1. Importer les bibliothèques
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.tsa.api import VAR

# 2. Générer des données simulées trimestrielles (2000-2024)
np.random.seed(42)
dates = pd.date_range(start="2000-01-01", periods=100, freq="Q")
interest_rate = 2 + 0.05*np.arange(100) + np.random.normal(0, 0.3, size=100)  # Tendance haussière
temperature_anomaly = 0.2 + 0.01*np.arange(100) + np.random.normal(0, 0.05, size=100)  # Réchauffement progressif

data = pd.DataFrame({
    "interest_rate": interest_rate,
    "temperature_anomaly": temperature_anomaly
}, index=dates)

# 3. Visualisation des séries
plt.figure(figsize=(12, 5))
sns.lineplot(data=data)
plt.title("Taux d'intérêt et Anomalie de Température (données simulées)")
plt.ylabel("Valeur")
plt.xlabel("Année")
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Modèle VAR
model = VAR(data)
results = model.fit(2)

# 5. Fonctions de réponse impulsionnelle
irf = results.irf(10)
irf.plot(orth=False)
plt.suptitle("Réponse impulsionnelle : Effet d’un choc climatique sur les taux d’intérêt", y=1.02)
plt.tight_layout()
plt.show()
