from data_agregation import (
    create_agregate_tables,
    agregate_dim_city,
    agregate_dim_station,
    agregate_fact_station_statements
)
from data_consolidation import (
    create_consolidate_tables,
    consolidate_city_data,
    consolidate_station_data,
    consolidate_station_statement_data
)
from data_ingestion import (
    get_paris_realtime_bicycle_data,
    get_nantes_realtime_bicycle_data,  # Ajout pour gérer l'ingestion de données pour Nantes
    get_commune_data
)

def main():
    # Début du processus ETL.
    print("Début du processus.")

    # Étape 1 : Ingestion des données
    # Récupération des données en temps réel depuis les APIs publiques pour les stations de vélos à Paris, Toulouse, Nantes et les communes françaises.
    print("Début de l'ingestion des données.")
    get_paris_realtime_bicycle_data()
    get_nantes_realtime_bicycle_data()
    get_commune_data()
    print("Fin de l'ingestion des données.")

    # Étape 2 : Consolidation des données
    # Les données sont nettoyées, transformées et chargées dans une base de données DuckDB pour un stockage structuré.
    print("Début de la consolidation des données.")
    create_consolidate_tables()  # Création des tables nécessaires dans la base de données.
    consolidate_city_data()      # Consolidation des données concernant les villes.
    consolidate_station_data()   # Consolidation des données concernant les stations de vélos.
    consolidate_station_statement_data()  # Consolidation des données transactionnelles des stations.
    print("Fin de la consolidation des données.")

    # Étape 3 : Agrégation des données
    # Les données sont davantage traitées pour créer des vues agrégées adaptées à l'analyse.
    print("Début de l'agrégation des données.")
    create_agregate_tables()  # Préparation des tables pour stocker les données agrégées.
    agregate_dim_city()       # Agrégation des données pour les dimensions liées aux villes.
    agregate_dim_station()    # Agrégation des données pour les dimensions liées aux stations.
    agregate_fact_station_statements()  # Agrégation des données transactionnelles dans des tables de faits.
    print("Fin de l'agrégation des données.")

if __name__ == "__main__":
    main()