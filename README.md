Ce dossier est associé au projet qui se trouve à l'adresse suivante: https://github.com/JulienNicola/Projet7

# Utilisation des différents fichiers dans le process de déploiement:	

**github/workflows/deploy_workflow.yml**: coordination des différentes actions de déploiement dans Github et Azure

**.dockerignore / Dockerfile**: documents permetttant de générer l'image qui va ensuite être containérisée dans Azure

**fast_api.py**: code permettant de générant l'application avec Fast API

**lgbm.pkl**: document stockant le modèle LIGHTGBM sélectionné via le travail de modélisation qui sera chargé dans l'application

**threshold.pkl**: seuil de probavilité déterminé via notre travail de modélisation afin d'optimiser notre fonction cout métier

**requirements.txt**: librairies python nécessaires pour l'application

**test_predict.py et test_sample.csv**: fichiers permettant de réaliser des tests unitaires sur la fonction de prédiction au cours du déploiement

