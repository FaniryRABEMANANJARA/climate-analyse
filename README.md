🇫🇷 README (version française)
markdown
Copier
Modifier
# 📘 Analyse économique : Taux d’intérêt et Changement Climatique en Europe

Ce projet accompagne une recherche universitaire portant sur **l’interaction entre les politiques monétaires (notamment les taux d’intérêt)** et **le changement climatique**, avec un accent particulier sur le contexte européen.

Les scripts Python proposés permettent de :

✅ Simuler des relations économiques entre taux d’intérêt et investissement vert  
✅ Visualiser les réponses économiques à des chocs climatiques (ex. augmentation du prix du carbone)  
✅ Réaliser une analyse économétrique en panel data par pays  
✅ Générer des graphiques interactifs avec sélection du pays d’étude  
✅ Afficher les intervalles de confiance pour les régressions estimées  

---

## 📂 Contenu des fichiers

- `simulation-choc-politique-climatic-economie.py`  
  ➤ Visualisation des effets d’un choc climatique (ex. prix carbone) sur l’inflation et les taux d’intérêt.

- `analyse-anomalies-climatiques.py`  
  ➤ Modélisation VAR pour simuler l’effet des anomalies climatiques sur les taux d’intérêt.

- `panel_green_investment.py`  
  ➤ Régression en données de panel sur l’effet des taux d’intérêt sur l’investissement vert (France, Allemagne, Pologne).

- `panel_interactif.py`  
  ➤ Version interactive avec menu déroulant pour sélectionner un pays et afficher la régression avec intervalle de confiance.

---

## 🧰 Dépendances

Installez les bibliothèques nécessaires :

```bash
pip install pandas numpy matplotlib seaborn statsmodels ipywidgets
⚠️ Si vous utilisez Jupyter Notebook ou Google Colab, ipywidgets doit être activé.

📊 À venir
Intégration de données réelles (Banque centrale européenne, Green Bond Index, etc.)

Modèle DSGE simplifié

Carte thermique de la prime de risque climatique par pays

👨‍🎓 Auteur
Ce dépôt est réalisé dans le cadre d’un mémoire de recherche sur l’économie du climat et les politiques monétaires européennes, incluant une dimension empirique et théorique.