# Projet Python – CBIR (Content-Based Image Retrieval)

Ce projet est une application de recherche d’images par le contenu (CBIR) développée dans le cadre du cours 420-1AB-TT : Intelligence Artificielle et Reconnaissance de Formes. L’objectif est de permettre à un utilisateur de retrouver des images similaires à partir d’un exemple, en comparant leurs signatures visuelles extraites automatiquement.

# Objectif pédagogique

- Appliquer des techniques de vision par ordinateur et de machine learning à un problème concret
- Utiliser descripteurs visuels (GLCM et BiT)
- Développer une interface de recherche d’images intuitive et performante
- Calculer des distances de similarité entre images

# Technologies utilisées

- Python
- Streamlit (interface web)
- NumPy, OpenCV, scikit-image
- Descripteurs : GLCM, BiT
- Mesures de distance : Euclidienne, Manhattan, Chebyshev, Canberra

# Structure du projet

- `app_cbir.py` : Script principal de l’application Streamlit
- `app_distance.py` : Interface pour tester les distances
- `BiT.py`, `descriptor.py` : Extraction descripteur BiT et GLCM
- `data_signatures.py`, `signatures.npy` : Gestion des signatures d’images
- `distances.py` : Fonctions de comparaison d’images
- `cbir_datasets/` : Jeux d’images à indexer
- `images/` : Contient les images de test
- `site/` : Interface utilisateur
- `iris.jpg` : Image d’exemple
- `__pycache__/` : Cache Python

# Fonctionnalités de l'application

- Téléversement d’une image par l’utilisateur
- Choix du descripteur (GLCM ou BiT)
- Choix du nombre d’images similaires à afficher
- Choix de la distance de comparaison (Euclidienne, Manhattan, Chebyshev, Canberra)
- Affichage rapide des images les plus proches

# Instructions pour exécuter en local

1. Installer les dépendances :

```bash
pip install -r requirements.txt
```

2. Lancer l’application :

```bash
streamlit run app_cbir.py
```

3. Naviguer dans l’interface et explorer les résultats.

# Auteur

Projet réalisé par Kaemly Morisseau, dans le cadre du cours 420-1AB-TT à l’Institut Teccart.
