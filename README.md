# 🏦 Banking Modern Data Stack

![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?logo=snowflake&logoColor=white)
![DBT](https://img.shields.io/badge/dbt-FF694B?logo=dbt&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?logo=apacheairflow&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?logo=apachekafka&logoColor=white)
![Debezium](https://img.shields.io/badge/Debezium-EF3B2D?logo=apache&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)



---

📌 Présentation du projet

Ce projet illustre une pipeline de données moderne de bout en bout appliquée au secteur bancaire.
Il simule des données de clients, de comptes et de transactions, diffuse les changements en temps réel, transforme ces données en modèles prêts pour l’analyse, et visualise les résultats — en suivant les bonnes pratiques de data warehousing.

👉 En résumé, c’est un écosystème de données bancaires complet construit avec des outils modernes.



🏗️ Architecture
<img src="images/architecture.png" alt="Architecture" width="800"/>

Flux de la pipeline :

Générateur de données → Simule les transactions, comptes et clients bancaires (via Faker).

Kafka + Debezium → Diffuse les changements en temps réel (CDC) vers(Amazon S3).

Snowpipe → Ingestion automatique de S3 vers Snowflake

Snowflake → Entrepôt de données Cloud (Bronze → Silver → Gold).

Airflow →  les snapshots vers Snowflake.

DBT → Effectue les transformations et construit les marts & snapshots (SCD Type-2).

Power BI →  Création du Dashboard

Dokcer → Conténerisation

⚡ Stack technologique

Snowflake → Entrepôt de données cloud

DBT → Transformations, tests, snapshots (SCD Type-2)

Apache Airflow → Orchestration & planification de DAGs

Apache Kafka + Debezium → Streaming temps réel & CDC

Amazon S3 → Data lake

PostgreSQL → Base de données source (OLTP)

Python (Faker) → Génération de données simulées

Docker & docker-compose → Environnement containerisé



✅ Fonctionnalités principales

PostgreSQL OLTP : Base transactionnelle respectant les contraintes ACID (clients, comptes, transactions)

Système bancaire simulé : clients, comptes et opérations bancaires

Capture de changement de données (CDC) via Kafka + Debezium (lecture du WAL de Postgres)

Ingestion automatique depuis s3 vers snowflake via snowpipe

Modèles DBT : Raw → Staging → Faits & Dimensions

Snapshots : suivi historique des données (slowly changing dimensions)

Orchestration automatique avec Airflow


📊 Livrables finaux

Jeu de données bancaires synthétiques pour démonstration

Pipeline CDC automatisée de Postgres → Snowflake

Modèles DBT (faits, dimensions, snapshots)

DAGs Airflow orchestrés

Dashboard Power BI pour le suivi en temps réel des données bancaires

<img src="images/dashboard.png" alt="Architecture" width="800"/>