# Projet d'Analyse de Mobilité Urbaine

## Description
Ce projet implique la création d'un pipeline ETL pour l'ingestion, la transformation, et le stockage des données relatives à la disponibilité des vélos en temps réel dans plusieurs grandes villes de France, notamment Paris et Nantes. L'objectif est de mettre en pratique les connaissances acquises en ingénierie de données en développant un système capable de traiter et analyser des données en temps réel.

## Fonctionnalités
- **Ingestion de données** : Extraction automatique des données depuis les APIs ouvertes des villes concernées.
- **Consolidation de données** : Normalisation et unification des données pour préparer des analyses.
- **Agrégation de données** : Synthèse des données pour générer des insights utiles et des rapports.

## Prérequis
- Python 3.8 ou supérieur
- Bibliothèques Python : Pandas, Requests, DuckDB
- Accès Internet pour la récupération des données des APIs

## Installation
Clonez le dépôt GitHub, puis installez les dépendances à partir du fichier `requirements.txt` :

    git clone https://github.com/ahmedbergadi/polytech-de-101-2025-tp-subject.git
    cd polytech-de-101-2025-tp-subject
    pip install -r requirements.txt



## Structure du Projet
- `data/` : Contient l’ensemble des données du projet.
- `data/raw_data/` : Stocke les données brutes extraites directement depuis les APIs.
- `data/duckdb/` : Contient la base de données DuckDB utilisée pour le stockage et les transformations.
- `src/` : Regroupe les scripts Python implémentant les différentes étapes du pipeline ETL.
- `src/main.py` : Script principal permettant de lancer l’ensemble du pipeline de données.

## Usage
Pour exécuter le pipeline ETL et lancer l’ingestion, la consolidation et l’agrégation des données, utilisez la commande suivante :

    python src/main.py

Le script récupère automatiquement les données depuis les APIs, les transforme, puis les stocke dans la base DuckDB.

## Documentation
Le code est structuré de manière modulaire afin de faciliter la compréhension et la maintenance.  
Chaque script et fonction est documenté à l’aide de commentaires expliquant :
- le rôle de chaque module,
- les étapes du pipeline ETL,
- les choix de transformation et de stockage des données.

Cette documentation permet à tout utilisateur ou développeur de comprendre rapidement le fonctionnement global du projet.
