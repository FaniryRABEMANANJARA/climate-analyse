import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
from IPython.display import clear_output, display

# 1. Génération de données simulées
np.random.seed(1)
years = list(range(2010, 2021))
countries = ["France", "Germany", "Poland"]

rows = []
for country in countries:
    for year in years:
        interest = np.random.uniform(0.5, 3.5)
        green_inv = 100 - 10 * interest + np.random.normal(0, 5)
        rows.append({
            "country": country,
            "year": year,
            "interest_rate": interest,
            "green_investment": green_inv
        })

panel_data = pd.DataFrame(rows)

# 2. Régression OLS avec effets fixes pays
model = smf.ols('green_investment ~ interest_rate + C(country)', data=panel_data).fit()

# 3. Fonction de mise à jour du graphique selon le pays
def plot_country(selected_country):
    interest_vals = np.linspace(panel_data["interest_rate"].min(), panel_data["interest_rate"].max(), 100)
    
    predict_df = pd.DataFrame({
        "interest_rate": interest_vals,
        "country": selected_country
    })

    predictions = model.get_prediction(predict_df)
    pred_summary = predictions.summary_frame(alpha=0.05)
    predict_df["predicted"] = pred_summary["mean"]
    predict_df["ci_lower"] = pred_summary["mean_ci_lower"]
    predict_df["ci_upper"] = pred_summary["mean_ci_upper"]

    # Affichage
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=panel_data[panel_data["country"] == selected_country],
                    x="interest_rate", y="green_investment", label=f"Observations ({selected_country})", alpha=0.6)
    plt.plot(predict_df["interest_rate"], predict_df["predicted"], color="black", label="Régression estimée")
    plt.fill_between(predict_df["interest_rate"], predict_df["ci_lower"], predict_df["ci_upper"],
                     color="gray", alpha=0.3, label="IC 95%")
    
    plt.title(f"Effet du taux d'intérêt sur l'investissement vert ({selected_country})")
    plt.xlabel("Taux d'intérêt (%)")
    plt.ylabel("Investissement vert (index)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 4. Création du widget interactif
dropdown = widgets.Dropdown(options=countries, description='Pays:')
output = widgets.Output()

def on_change(change):
    with output:
        clear_output(wait=True)
        plot_country(change['new'])

dropdown.observe(on_change, names='value')
display(dropdown, output)

# Lancer avec un pays par défaut
with output:
    plot_country(dropdown.value)
