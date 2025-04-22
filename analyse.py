import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR

# Exemple de données simulées : taux d'intérêt et température
np.random.seed(0)
dates = pd.date_range(start="2000-01-01", periods=80, freq="Q")
data = pd.DataFrame({
    "interest_rate": np.random.normal(2, 0.5, size=80).cumsum(),
    "temperature_anomaly": np.random.normal(0.1, 0.02, size=80).cumsum()
}, index=dates)

# VAR model
model = VAR(data)
results = model.fit(2)

# Affichage des résultats
print(results.summary())

# Tracer les fonctions de réponse impulsionnelle
irf = results.irf(10)
irf.plot(orth=False)
plt.tight_layout()
plt.show()
